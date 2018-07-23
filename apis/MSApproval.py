# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CApproval import CApproval
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log

class MSApproval(Resource):
    def __init__(self):
        self.capproval = CApproval()
        # self.log = LOG()

    def get(self, approval):
        log.info("get api", approval)
        action = {
            "get_approval": "self.capproval.get_approval()",
        }
        if approval in action:
            return eval(action.get(approval))

        return APIS_WRONG


    def post(self, approval):
        log.info("get api", approval)
        action = {
            "add_approval": "self.capproval.add_approval()",
            "update_approval": "self.capproval.update_approval()",
            "add_permission": "self.capproval.add_permission()",
            "update_permission": "self.capproval.update_permission()",
        }
        if approval in action:
            return eval(action.get(approval))
        return APIS_WRONG