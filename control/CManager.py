# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

import json
import uuid
from flask import request
from ManagerSystem.service.SManager import SManager
from ManagerSystem.service.SInterface import SInterface
from ManagerSystem.common.MakeToken import usid_to_token, token_to_usid
from ManagerSystem.globals import log
from ManagerSystem.common.TimeManagert import TimeManager
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS
from ManagerSystem.config.conversion import conversion_MAidentity_reverse, conversion_MAidentity,\
    conversion_MAstatus, conversion_MAstatus_resverse
from ManagerSystem.common.ResultManager import todict, tolist



class CManager():
    def __init__(self):
        self.smanager = SManager()
        self.sinterface = SInterface()

    def add_manager(self):
        data = json.loads(request.data)
        log.info("data", data)
        manager_key = [
            "MAtelphone", "MAemail", "MAname"
        ]
        manager = {}
        for key in manager_key:
            if key in data:
                manager[key] = data.get(key)
        maid = str(uuid.uuid1())
        manager["MAid"] = maid
        manager["MAname"] = get_str(data, "MAname")
        manager["MAtelphone"] = get_str(data, "MAtelphone")
        # todo 创建管理员

    def update_manager(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        log.info("args", args)
        maid = token_to_usid(args.get("token"))
        data = json.loads(request.data)
        log.info("data", data)



    def apply_manager(self):
        data = json.loads(request.data)
        log.info("data", data)
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

        MAid = str(uuid.uuid1())
        manager["MAid"] = MAid
        maname = "商家{0}".format(data.get("MAtelphone")) if not data.get("MAname") else data.get("MAname")
        manager["MAname"] = maname

        manager["MApassword"] = self.create_password()
        manager["MAidentity"] = conversion_MAidentity_reverse.get(data.get("MAidentity", "卖家"))
        manager["MAcreatTime"] = TimeManager.get_db_time_str()
        manager["MAendTime"] = TimeManager.get_db_time_str(data.get("MAendTime"))
        manager["MAstatus"] = conversion_MAstatus_resverse.get(data.get("MAstatus", "可用"))

        try:
            self.smanager.add_model("Manager", **manager)
        except Exception as e:
            log.error("add manager error", e.message)
            return SYSTEM_ERROR
        response = get_response("SUCCESS_MESSAGE_REGISTER", "OK")
        response["data"] = {
            "MAname": maname,
            "MApassword": manager["MApassword"]
        }
        return response

    def create_password(self):
        import random
        import string
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))

    def update_password(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        log.info("args", args)
        maid = token_to_usid(args.get("token"))
        data = json.loads(request.data)
        log.info("data", data)
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
            log.info("password", password)
            if password != old_pwd:
                return get_response("ERROR_MESSAGE_WRONG_PASSWORD", "MANAGERSYSTEMERROR", "ERROR_WRONG_PASSWORD")
        except Exception as e:
            log.error("DBERROR", e.message)
            return SYSTEM_ERROR

        try:
            result = self.smanager.update_manager(maid, {"MApassword": new_pwd})
            log.info("update result", result)
            if result == 1 :
                return get_response("SUCCESS_MESSAGE_UPDATE_PASSWORD", "OK")
        except Exception as e:
            log.error("UPDATEERROR", e.message)
        return SYSTEM_ERROR

    def login(self):
        data = json.loads(request.data)
        log.info("data", data)
        param_keys = ["MAname", "MApassword"]
        for key in param_keys:
            if key not in data:
                return PARAMS_MISS
        name = get_str(data, "MAname")
        password = data.get("MApassword")

        if not name or not password:
            return get_response("ERROR_MESSAGE_WRONG_PARAMS", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_PARAMS")

        try:
            manager = self.smanager.get_manager_by_maname_mapassword(name, password)

            if not manager:
                return get_response("ERROR_MESSAGE_WRONG_PASSWORD", "MANAGERSYSTEMERROR", "ERROR_WRONG_PASSWORD")

            maid = manager.MAid
            self.smanager.update_manager(maid, {"MAloginTime": TimeManager.get_db_time_str()})
            response = get_response("SUCCESS_MESSAGE_LOGIN", "OK")
            response["data"] = {
                "side": self.get_interface(maid),
                "token": usid_to_token(maid),
                "MAidentity": conversion_MAidentity.get(manager.MAidentity)}
            return response
        except Exception as e:
            log.error("LOGINERROR", e.message)
            return SYSTEM_ERROR

    def update_manager(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)

        if "MAidentity" not in data or "MAstatus" not in data:
            return PARAMS_MISS
        manager = {
            "MAcreatTime": TimeManager.get_db_time_str()
        }
        if data.get("MAidentity"):
            manager["MAidentity"] = conversion_MAidentity_reverse.get(data.get("MAidentity", "卖家"))
        if data.get("MAstatus"):
            manager["MAstatus"] = conversion_MAstatus_resverse.get(data.get("MAstatus"), "可用")

        maid = token_to_usid(args.get("token"))
        try:
            self.smanager.update_manager(maid, manager)
            return get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        except Exception as e:
            log.error("UPDATEERROR", e.message)
            return SYSTEM_ERROR

    def get_manager(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))
        try:
            manager = todict(self.smanager.get_manager_by_maid(maid))
            manager["MAstatus"] = conversion_MAstatus.get(manager.get("MAstatus"))
            manager["MAidentity"] = conversion_MAidentity.get(manager.get("MAidentity"))
            return manager
        except Exception as e:
            log.error("ERROR", e.message)
            return SYSTEM_ERROR

    def get_inforcode(self):
        data = json.loads(request.data)
        log.info("data", data)
        if "MAtelphone" not in data:
            return PARAMS_MISS
        Utel = data["MAtelphone"]
        # 拼接验证码字符串（6位）
        code = ""
        while len(code) < 6:
            import random
            item = random.randint(1, 9)
            code = code + str(item)

        # 获取当前时间，与上一次获取的时间进行比较，小于60秒的获取直接报错
        import datetime
        from ManagerSystem.common.TimeManagert import format_for_db
        
        time_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(time_time, format_for_db)

        """
        utel_list = self.smanager.get_user_by_utel(Utel)
        print(self.title.format("utel_list"))
        print(utel_list)
        print(self.title.format("utel_list"))
        if utel_list:
            return get_response("ERROR_MESSAGE_REPEAT_TELPHONE", "MANAGERSYSTEMERROR", "ERROR_CODE_REPEAT_TELPHONE")
            """
        # 根据电话号码获取时间
        time_up = self.smanager.get_uptime_by_utel(Utel)
        log.info(time_up)
        if time_up:
            time_up_time = datetime.datetime.strptime(time_up.ICtime, format_for_db)
            delta = time_time - time_up_time
            if delta.seconds < 60:
                return get_response("ERROR_MESSAGE_GET_CODE_FAST", "MANAGERSYSTEMERROR", "ERROR_CODE_GET_CODE_FAST")

        inforcode = {
            "ICid": str(uuid.uuid1()),
            "ICtelphone": Utel,
            "ICcode": code,
            "ICtime": time_str
        }
        new_inforcode = self.smanager.add_model("IdentifyingCode", **inforcode)

        log.info("new inforcode", new_inforcode)

        if not new_inforcode:
            return SYSTEM_ERROR
        from ManagerSystem.config.Inforcode import SignName, TemplateCode
        from ManagerSystem.common.Inforsend import send_sms
        params = '{\"code\":\"' + code + '\",\"product\":\"etech\"}'

        # params = u'{"name":"wqb","code":"12345678","address":"bz","phone":"13000000000"}'
        __business_id = uuid.uuid1()
        response_send_message = send_sms(__business_id, Utel, SignName, TemplateCode, params)

        response_send_message = json.loads(response_send_message)
        log.info("response_send_message", response_send_message)

        status = 200 if response_send_message["Code"] == "OK" else 405
        response_ok = {}
        response_ok["status"] = status
        response_ok["messages"] = response_send_message["Message"]

        return response_ok

    def forget_password(self):
        data = json.loads(request.data)
        log.info("data", data)
        params_key_list = ["MApasswordnew", "MApasswordnewrepeat", "MAtelphone", "MAcode"]
        for key in params_key_list:
            if key not in data:
                return PARAMS_MISS

        Utel = data["MAtelphone"]
        try:
            manager = self.smanager.get_manager_by_matelphone(Utel)
            log.info("manager", manager)
            if not manager:
                return get_response("ERROR_MESSAGE_NONE_TELPHONE", "MANAGERSYSTEMERROR", "ERROR_CODE_NONE_TELPHONE")

            code_in_db = self.smanager.get_code_by_utel(Utel)

            if not code_in_db:
                return get_response("ERROR_MESSAGE_WRONG_TELCODE", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_TELCODE")
            if code_in_db.ICcode != data["MAcode"]:
                return get_response("ERROR_MESSAGE_WRONG_TELCODE", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_TELCODE")

            if data["MApasswordnew"] != data["MApasswordnewrepeat"]:
                return get_response("ERROR_MESSAGE_WRONG_REPEAT_PASSWORD", "MANAGERSYSTEMERROR", "ERROR_CODE_WRONG_REPEAT_PASSWORD")

            users = {}
            Upwd = data["MApasswordnew"]
            users["MApassword"] = Upwd
            update_info = self.smanager.update_users_by_matel(Utel, users)
            log.info("update info", update_info)
            if not update_info:
                return SYSTEM_ERROR

            return get_response("SUCCESS_MESSAGE_UPDATE_PASSWORD", "OK")
        except Exception as e:
            log.error("forget pwd error", e.message)
            return SYSTEM_ERROR

    def get_interface(self, maid):
        mnid_list = [mm.MNid for mm in self.sinterface.get_mnid_by_maid(maid)]
        menu_dict = {}
        for mnid in mnid_list:
            menu = todict(self.sinterface.get_menu_by_mnid(mnid))
            parentid = menu.get("MNparent")
            while parentid != "0":
                if parentid in menu_dict:
                    menu_dict[parentid].append(menu)
                else:
                    menu_dict[parentid] = [menu]
                menu = todict(self.sinterface.get_menu_by_mnid(parentid))
                if not menu:
                    raise Exception("SYSTEM ERROR")
                parentid = menu.get("MNparent")
        log.info("menu dict", menu_dict)
        menu_list = []
        for mnid in menu_dict:
            menu = todict(self.sinterface.get_menu_by_mnid(mnid))
            menu["children"] = menu_dict.get(mnid)
            menu_list.append(menu)
        log.info("menu list", menu_list)
        return menu_list

    def get_managers(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        page_size = int(args.get("page_size"))
        page_num = int(args.get("page_num"))
        or_filter = set()
        if "MAfilter" in args:
            from ManagerSystem.models.model import Manager
            or_filter.add(Manager.MAnicname.like("%{0}%".format(get_str(args, "MAfilter"))))
            or_filter.add(Manager.MAemail.like("%{0}%".format(get_str(args, "MAfilter"))))

        maid = token_to_usid(args.get("token"))
        try:
            pn, count = self.check_page_value(page_num, page_size, "model.Manager.MAid", set(), or_filter)
            start_num = (pn - 1) * page_size
            manager = self.smanager.get_manager_by_maid(maid)
            if not manager:
                return SYSTEM_ERROR
            manager_list = tolist(self.smanager.get_managers(start_num, page_size, or_filter))
            for manager in manager_list:
                manager["MAidentity"] = conversion_MAidentity.get(manager.get("MAidentity"))
                manager["MAstatus"] = conversion_MAstatus.get(manager.get("MAstatus"))
                manager["MAloginTime"] = TimeManager.get_web_time_str(manager.get("MAloginTime"))
                manager["MAcreatTime"] = TimeManager.get_web_time_str(manager.get("MAcreatTime"))
            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = {
                "count": count,
                "page_num": pn,
                "page_size": page_size,
                "Managers": manager_list
            }
            return response
        except Exception as e:
            log.error("get managers", e.message)
            return SYSTEM_ERROR

    def check_page_value(self, page_num, page_size, model_name, and_params, or_params):
        count = self.smanager.get_count_by_or_filter(model_name, and_params, or_params)
        if page_size * page_num > count:
            page_num = count / page_size + 1
        page_num = page_num if page_num > 0 else 1
        return page_num, count

    def get_users(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))
        try:
            manager = self.smanager.get_manager_by_maid(maid)
            if not manager:
                return SYSTEM_ERROR
            if manager.MAidentity > 101 :
                return get_response("ERROR_MESSAGE_NO_PERMISSION","MANAGERSYSTEMERROR", "ERROR_CODE_NO_PERMISSION")
            page_size = int(args.get("page_size"))
            page_num = int(args.get("page_num"))
            or_filter = set()
            if args.get("USfilter"):
                from ManagerSystem.models.model import Users
                or_filter.add(Users.USname.like("%{0}%".format(get_str(args, "USfilter"))))
                or_filter.add(Users.UStelphone.like("%{0}%".format(get_str(args, "USfilter"))))

            from ManagerSystem.config.conversion import conversion_USsex
            pn, count = self.check_page_value(page_num, page_size, "model.Users.USid", set(), or_filter)
            start_num = (pn - 1) * page_size
            users = tolist(self.smanager.get_users(start_num, page_size, or_filter))
            for user in users:
                user["USsex"] = conversion_USsex.get(user.get("USsex"))
                user["UScreateTime"] = TimeManager.get_web_time_str(user.get("UScreateTime"))
                user["USloginTime"] = TimeManager.get_web_time_str(user.get("USloginTime"))
                user["USstatus"] = conversion_MAstatus.get(user.get("USstatus"))

            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")

            response["data"] = {
                "count": count,
                "page_num": pn,
                "page_size": page_size,
                "USers": users
            }
            return response
        except Exception as e:
            log.error("get users", e.message)
            return SYSTEM_ERROR

    def update_users(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        if "UStelphone" not in data:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))
        manager = self.smanager.get_manager_by_maid(maid)
        if manager.MAidentity > 101:
            return get_response("ERROR_MESSAGE_NO_PERMISSION", "MANAGERSYSTEMERROR", "ERROR_CODE_NO_PERMISSION")
        try:
            from ManagerSystem.models.model import Users
            and_filter = {
                Users.UStelphone == data.get("UStelphone")
            }
            users = {
                "USstatus": conversion_MAstatus_resverse.get(get_str(data, "USstatus"))
            }
            update_result = self.smanager.update_user_by_filter(and_filter, users)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("update users", e.message)
            return SYSTEM_ERROR

    def update_manager_by_matel(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        if "MAtelphone" not in data:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))
        manager = self.smanager.get_manager_by_maid(maid)
        if manager.MAidentity > 101:
            return get_response("ERROR_MESSAGE_NO_PERMISSION", "MANAGERSYSTEMERROR", "ERROR_CODE_NO_PERMISSION")
        try:
            from ManagerSystem.models.model import Manager
            mng = {
                "MAstatus": conversion_MAstatus_resverse.get(get_str(data, "MAstatus"))
            }
            update_result = self.smanager.update_users_by_matel(data.get("MAtelphone"), mng)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("update users", e.message)
            return SYSTEM_ERROR
