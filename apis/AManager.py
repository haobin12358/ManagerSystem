# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CManager import CManager
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log

class AManager(Resource):
    def __init__(self):
        self.cmanager = CManager()
        # self.log = LOG()

    def get(self, manager):
        log.info("get api", manager)
        action = {
            "get_manager": "self.cmanager.get_manager()",
            "get_managers": "self.cmanager.get_managers()",
            "get_users": "self.cmanager.get_users()",
        }
        if manager in action:
            return eval(action.get(manager))

        return APIS_WRONG


    def post(self, manager):
        log.info("get api", manager)
        action = {
            "apply": "self.cmanager.apply_manager()",
            "update_manager": "self.cmanager.update_manager()",
            "update_user": "self.cmanager.update_password()",
            "get_inforcode": "self.cmanager.get_inforcode()",
            "login": "self.cmanager.login()",
            "forget_password": "self.cmanager.forget_password()"
        }
        if manager in action:
            return eval(action.get(manager))
        return APIS_WRONG