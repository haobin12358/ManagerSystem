# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CProducts import CProducts
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log


class MSProduct(Resource):
    def __init__(self):
        self.control_product = CProducts()



    def post(self, product):
        log.info("get api :", product)
        apis = {
            "release": "self.control_product.add_product()",
            "update_pro_info": "self.control_product.update_pro_info()",
            "update_product": "self.control_product.update_product_status()",
        }

        if product in apis:
            return eval(apis[product])

        return APIS_WRONG

    def get(self, product):
        log.info("get api: ", product)
        apis = {
            "get_abo": "self.control_product.get_info_by_id()",
            "get_all": "self.control_product.get_all()",
            "get_prid": "self.control_product.get_prid()"
        }
        if product in apis:
            return eval(apis[product])

        return APIS_WRONG