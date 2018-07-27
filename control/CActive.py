# *- coding:utf-8 *-
import sys
import json
import uuid
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request


from ManagerSystem.globals import log
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR
from ManagerSystem.config.conversion import conversion_COstatus, conversion_PBunit_reverse, \
    conversion_COstatus_resverse,conversion_COtype, conversion_COtype_resverse,\
    conversion_COgenre, conversion_COgenre_resverse, conversion_PBunit
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid

from ManagerSystem.common.ResultManager import todict, tolist
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.TimeManagert import TimeManager
from ManagerSystem.service.SActive import SActive
from ManagerSystem.service.SManager import SManager
from ManagerSystem.models.model import CouponsActives, CouponsManager

class CActive():
    def __init__(self):
        self.sactive = SActive()
        self.smanager = SManager()

    def add_active(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR
        manager = self.smanager.get_manager_by_maid(maid)
        if not manager:
            return TOKEN_ERROR
        params_list = ["COname", "COabo", "COtype", "COstart", "COend"]
        for key in params_list:
            if key not in data:
                return PARAMS_MISS

        acstart = TimeManager.get_db_time_str(get_str(data, "COstart"))
        acend = TimeManager.get_db_time_str(get_str(data, "COend"))
        if acstart >= acend:
            return get_response("ERROR_MESSAGE_TIME_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_TIME_ERROR")
        coid = str(uuid.uuid1())
        CA = {
            "COid": coid,
            "COabo": get_str(data, "COabo"),
            "COimage": get_str(data, "COimage"),
            "COname": get_str(data, "COname"),
            "COstatus": conversion_COstatus_resverse.get(get_str(data, "COstatus")),
            "COstart": acstart,
            "COend": acend,
            "COfilter": data.get("COfilter"),
            "COother": get_str(data, "COother"),
            "COdiscount": data.get("COdiscount"),
            "COamount": data.get("COamount"),
            "COtype": conversion_COtype_resverse.get(get_str(data, "COtype")),
            "COnumber": data.get("COnumber"),
            "COgenre": conversion_COgenre_resverse.get(get_str(data, "COgenre")),
            "COunit": conversion_PBunit_reverse.get(get_str(data, "COunit")),
        }
        log.info("CA", CA)
        try:
            self.sactive.add_model("CouponsActives", **CA)
        except Exception as e:
            log.error("add CA", e.message)
            return SYSTEM_ERROR
        try:
            prid_list = data.get("PRids")
            if prid_list:
                for prid in prid_list:
                    self.sactive.add_model("CouponsManager", **{
                        "CMid": str(uuid.uuid1()),
                        "COid": coid,
                        "MAid": maid,
                        "PRid": prid,
                        "CMprobability": data.get("CMprobability", 1)
                    })
            else:
                self.sactive.add_model("CouponsManager", **{
                    "CMid": str(uuid.uuid1()),
                    "COid": coid,
                    "MAid": maid,
                    "PRid": "",
                    "CMprobability": data.get("CMprobability", 1)
                })
            return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
        except Exception as e:
            log.error("add CM", e.message)
            return SYSTEM_ERROR





