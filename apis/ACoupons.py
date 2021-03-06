# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CActive import CActive
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log


class MSCoupons(Resource):
    def __init__(self):
        self.cactive = CActive()

    def get(self, card):
        log.info("get api", card)
        action = {
            "get_all": "self.cactive.get_active()",
            "get_situation": "self.cactive.get_situation()",
            "get_acabo": "self.cactive.get_acabo()",
        }
        if card in action:
            return eval(action.get(card))

        return APIS_WRONG

    def post(self, card):
        log.info("get api", card)
        action = {
            "create": "self.cactive.add_active()",
            "update_active_status": "self.cactive.update_active_status()"
        }
        if card in action:
            return eval(action.get(card))
        return APIS_WRONG