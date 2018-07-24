# *- coding:utf-8 *-
import sys
import json
import uuid
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request


from ManagerSystem.globals import log
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS
from ManagerSystem.common.ResultManager import todict, tolist
from ManagerSystem.service.SActive import SActive

class CActive():
    def __init__(self):
        self.sactive = SActive()

    def add_active(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        maid = token_to_usid(args.get("token"))


