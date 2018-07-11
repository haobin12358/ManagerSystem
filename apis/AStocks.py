# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from control.CStocks import CStocks
from config.response import APIS_WRONG
from globals import log


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
