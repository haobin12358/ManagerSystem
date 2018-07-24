# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from ManagerSystem.globals import log
from ManagerSystem.service.SOrder import SOrder
from ManagerSystem.service.SManager import SManager
from ManagerSystem.service.SProducts import SProducts

from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.ResultManager import todict, tolist
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.TimeManagert import TimeManager

from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR
from ManagerSystem.config import conversion as cvs


class COrder():
    def __init__(self):
        self.sorder = SOrder()
        self.suser = SManager()
        self.sproduct = SProducts()

    def get_order_list(self):
        try:
            args = request.args.to_dict()
            log.info("args", args)
            if "token" not in args or "page_size" not in args or "page_num" not in args:
                return PARAMS_MISS
            page_size = int(args.get("page_size"))
            page_num = int(args.get("page_num"))
            maid = token_to_usid(args.get("token"))
            from ManagerSystem.models.model import Products
            product_filter = {
                Products.MAid == maid
            }
            if args.get("PRname"):
                product_filter.add(Products.PRname.like("%{0}%".format(get_str(args, "PRname"))))

            product_list = tolist(self.sproduct.get_product_by_filter(product_filter))
            log.info("product list ", product_list)
            pb_list = []
            for product in product_list:
                product["PBunit"] = cvs.conversion_PBunit.get(product.get("PBunit", "其他币种"))
                product["PRbrand"] = cvs.conversion_PRbrand.get(product.get("PRbrand"), "其他")
                product["PRtype"] = cvs.conversion_PRtype.get(product.get("PRtype"))
                for pb in tolist(self.sproduct.get_pball_by_prid(product.get("PRid"))):
                    pb.update(product)
                    pb_list.append(pb)
            log.info("pb_list", pb_list)
            om_list = []
            om_id_dict = {}
            from ManagerSystem.models.model import OrderMain
            omfilter = set()
            if args.get("OMstatus"):
                omstatus = cvs.conversion_OMstatus_reverse.get(get_str(args, "OMstatus"))
                omfilter.add(OrderMain.OMstatus == omstatus)
            if args.get("OMlogisticsName"):
                omfilter.add(OrderMain.OMlogisticsName == get_str(args, "OMlogisticsName"))
            if args.get("OMstartTime"):
                omfilter.add(OrderMain.OMtime >= TimeManager.get_db_time_str(args.get("OMstartTime")))
            if args.get("OMendTime"):
                omfilter.add(OrderMain.OMtime <= TimeManager.get_db_time_str(args.get("OMendTime")))

            for pb in pb_list:
                op_pb_list = tolist(self.sorder.get_order_part_list_by_pbid(pb.get("PBid")))
                for op_pb in op_pb_list:
                    op_pb.update(pb)
                    if op_pb.get("OMid") in om_id_dict:
                        om_id_dict[op_pb.get("OMid")].append(op_pb)
                    else:
                        om_id_dict[op_pb.get("OMid")] = [op_pb]
            log.info("om_id_dict", om_id_dict)
            for om_id in om_id_dict:
                if args.get("OMid") and args.get("OMid") not in om_id:
                    continue
                omfilter_tmp  = omfilter.copy()
                omfilter_tmp.add(OrderMain.OMid == om_id)
                om_dict = tolist(self.sorder.get_om_by_filter(omfilter_tmp))

                if not om_dict:
                    continue
                om_dict = om_dict[0]
                om_count = {k: 0 for k in cvs.conversion_OMstatus}

                om_dict.update({"order_item": om_id_dict.get(om_id)})
                location = todict(self.sorder.get_location_by_usid(om_dict.pop("USid")))
                log.info("location", location)
                om_count[om_dict.get("OMstatus")] = om_count.get(om_dict.get("OMstatus")) + 1
                om_dict.update(location)
                om_dict["OMcointype"] = cvs.conversion_PBunit.get(om_dict.get("OMcointype"), "其他币种")
                om_dict["OMstatus"] = cvs.conversion_OMstatus.get(om_dict.get("OMstatus"), 0)
                om_dict["OMtime"] = TimeManager.get_web_time_str(om_dict.get("OMtime"))

                om_list.append(om_dict)
            log.info("omlist", om_list)
            count = len(om_list)
            if page_size * page_num > count:
                page_num = count / page_size + 1
            page_num = page_num if page_num > 0 else 1
            om_list = om_list[(page_num - 1) * page_size: page_num * page_size]
            data = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            data["data"] = {
                "count": count,
                "page_num": page_num,
                "page_size": page_size,
                "OrderMains": om_list,
                "OMcount": om_count
            }
            return data
        except Exception as e:
            log.error("get order list", e.message)
            import traceback
            print(traceback.format_exc())
            return SYSTEM_ERROR

    def get_order_abo(self):
        try:
            args = request.args.to_dict()
            log.info("args", args)
            if "token" not in args or "OMid" not in args:
                return PARAMS_MISS

            maid = token_to_usid(args.get("token"))
            if not maid:
                return TOKEN_ERROR

            order_main = todict(self.sorder.get_order_main_by_om_id(get_str(args, "OMid")))
            order_main.pop("USid")

            self._get_order_abo_by_order_main(order_main)
            log.info("order main", order_main)
            data = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            data["data"] = order_main
            return data
        except Exception as e:
            log.error("get order abo", e.message)
            return SYSTEM_ERROR

    def _get_order_abo_by_order_main(self, order_main):
        order_part_list = tolist(self.sorder.get_order_part_list_by_omid(order_main.get("OMid")))
        for order_part in order_part_list:
            order_part.update(self._get_product_into_order_abo(order_part.get("PBid")))

        order_main["order_abo"] = order_part_list
        order_main["OMcointype"] = cvs.conversion_PBunit.get(order_main.get("OMcointype"), "其他币种")
        order_main["OMstatus"] = cvs.conversion_OMstatus.get(order_main.get("OMstatus"), 0)
        order_main["OMtime"] = TimeManager.get_web_time_str(order_main.get("OMtime"))
        location = todict(self.sorder.get_location_by_loid(order_main.get("LOid")))
        if location.get("LOisedit") == 303:
            print(get_response("ERROR_MESSAGE_GET_LOCATION", "WORING_LOCATION"))
        order_main.update(location)
        order_main["CAid"] = order_main.pop("COid")

    def _get_product_into_order_abo(self, pbid):
        product = todict(self.sproduct.get_product_by_pbid(pbid))
        if not product:
            raise Exception("SYSTEM ERROR NO FIDN PBID")
        product.update(todict(self.sproduct.get_product_by_prid(product.get("PRid"))))
        product.update(self._get_brinfo(product.get("BRid")))
        product["PBunit"] = cvs.conversion_PBunit.get(product.get("PBunit", "其他币种"))
        product["PRbrand"] = cvs.conversion_PRbrand.get(product.get("PRbrand"), "其他")
        product["PRtype"] = cvs.conversion_PRtype.get(product.get("PRtype"))
        return product

    def _get_brinfo(self, brid):
        brinfo = {}
        while True:
            brand = todict(self.sproduct.get_brand_by_brid(brid))
            if not (brand.get("BRkey") and brand.get("BRvalue")):
                error = "the brand does not have BRkey or BRvalue. brand = {0}".format(brand)
                raise Exception(error)

            if brand.get("BRkey") in brinfo:
                raise Exception("the product has duplicate brand = {0}".format(brand))

            brinfo[brand.get("BRkey")] = brand.get("BRvalue")

            if brand.get("BRfromid") == "0":
                break
            brid = brand.get("BRfromid")

        return brinfo

    def update_order_main(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS

        maid = token_to_usid(args.get("token"))
        if not maid:
            return TOKEN_ERROR
        data = json.loads(request.data)
        log.info("data", data)
        if "OMstatus" not in data or "OMid" not in data:
            return PARAMS_MISS
        try:
            omstatus = cvs.conversion_OMstatus_reverse.get(get_str(data, "OMstatus"))
            update_result = self.sorder.update_order(get_str(data, "OMid"), {"OMstatus": omstatus})
            log.info("update_result", update_result)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_ORDER", "OK")
        except Exception as e:
            log.error("update order", e.message)
            return SYSTEM_ERROR

    def get_omfilter(self):
        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = [
            {
                "name": "订单号",
                "value": "",
                "key": "OMid"
            },
            {
                "name": "订单状态",
                "value": cvs.conversion_OMstatus_reverse.keys(),
                "key": "OMstatus"
            },
            {
                "name": "下单时间",
                "value": "",
                "key": "OMstartTime"
            },
            {
                "name": "下单时间",
                "value": "",
                "key": "OMendTime"
            },
            {
                "name": "物流方式",
                "value": ["顺丰速运"],
                "key": "OMlogisticsName"
            },
            {
                "name": "商品名称",
                "value": "",
                "key": "PRname"
            },
        ]
        return response

    def get_order_situation(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        from ManagerSystem.models.model import OrderMain
        days = int(args.get("days", 1))
        maid = token_to_usid(args.get("token"))
        prid_list = self.sproduct.get_product_by_maid(maid)
        pbid_list = []
        for pr in prid_list:
            pbid_list.extend([pb.PBid for pb in self.sproduct.get_pbid_by_prid(pr.PRid)])
        OMid_list = []
        for pbid in pbid_list:
            OMid_list.extend([op.OMid for op in self.sorder.get_order_part_list_by_pbid(pbid)])

        OMid_list = {}.fromkeys(OMid_list).keys()
        payed_count = 0
        paying_count = 0
        deliver_count = 0
        week_payed_count = 0
        week_paying_count = 0
        omprice = 0
        week_payed_list = []
        week_paying_list = []

        for omid in OMid_list:

            om = self.sorder.get_om_by_filter({OrderMain.OMid == omid})[0]
            if om.OMtime > TimeManager.get_forward_time(days=-days):
                if om.OMstatus >= 21:
                    payed_count += 1
                    omprice += om.OMprice
                elif om.OMstatus != 0:
                    paying_count += 1
                if om.OMstatus == 21:
                    deliver_count += 1
            if om.OMtime > TimeManager.get_forward_time(days=-7):
                if om.OMstatus >= 21:
                    week_payed_count += 1
                elif om.OMstatus != 0:
                    week_paying_count += 1

            for i in range(1, 8):
                if om.OMtime == TimeManager.get_forward_time(days=-i):
                    if om.OMstatus >= 21:
                        if len(week_payed_list) < i:
                            week_payed_list.append(1)
                        else:
                            week_payed_list[i - 1] += 1
                    elif om.OMstatus != 0:
                        if len(week_paying_list) < i:
                            week_paying_list.append(1)
                        else:
                            week_paying_list[i - 1] += 1
                else:
                    if len(week_payed_list) < i:
                        week_payed_list.append(0)
                    else:
                        week_payed_list[i - 1] += 0

                    if len(week_paying_list) < i:
                        week_paying_list.append(0)
                    else:
                        week_paying_list[i - 1] += 0

        # payed_filter = {
        #     OrderMain.OMtime< TimeManager.get_forward_time(days=-days),
        #     OrderMain.OMstatus >= 21,
        # }
        # payed_count = self.sorder.get_count_by_or_filter("model.OrderMain.OMid", payed_filter, set())
        # omlist = self.sorder.get_om_by_filter(payed_filter)
        # omprice = 0
        # for om in omlist:
        #     omprice += om.OMprice
        # paying_filter = {
        #     OrderMain.OMtime < TimeManager.get_forward_time(days=-days),
        #     OrderMain.OMstatus < 21,
        #     OrderMain.OMstatus != 0,
        # }
        # paying_count = self.sorder.get_count_by_or_filter("model.OrderMain.OMid", paying_filter, set())
        # deliver_filter = {
        #     OrderMain.OMstatus == 21,
        # }
        # deliver_count = self.sorder.get_count_by_or_filter("model.OrderMain.OMid", deliver_filter, set())
        # week_payed_filter = {
        #     OrderMain.OMtime < TimeManager.get_forward_time(days=-7),
        #     OrderMain.OMstatus >= 21
        #
        # }
        # week_payed_count = self.sorder.get_count_by_or_filter("model.OrderMain.OMid", week_payed_filter, set())
        # week_paying_filter = {
        #     OrderMain.OMtime < TimeManager.get_forward_time(days=-days),
        #     OrderMain.OMstatus < 21,
        #     OrderMain.OMstatus != 0,
        # }
        # week_paying_count = self.sorder.get_count_by_or_filter("model.OrderMain.OMid", week_paying_filter, set())
        # week_payed_list = []
        # week_paying_list = []
        # for i in range(1, 8):
        #     day_payed_filter = {
        #         OrderMain.OMtime < TimeManager.get_forward_time(days=-i),
        #         OrderMain.OMstatus >= 21
        #     }
        #     count = self.sorder.get_count_by_or_filter(day_payed_filter)
        #     week_payed_list.append(count)
        #     day_paying_filter = {
        #         OrderMain.OMtime < TimeManager.get_forward_time(days=-i),
        #         OrderMain.OMstatus < 21,
        #         OrderMain.OMstatus != 0,
        #     }
        #     count = self.sorder.get_count_by_or_filter(day_paying_filter)
        #     week_paying_list.append(count)
        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = {
            "payed_count": payed_count,
            "paying_count": paying_count,
            "deliver_count": deliver_count,
            "week_payed_count": week_payed_count,
            "week_paying_count": week_paying_count,
            "week_payed_list": week_payed_list,
            "week_paying_list": week_paying_list,
            "omprice": omprice,

        }
        return response


if __name__ == "__main__":
    co = COrder()
    # co.get_order_abo(OMid="1df44780-f5ed-43dd-bbd1-4fb245af5839")