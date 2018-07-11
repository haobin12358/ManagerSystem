# *- coding:utf-8 *-
import sys
import json
import uuid
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request

from service.SStocks import SStocks
from service.SProducts import SProducts
from common.MakeToken import token_to_usid
from globals import log
from common.ImportManager import get_response
from config.response import SYSTEM_ERROR, PARAMS_MISS
from common.ResultManager import todict, tolist


class CStocks():
    def __init__(self):
        self.sstocks = SStocks()
        self.sproduct = SProducts()
        self.stock_key_list = ["STname", "STamount", "STabo"]
        self.stock_product_key_list = ["STid", "PBid", "PBnumber"]

    def get_stock_all(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))

        try:
            if "PBid" not in args:
                prid_list = [product.PRid for product in self.sproduct.get_product_by_maid(maid)]
                log.info("prid list", prid_list)
                pbid_list = []
                for prid in prid_list:
                    pbid_list.extend([productbrand.PBid for productbrand in self.sproduct.get_productbrand_by_prid(prid)])
                log.info("pbid list", pbid_list)
                stocks_list = []
                for pbid in pbid_list:
                    stock_product_list = tolist(self.sstocks.get_stocks_by_PBid(pbid))
                    log.info("stock_product_list", stock_product_list)
                    for stock_product in stock_product_list:
                        stock = todict(self.sstocks.get_stock_by_stid(stock_product.get("STid")))
                        log.info("stock", stock)
                        stock_product.update(stock)

                    stocks_list.extend(stock_product_list)
            else :
                stocks_list = tolist(self.sstocks.get_stocks_by_PBid(args.get("PBid")))
                for stock_product in stocks_list:
                    stock = todict(self.sstocks.get_stock_by_stid(stock_product.get("STid")))
                    stock_product.update(stock)

            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = stocks_list
            return response
        except Exception as e:
            log.error("get error", e.message)
            return SYSTEM_ERROR

    def get_stock(self):
        args = request.args.to_dict()
        log.info("args", args)
        params_list = ["token", "STid"]
        for key in params_list:
            if key not in args:
                return PARAMS_MISS

        maid = token_to_usid(args.get("token"))
        prid_list = [product.PRid for product in self.sproduct.get_product_by_maid(maid)]
        pbid_list = []
        for prid in prid_list:
            pbid_list.extend([productbrand.PBid for productbrand in
                         self.sproduct.get_productbrand_by_prid(prid)])
        stocks_list = []
        for pbid in pbid_list:
            stocks_list.extend(tolist(self.sstocks.get_stocks_by_PBid(pbid)))
        if args.get("STid") not in stocks_list:
            return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
        stock = todict(self.sstocks.get_stock_by_stid(args.get("STid")))
        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = stock
        return response

    def add_stock(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)

        if "STname" not in data:
            return PARAMS_MISS
        stock = {"STid": str(uuid.uuid1())}
        for key in self.stock_key_list:
            if key in data:
                stock[key] = data.get(key)


        try:
            self.sstocks.add_model("Stocks", **stock)
        except Exception as e:
            log.error("add stock error", e.message)
            return SYSTEM_ERROR
        return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")

    def add_stock_product(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        sp = {"SPid": str(uuid.uuid1())}
        for key in self.stock_product_key_list:
            if key not in data:
                return PARAMS_MISS
            sp[key] = data.get(key)

        try:
            self.sstocks.add_model("StocksProducts", **sp)
            return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
        except Exception as e:
            log.error("add stock product error", e.message)
            return SYSTEM_ERROR

    def update_stock(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        stock = {}
        for key in self.stock_key_list:
            if key in data:
                stock[key] = data.get(key)
        stid = data.get("STid")
        try:
            update_result = self.sstocks.update_stock(stid, stock)
            log.info("update result", update_result)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("add stock error", e.message)
            return SYSTEM_ERROR

    def update_stock_product(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        if "SPid" not in data:
            return PARAMS_MISS
        spid = data.get("SPid")
        sp = {}
        for key in self.stock_product_key_list:
            if key not in data:
                return PARAMS_MISS
            sp[key] = data.get(key)

        try:
            log.info("sp", sp)
            update_result = self.sstocks.update_stock_product(spid, sp)
            log.info("update result", update_result)
            if not update_result:
                 return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("add stock product error", e.message)
            return SYSTEM_ERROR
