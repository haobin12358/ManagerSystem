# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from service.SManager import SManager
from common.MakeToken import  usid_to_token, token_to_usid
from common.LogManager import LOG
from common.TimeManagert import TimeManager
from common.ImportManager import get_response
from config.response import SYSTEM_ERROR, PARAMS_MISS
from config.conversion import conversion_MAidentity_reverse, conversion_MAidentity


class CManager():
    def __init__(self):
        self.smanager = SManager()
        self.title = "=========={0}==========="

    def apply_manager(self):
        data = json.loads(request.data)
        LOG.info("data", data)
        param_keys = ["MAtelphone"]
        for params in param_keys:
            if params not in data:
                return PARAMS_MISS
        manager_key = [
            "MAname", "MAtelphone", "MAemail", "MAidentity",
            "MApassword", "MAstatus", "MAcreatTime", "MAendTime",
            "MAidNumber", "MAidImageFront", "MAidImageReverse",
            "MAbusinessLicense", "MAcredit"
        ]
        manager = {}
        for key in manager_key:
            if key in data:
                manager[key] = data.get(key)
        import uuid
        MAid = uuid.uuid1()
        manager["MAid"] = MAid
        maname = "商家{0}".format(data.get("MAtelphone")) if not data.get("MAname") else data.get("MAname")
        manager["MAname"] = maname
        import random
        import string
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        manager["MApassword"] = ran_str
        manager["MAidentity"] = conversion_MAidentity_reverse.get(data.get("MAidentity", "卖家"))
        manager["MAcreatTime"] = TimeManager.get_db_time_str()
        manager["MAendTime"] = TimeManager.get_db_time_str(data.get("MAendTime"))

        try:
            self.smanager.add_model("Manager", **manager)
        except Exception as e:
            LOG.error("add manager error", e.message)
            return SYSTEM_ERROR
        response = get_response("SUCCESS_MESSAGE_REGISTER", "OK")
        response["data"] = {
            "MAname": maname,
            "MApassword": ran_str
        }
        return response

    def update_password(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        LOG.info("args", args)
        maid = token_to_usid(args.get("token"))
        data = json.loads(request.data)
        LOG.info("data", data)
        params_key = ["MApasswordNew", "MApasswordRepeat", "MApasswordOld"]
        for key in params_key:
            if key not in data:
                return PARAMS_MISS

        new_pwd = data.get("MApasswordNew")
        repeat_pwd = data.get("MApasswordRepeat")
        old_pwd = data.get("MApasswordOld")
        if new_pwd and repeat_pwd and new_pwd != repeat_pwd:
            return get_response("ERROR_MESSAGE_WRONG_PARAMS", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_PARAMS")
        try:
            password = self.smanager.get_manager_by_maid(maid).MApassword
            LOG.info("password", password)
            if password != old_pwd:
                return get_response("ERROR_MESSAGE_WRONG_PASSWORD", "MANAGERSYSTEMERROR", "ERROR_WRONG_PASSWORD")
        except Exception as e:
            LOG.error("DBERROR", e.message)
            return SYSTEM_ERROR

        try:
            result = self.smanager.update_manager(maid, {"MApassword": new_pwd})
            LOG.info("update result", result)
            if result == 1 :
                return get_response("SUCCESS_MESSAGE_UPDATE_PASSWORD", "OK")
        except Exception as e:
            LOG.error("DBERROR", e.message)
        return SYSTEM_ERROR

    def login(self):
        data = json.loads(request.data)
        LOG.info("data", data)
        param_keys = ["MAname", "MApassword"]
        for key in param_keys:
            if key not in data:
                return PARAMS_MISS
        name = data.get("MAname")
        password = data.get("MApassword")

        if not name or not password:
            return get_response("ERROR_MESSAGE_WRONG_PARAMS", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_PARAMS")

        try:
            manager = self.smanager.get_manager_by_maname_mapassword(name, password)
            maid = manager.MAid
            if not maid:
                return get_response("ERROR_MESSAGE_WRONG_PASSWORD", "MANAGERSYSTEMERROR", "ERROR_WRONG_PASSWORD")
            response = get_response("SUCCESS_MESSAGE_LOGIN", "OK")
            response["data"] = {"token": usid_to_token(maid)}
            return response
        except Exception as e:
            LOG.error("DBERROR", e.message)
            return SYSTEM_ERROR

