# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CStocks import CStocks
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log


class AStocks(Resource):
    def __init__(self):
        self.cstocks = CStocks()

    def get(self, stock):
        log.info("get api", stock)
        action = {
            "get_stock_all": "self.cstocks.get_stock_all()",
            "get_stock": "self.cstocks.get_stock()"
        }
        if stock in action:
            return eval(action.get(stock))

        return APIS_WRONG

    def post(self, stock):
        log.info("get api", stock)
        action = {
            "add_stock": "self.cstocks.add_stock()",
            "add_stock_product": "self.cstocks.add_stock_product()",
            "update_stock": "self.cstocks.update_stock()",
            "update_stock_product": "self.cstocks.update_stock_product()"
        }
        if stock in action:
            return eval(action.get(stock))
        return APIS_WRONG
