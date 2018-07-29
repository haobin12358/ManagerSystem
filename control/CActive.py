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
from ManagerSystem.service.SOrder import SOrder
from ManagerSystem.models.model import CouponsActives, CouponsManager, OrderMain, Cardpackage


class CActive():
    def __init__(self):
        self.sactive = SActive()
        self.smanager = SManager()
        self.sorder = SOrder()

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
            "COimage": json.dumps(data.get("COimage")),
            "COname": get_str(data, "COname"),
            "COstatus": conversion_COstatus_resverse.get(get_str(data, "COstatus"), 550),
            "COstart": acstart,
            "COend": acend,
            "COfilter": data.get("COfilter", 0),
            "COother": get_str(data, "COother"),
            "COdiscount": data.get("COdiscount", 1),
            "COamount": data.get("COamount", 0),
            "COtype": conversion_COtype_resverse.get(get_str(data, "COtype")),
            "COnumber": data.get("COnumber", 0),
            "COgenre": conversion_COgenre_resverse.get(get_str(data, "COgenre")),
            "COunit": conversion_PBunit_reverse.get(get_str(data, "COunit")),
            "COtime": TimeManager.get_db_time_str(),
            "COuserfilter": data.get("COuserfilter", 0)
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

    def get_active(self):
        args = request.args.to_dict()
        log.info("args", args)
        params_key = ["token", "page_size", "page_num", "COgenre"]
        for key in params_key:
            if key not in args:
                return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR
        manager = self.smanager.get_manager_by_maid(maid)
        if not manager:
            return TOKEN_ERROR
        page_num = int(args.get("page_num"))
        page_size = int(args.get("page_size"))
        amfilter = {
            CouponsManager.MAid == maid
        }
        cm_dict = {}
        for cm in self.sactive.get_cm_by_filter(amfilter, set()):
            if cm.COid not in cm_dict:
                cm_dict[cm.COid] = [cm.PRid]
            else:
                cm_dict[cm.COid].append(cm.PRid)

        active_list = []
        for coid in cm_dict:
            am_tmp_filter = {
                CouponsActives.COid == coid,
                CouponsActives.COgenre == conversion_COgenre_resverse.get(get_str(args, "COgenre")),
                CouponsActives.COstatus != 560
            }
            ca_list = tolist(self.sactive.get_actives_by_filter(am_tmp_filter, set()))
            for ca in ca_list:
                if args.get("COname") and get_str(args, "COname") not in get_str(ca, "COname"):
                    continue
                if args.get("COid") and get_str(args, "COid") not in get_str(ca, "COid"):
                    continue
                if args.get("COstatus") and conversion_COstatus_resverse.get(get_str(args, "COstatus")) != ca.get("COstatus"):
                    continue
                ca["COstatus"] = conversion_COstatus.get(ca["COstatus"])
                ca["duration"] = TimeManager.get_delta_time(ca["COstart"], ca["COend"])
                ca["COstart"] = TimeManager.get_web_time_str(ca["COstart"])
                ca["COend"] = TimeManager.get_web_time_str(ca["COend"])
                ca["COunit"] = conversion_PBunit.get(ca["COunit"])
                ca["COtype"] = conversion_COtype.get(ca.get("COtype"))
                ca["PRids"] = cm_dict.get(coid)
                ca["COimage"] = json.loads(ca["COimage"])


                active_list.append(ca)
        count = len(active_list)
        if page_size * page_num > count:
            page_num = count / page_size + 1
        active_list = active_list[(page_num - 1) * page_size: page_num * page_size]
        response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["count"] = count
        response["page_size"] = page_size
        response["page_num"] = page_num
        response["CouponsActives"] = active_list
        return response

    def get_situation(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR
        manager = self.smanager.get_manager_by_maid(maid)
        if not manager:
            return TOKEN_ERROR

        days = int(args.get("days", 1))
        try:
            cm_list = self.sactive.get_cm_by_filter({CouponsManager.MAid ==maid}, set())
            coid_list_all = {}.fromkeys([cm.COid for cm in cm_list]).keys()
            timefilter = TimeManager.get_forward_time_web(days=-days)
            # 筛选优惠券/活动创建时间
            # coid_list_filter = []
            # for coid in coid_list_all:
            #     ca = self.sactive.get_actives_by_filter({CouponsActives.COid == coid}, set())
            #     if ca.COtime < TimeManager.get_forward_time_web(days=-days):
            #         continue
            #     coid_list_filter.append(ca.COid)

            om_list = self.sorder.get_om_by_filter(set())
            used_sum = 0
            for om in om_list:
                if om.COid in coid_list_all and om.OMtime > timefilter:
                    used_sum += 1

            cp_list = self.sactive.get_cp_by_filter(set(), set())
            get_num = 0
            for cp in cp_list:
                if cp.COid in coid_list_all and cp.CPtime > timefilter:
                    get_num += 1
            data_dict = {}
            for i in range(1, days):
                sub_time_filter_start = TimeManager.get_forward_time_web(days=-i)
                sub_time_filter_end = TimeManager.get_forward_time_web(days=-(i + 1))

                sub_om_num = 0
                for om in om_list:
                    if om.COid in coid_list_all and sub_time_filter_end < om.OMtime < sub_time_filter_start:
                        sub_om_num += 1
                sub_cp_num = 0
                for cp in cp_list:
                    sub_cp_num += 1
                    if cp.COid in coid_list_all and sub_time_filter_end < cp.CPtime < sub_time_filter_start:
                        sub_cp_num += 1
                data_dict[sub_time_filter_start] = [sub_om_num, sub_cp_num]

            response = get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
            params = [
                {"name": "领取张数", "value": get_num},
                {"name": "使用张数", "value": used_sum},
            ]
            response["data"] = {
                "params": params,
                "data": data_dict
            }
            return response
        except Exception as e:
            log.error("get situation", e.message)
            return SYSTEM_ERROR

    def update_cative_status(self):
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

        coid = data.get("COid")
        log.info("coid", coid)
        log.info("maid", maid)
        costatus = conversion_COstatus_resverse.get(get_str(data, "COstatus"))
        try:
            cmlist = self.sactive.get_cm_by_filter({CouponsManager.MAid == maid, CouponsManager.COid == coid}, set())
            log.info("cmlist", cmlist)
            if not cmlist:
                return SYSTEM_ERROR

            update_result = self.sactive.update_actives(coid, {"COstatus": costatus})
            log.info("update result", update_result)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_ORDER", "OK")
        except Exception as e:
            log.error("update actiave status", e.message)
            return SYSTEM_ERROR



if __name__ == "__main__":
    pass
    # ca = CActive()

    # time_list = []

