# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.COrder import COrder
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log


class MSOrder(Resource):
    def __init__(self):
        self.corder = COrder()

    def get(self, order):
        log.info("get api", order)
        action = {
            "order_list": "self.corder.get_order_list()",
            "order_abo": "self.corder.get_order_abo()",
            "get_omfilter": "self.corder.get_omfilter()",
            "get_order_situation": "self.corder.get_order_situation()",
        }
        if order in action:
            return eval(action.get(order))

        return APIS_WRONG


    def post(self, order):
        log.info("get api", order)
        action = {
            "update_order_status": "self.corder.update_order_main()"
        }
        if order in action:
            return eval(action.get(order))
        return APIS_WRONG