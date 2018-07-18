# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CCategory import CCategory
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log


class MSCategory(Resource):
    def __init__(self):
        self.ccategory = CCategory()

    def get(self, category):
        log.info("get api", category)
        action = {
            "get_first": "self.ccategory.get_first()",
            "get_child": "self.ccategory.get_child()",
            "get_categorybrands": "self.ccategory.get_categorybrands()"
        }
        if category in action:
            return eval(action.get(category))

        return APIS_WRONG


    def post(self, category):
        log.info("get api", category)
        action = {
            "add_category": "self.ccategory.add_category()"
        }
        if category in action:
            return eval(action.get(category))
        return APIS_WRONG