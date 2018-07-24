# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid
import json
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.ResultManager import todict, tolist
from ManagerSystem.common.TimeManagert import TimeManager
from ManagerSystem.config.conversion import conversion_PBunit, \
    conversion_PBunit_reverse, conversion_PRbrand, conversion_PRbrand_reverse, \
    conversion_PRtype, conversion_PRtype_reverse, conversion_PBstatus_reverse, conversion_PBstatus

from ManagerSystem.config.imageconfig import PRSWINGIMAGE, PRABOIMAGE
from ManagerSystem.globals import log


class CProducts():
    def __init__(self):
        from ManagerSystem.service.SProducts import SProducts
        from ManagerSystem.service.SStocks import SStocks
        self.sproduct = SProducts()
        self.stock = SStocks()

    def get_info_by_id(self):
        args = request.args.to_dict()
        log.info("args", args)
        params_key_list = ["PRid", "token"]
        for param_key in params_key_list:
            if param_key not in args:
                return PARAMS_MISS
        PRid = args["PRid"]
        maid = args.get("token")
        product = self.sproduct.get_product_by_prid(PRid)
        log.info("product", product)
        if not product:
            return SYSTEM_ERROR
        product_price = [9999999, -1]
        product_volue = 0
        product_price_list =[
            pro.PBprice for pro in self.sproduct.get_pbprice_by_prid(PRid)]
        log.info("product_price_list", product_price_list)
        if not product_price_list:
            return SYSTEM_ERROR
        for row in product_price_list:
            if row < product_price[0]:
                product_price[0] = row
            if row > product_price[1]:
                product_price[1] = row
        prprice = "-".join(product_price) \
            if product_price[0] != product_price[1] \
            else product_price[0]
        product_volue_list = [pro.PBsalesvolume for pro in
                              self.sproduct.get_pbvolume_by_prid(PRid)]
        log.info('product_volue_list', product_volue_list)
        if not product_volue_list:
            return SYSTEM_ERROR
        for row in product_volue_list:
            product_volue = product_volue + row
        product_info = {}
        product_info["PRid"] = PRid
        product_info["PRprice"] = prprice
        product_info["PRsalevolume"] = product_volue
        product_info["PRname"] = product.PRname
        product_info["PRvideo"] = product.PRvideo
        product_info["PRinfo"] = product.PRinfo
        product_info["PRvideostart"] = product.PRvideostart
        product_info["PRimage"] = json.loads(product.PRimage)
        product_info["PRaboimage"] = json.loads(product.PRaboimage)
        PRbrand = product.PRbrand
        PRtype = product.PRtype
        product_info["PRbrand"] = json.loads(PRbrand)
        product_info["PRtype"] = conversion_PRtype.get(PRtype)
        product_info["PBimage"] = list(PRSWINGIMAGE.get(PRid))
        product_info["PRquality"] = {}
        BRid = [br.BRid for br in self.sproduct.get_brid_by_prid(PRid)]
        log.info("BRid", BRid)
        for brid in BRid:
            while brid != "0":
                brand = self.sproduct.get_brand_by_brid(brid)
                log.info("brand", brand)
                brid, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if BRkey in product_info["PRquality"].keys():
                    if BRvalue not in product_info["PRquality"][BRkey]["choice"]:
                        product_info["PRquality"][BRkey]["choice"].append(BRvalue)
                else:
                    product_info["PRquality"].keys().append(BRkey)
                    product_info["PRquality"][BRkey] = {}
                    product_info["PRquality"][BRkey]["name"] = BRkey
                    product_info["PRquality"][BRkey]["choice"] = [BRvalue]
        response_of_product = get_response("SUCCESS_MESSAGE_GET_PRODUCT", "OK")
        response_of_product["data"] = product_info
        return response_of_product

    def get_all(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args or "page_size" not in args or "page_num" not in args:
            return PARAMS_MISS
        page_size = int(args.get("page_size"))
        page_num = int(args.get("page_num"))
        maid = token_to_usid(args.get("token"))
        from ManagerSystem.models.model import Products
        pro_fillter = {Products.MAid == maid}
        sub_filter = set()
        if args.get("product_filter"):
            product_filter = get_str(args, "product_filter")
            sub_filter = {
                Products.PRname.like("%{0}%".format(product_filter)),
                Products.PRinfo.like("%{0}%".format(product_filter))
            }

        pn, count = self.check_page_value(page_num, page_size, "model.Products.PRid", pro_fillter, sub_filter)
        start_num = (pn - 1) * page_size
        PRid_list = [products.PRid for products in self.sproduct.get_all_prid(start_num, page_size, pro_fillter, sub_filter)]
        log.info("PRid list", PRid_list)
        pbstatus = get_str(args, "PBstatus")
        # todo 增加遍历输出所有图片
        htv = float(args.get("htv", 0.48))
        from ManagerSystem.common.Gethdp import get_hdp
        hdp = get_hdp(htv)
        product_infos = []
        for PRid in PRid_list:
            product = todict(self.sproduct.get_product_by_prid(PRid))
            log.info("product", product)
            if not product:
                return SYSTEM_ERROR

            product["PRid"] = PRid
            product["PRimage"] = json.loads(product.get("PRimage"))
            product["PRaboimage"] = json.loads(product.get("PRaboimage"))
            product["PRtype"] = conversion_PRtype.get(get_str(product, "PRtype"))
            product["PRtime"] = TimeManager.get_web_time_str(product.get("PRtime"))
            product["PRbrand"] = json.loads(product.get("PRbrand"))
            log.info("pbstatus", pbstatus)
            saleamount = 0
            stockamout = 0
            if not pbstatus:
                pb_list = tolist(self.sproduct.get_pball_by_prid(PRid))
            else:
                pb_list = tolist(self.sproduct.get_pball_by_prid_pbstatus(PRid, conversion_PBstatus_reverse.get(pbstatus)))

            PRstatus = ""
            for pb in pb_list:
                saleamount += int(pb.get("PBsalesvolume"))
                PRstatus = conversion_PBstatus.get(pb.get("PBstatus"))
                stockamout += sum([int(st.get("PBnumber", 0)) for st in tolist(self.stock.get_stocks_by_PBid(pb.get("PBid")))])
                pb.update(product)

            if not PRstatus:
                count -= 1
                continue

            # product_infos.extend(pb_list)
            product["PRsalesvolume"] = saleamount
            product["PRstock"] = stockamout
            product["PRstatus"] = PRstatus
            product_infos.append(product)

        response_of_product = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response_of_product["data"] = {
            "count": count,
            "page_num": page_num,
            "page_size": page_size,
            "products": product_infos
        }
        log.info("response", response_of_product)
        return response_of_product

    def check_page_value(self, page_num, page_size, model_name, and_params, or_params):
        count = self.sproduct.get_count_by_or_filter(model_name, and_params, or_params)
        if page_size * page_num > count:
            page_num = count / page_size
        page_num = page_num if page_num > 0 else 1
        return page_num, count

    def get_control_brand_by_prid(self):
        args = request.args.to_dict()
        log.info('args', args)
        data = request.data
        data = json.loads(data)
        log.info("data", data)
        if "token" not in args or "PRid" not in args:
            return PARAMS_MISS
        if data == {}:
            return PARAMS_MISS
        BRid = self.sproduct.get_brid_by_prid(args["PRid"])
        log.info("BRid", BRid)
        if not BRid:
            return SYSTEM_ERROR
        key_list = []
        brid = BRid[0]
        while brid != "0":
            Brand = self.sproduct.get_brand_by_brid(brid)
            brid, BRkey, BRvalue = Brand.BRfromid, Brand.BRkey, Brand.BRvalue
            key_list.append(BRkey)
        log.info("key list", key_list)
        BRid_list = self.sproduct.get_brid_by_prid(args["PRid"])
        brid_list = self.sproduct.get_brid_by_prid(args["PRid"])
        log.info("BRid list", BRid_list)
        i = len(BRid_list)
        while i > 0:
            raw = BRid_list[i - 1]
            row = BRid_list[i - 1]
            log.info("row", row)
            while row != "0":
                brand = self.sproduct.get_brand_by_brid(row)
                log.info("brand", brand)
                row, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if BRkey in data.keys() and data[BRkey] != BRvalue:
                    BRid_list.remove(raw)
                    break
            i = i - 1
        log.info("BRid list removed", BRid_list)
        back_data = {}
        for key in key_list:
            back_data.keys().append(key)
            back_data[key] = []
            for BRid in BRid_list:
                brand = self.sproduct.get_brand_by_brid(BRid)
                BRkey, BRvalue = brand.BRkey, brand.BRvalue
                if BRkey == key and BRvalue not in back_data[key]:
                    back_data[key].append(BRvalue)
                else:
                    while BRid != "0":
                        brand_parent = self.sproduct.get_brand_by_brid(BRid)
                        BRid, BRkey, BRvalue = brand_parent.BRfromid, brand_parent.BRkey, brand_parent.BRvalue
                        if BRvalue not in back_data[key] and BRkey == key:
                            back_data[key].append(BRvalue)

        key_list_control = data.keys()
        i = len(key_list_control)
        j = 0
        control = []
        while i > 0:
            control.append(self.get_m_by_n(key_list_control[i - 1], key_list_control, data, brid_list, i - 1))
            back_data[key_list_control[i - 1]] = control[j]
            #print key_list_control[i - 1]
            i = i - 1
            j = j + 1

        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = back_data
        return response

    def get_pbid_by_all_brand(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "token" not in args or "PRid" not in args:
            return PARAMS_MISS
        if data == {}:
            return PARAMS_MISS
        BRid = self.sproduct.get_brid_by_prid(args["PRid"])
        print "=================BRid================="
        print BRid
        print "=================BRid================="
        if not BRid:
            return SYSTEM_ERROR
        key_list = []
        brid = BRid[0]
        while brid != "0":
            Brand = self.sproduct.get_brand_by_brid(brid)
            brid, BRkey, BRvalue = Brand.BRfromid, Brand.BRkey, Brand.BRvalue
            key_list.append(BRkey)
        print "=================key_list================="
        print key_list
        print "=================key_list================="
        BRid_list = self.sproduct.get_brid_by_key_value(key_list[0], data[key_list[0]])
        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        i = len(BRid_list)
        while i > 0:
            row = BRid_list[i - 1]
            raw = row
            while row != "0":
                brand = self.sproduct.get_brand_by_brid(row)
                print "=================brand================="
                print brand
                print "=================brand================="
                row, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if data[BRkey] != BRvalue:
                    BRid_list.remove(raw)
            i = i - 1

        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        if len(BRid_list) != 1:
            return SYSTEM_ERROR
        BRid = BRid_list[0]
        pball = self.sproduct.get_pball_by_brid(BRid)
        print "=================pball================="
        print pball
        print "=================pball================="
        data = {}
        data["PBid"] = pball.PBid
        data["PBimage"] = pball.PBimage
        PBunit = pball.PBunit
        if PBunit == 401:
            data["PBunit"] = "$"
        elif PBunit == 402:
            data["PBunit"] = "￥"
        elif PBunit == 403:
            data["PBunit"] = "欧元"
        elif PBunit == 404:
            data["PBunit"] = "英镑"
        else:
            data["PBunit"] = "其他币种"
        data["PBprice"] = pball.PBprice
        data["PBsalesvolume"] = pball.PBsalesvolume
        data["PBscore"] = pball.PBscore

        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = data
        return response


    def get_m_by_n(self, key, key_list, brands, brid_list, index):
        # 首先移除需要判断的key
        #key_list.remove(key)
        key_list[index] = 0
        len_brid_list = len(brid_list)
        # 倒序循环，移除不合适的，放跳位
        while len_brid_list > 0:
            # 备份一个brid，用于remove
            raw = brid_list[len_brid_list - 1]
            row = brid_list[len_brid_list - 1]
            log.info("raw", raw)
            # 循环，直至找到根节点的brid
            while row != "0":
                # 获取父节点和当前节点的key、value
                brand = self.sproduct.get_brand_by_brid(row)
                print "=================brand================="
                print brand
                print "=================brand================="
                # 替代当前值
                row, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                # 判断，如果存在一个key对应的value和实际brands中key对应的value不同，移除当前的brid
                if BRkey in key_list and brands[BRkey] != BRvalue:
                    brid_list.remove(raw)
                    print "=================BRid_list_remove================="
                    print brid_list
                    print "=================BRid_list_remove================="
            len_brid_list = len_brid_list - 1

        # 设置最后要返回的可选值
        control_key = []

        # 利用已经筛选好的brid_list进行处理
        for BRid in brid_list:
            # 获取key和value
            brand = self.sproduct.get_brand_by_brid(BRid)
            BRkey, BRvalue = brand.BRkey, brand.BRvalue
            # 如果key属于设定的key且value不存在于要返回的list中，那么将value添加进该list
            if BRkey == key and BRvalue not in control_key:
                control_key.append(BRvalue)
            # 否则循环寻找父节点，重复判断逻辑，直到找到对应的key
            else:
                while BRid != "0":
                    brand_parent = self.sproduct.get_brand_by_brid(BRid)
                    BRid, BRkey, BRvalue = brand_parent.BRfromid, brand_parent.BRkey, brand_parent.BRvalue
                    if BRvalue not in control_key and BRkey == key:
                        control_key.append(BRvalue)
        key_list[index] = key

        return control_key


    def add_product(self):
        args = request.args.to_dict()
        log.info("args", args)
        data = json.loads(request.data)
        log.info("data", data)
        if "token" not in args:
            return PARAMS_MISS
        # if "PRid" not in data:
        #     return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except Exception as e:
            return TOKEN_ERROR
        # 库存


        prid = data.get("PRid")
        # todo 拆分更新
        prid = prid if prid else str(uuid.uuid1())
        try:
            if not self.add_brands(prid, data.get("brands"), data.get("brands_key")):
                return get_response("ERROR_MESSAGE_WRONG_BRNADS", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_BRANDS")
            product = {
                "PRid": prid,
                "PRname": data.get("PRname", ""),
                "PRvideo": data.get("PRvideo", ""),
                "PRimage": json.dumps(data.get("PRimage", [])),
                "PRaboimage": json.dumps(data.get("PRaboimage", "")),
                "PRinfo": data.get("PRinfo", ""),
                "PRvideostart": data.get("PRvideostart", ""),
                "PRfranking": data.get("PRfranking", 0.0),
                "MAid": maid,
                "PRtype": conversion_PRtype_reverse.get(get_str(data, "PRtype", "自营")),
                "PRbrand": json.dumps(data.get("PRbrand")),
                "PRtime": TimeManager.get_db_time_str(),
                "CTid": data.get("CTid")
            }

            self.sproduct.add_model("Products", **product)
            self.add_approval(maid, prid)
            return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
        except Exception as e:
            log.error("add pruduct error", e.message)
            return SYSTEM_ERROR


    def update_product_status(self):
        args = request.args.to_dict()
        log.info("args", args)
        maid = token_to_usid(args.get("token"))
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data, encoding="utf8")
        log.info("data", data)
        if "PRstatus" not in data or "PRid" not in data:
            return PARAMS_MISS
        prstatus = get_str(data, "PRstatus")
        pridlist = data.get("PRid")

        self.on_or_off_shelves(pridlist, conversion_PBstatus_reverse.get(prstatus), maid)
        return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")

    def on_or_off_shelves(self, prid_list, PBstatus, maid):
        for prid in prid_list:
            pbid_list = [pb.PBid for pb in self.sproduct.get_pbid_by_prid(prid)]
            for pbid in pbid_list:
                pb = {
                    "PBstatus": PBstatus
                }
                # todo 增加审批流

                update_result =self.sproduct.update_pb(pbid, pb)
                log.info("update result", update_result)
                if not update_result:
                    raise Exception("update pb failed")

            if PBstatus == 205:
                self.add_approval(maid, prid)

    def add_approval(self, maid, prid):
        from ManagerSystem.service.SApproval import SApproval
        sapproval = SApproval()
        receive_list = sapproval.get_permission_by_petype_pesublevel(304, 1)
        apname = "商品发布审批" + str(uuid.uuid1())
        for pe in receive_list:
            approval = {
                "APid": str(uuid.uuid1()),
                "APname": apname,
                "APstart": maid,
                "APreceive": pe.MAid,
                "PEtype": 304,
                "APcontent": prid,
                "APremark": "",
                "APstatus": 443,
                "APtime": TimeManager.get_db_time_str()
            }
            sapproval.add_model("Approval", **approval)

    def update_pro_info(self):
        args = request.args.to_dict()
        log.info("args", args)
        data = json.loads(request.data, encoding="utf8")
        log.info("data", data)
        if "token" not in args:
            return PARAMS_MISS

        if  "PRid" not in data:
            return PARAMS_MISS
        prid = data.get("PRid")




    def add_brands(self, prid, brands, brands_key):
        if not isinstance(brands, list):
            return False

        for i in brands:
            brid = ""
            brand_values = i.get("BRands")
            if len(brand_values) != len(brands_key):
                return False
            BRfromid = 0
            for index, key in enumerate(brands_key):
                brandid = [br.BRid for br in self.sproduct.get_brid_by_key_value(key, brand_values[index])]
                if brandid:
                    if not BRfromid:
                        if len(brandid) != 1:
                            return False
                        BRfromid = brandid[0]
                    else:
                        BRfromid_tmp = [brfrom for brfrom in brandid if self.sproduct.get_brfromid_by_brid(brfrom) == BRfromid]
                        if BRfromid_tmp:
                            BRfromid = BRfromid_tmp[0]
                        else:
                            brid = str(uuid.uuid1())

                            self.sproduct.add_model("Brands", **{
                                "BRid": brid,
                                "BRfromid": BRfromid,
                                "BRvalue": brand_values[index],
                                "BRkey": key
                            })
                            BRfromid = brid
                else:
                    brid = str(uuid.uuid1())

                    self.sproduct.add_model("Brands", **{
                        "BRid": brid,
                        "BRfromid": BRfromid,
                        "BRvalue": brand_values[index],
                        "BRkey": key
                    })
                    BRfromid = brid

            if not brid:
                brid = BRfromid
            from ManagerSystem.config.conversion import conversion_PBstatus_reverse
            stid = str(uuid.uuid1())
            pbid = str(uuid.uuid1())

            self.stock.add_model("Stocks", STid=stid, STname="库存"+prid, STamout=10 * 10 * 10 * 10 * 10 * 10)
            self.stock.add_model("StocksProducts", SPid=str(uuid.uuid1()), STid=stid, PBid=pbid, PBnumber=i.get("PBnumber"))
            self.sproduct.add_model("ProductsBrands", **{
                "PBid": pbid,
                "PRid": prid,
                "BRid": brid,
                "PBprice": i.get("PBprice"),
                "PBunit": conversion_PBunit_reverse.get(get_str(i, "PBunit", "$")),
                "PBimage": i.get("PBimage"),
                "PBstatus": conversion_PBstatus_reverse.get(get_str(i, "PBstatus", "在售状态")),
                "PBsalesvolume": 0,
                "PBscore": 0,
            })

        return True
