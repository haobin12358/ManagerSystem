# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from control.CManager import CManager
from config.response import APIS_WRONG
from globals import log

class AManager(Resource):
    def __init__(self):
        self.cmanager = CManager()
        # self.log = LOG()

    def get(self, manager):
        log.info("get api", manager)
        action = {
            "get_manager": "self.cmanager.get_manager()",
        }
        if manager in action:
            return eval(action.get(manager))

        return APIS_WRONG


    def post(self, manager):
        log.info("get api", manager)
        action = {
            "apply": "self.cmanager.apply_manager()",
            "update_manager": "self.cmanager.update_manager()",
            "update_password": "self.cmanager.update_password()",
            "get_inforcode": "self.cmanager.get_inforcode()",
            "login": "self.cmanager.login()"
        }
        if manager in action:
            return eval(action.get(manager))
        return APIS_WRONG