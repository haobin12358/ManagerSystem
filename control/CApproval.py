# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid
import json
from ManagerSystem.globals import log
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR
from ManagerSystem.config.conversion import conversion_APstatus, conversion_APstatus_resverse, \
    conversion_PEtype, conversion_PEtype_resverse
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.ResultManager import tolist, todict
from ManagerSystem.common.TimeManagert import TimeManager
from ManagerSystem.service.SApproval import SApproval
from ManagerSystem.service.SManager import SManager
from ManagerSystem.models.model import Approval


class CApproval():
    def __init__(self):
        self.sapproval = SApproval()
        self.smanager = SManager()

    def add_approval(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        if "PEtype" not in data or "APcontent" not in data:
            return PARAMS_MISS

        petype = conversion_PEtype_resverse.get(get_str(data, "PEtype"))
        apreceive_list =[apreceive.MAid for apreceive in  self.sapproval.get_permission_by_petype_pesublevel(petype, 1)]
        if not apreceive_list:
            return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")

        apstart = token_to_usid(args.get("token"))
        try:
            apname = get_str(data, "PEtype") + str(uuid.uuid1())
            for apreceive in apreceive_list:
                self.sapproval.add_model("Approval", **{
                    "APid": str(uuid.uuid1()),
                    "APname": apname,
                    "APstart": apstart,
                    "APstatus": 445,
                    "APreceive": apreceive,
                    "PEtype": petype,
                    "APremark": "",
                    "APcontent": data.get("APcontent"),
                    "APtime": TimeManager.get_db_time_str()
                    })
            return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
        except Exception as e:
            log.error("add approval", e.message)
            return SYSTEM_ERROR

    def update_approval(self):
        args = request.args.to_dict()
        log.info("args", args )
        if "token" not in args:
            return PARAMS_MISS
        data = json.loads(request.data)
        log.info("data", data)
        params = ["APid",  "APaction", 'APremark']
        for key in params:
            if key not in data:
                return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR
        try:
            approval = todict(self.sapproval.get_approval_by_apid(data.get("APid")))
            log.info("approval", approval)

            petype = approval.get("PEtype")
            apaction = get_str(data, "APaction")

            pemaxlevel = self.sapproval.get_max_level(petype)
            log.info("max level", pemaxlevel)
            permission = self.sapproval.gert_pemission_by_maid_petype(maid, petype)
            log.info("permission", permission)

            manager = todict(self.smanager.get_manager_by_maid(maid))
            apremark = get_str(approval, "APremark", "") + "\n" + get_str(manager, "MAname") + ":\n" + get_str(data, "APremark", "")
            log.info("apremark", apremark)
            update_approval = {
                "APid": str(uuid.uuid1()),
                "APname": approval.get("APname"),
                "APremark": apremark,
                "APstart": approval.get("APstart"),
                "APtime": approval.get("APtime"),
                "APcontent": approval.get("APcontent"),
                "PEtype": approval.get("PEtype")
            }
            recevie_list = []
            if apaction == "同意":
                if pemaxlevel == permission.PEsubLevel:
                    update_approval["APstatus"] = 445
                    self.dealapproval(petype, data.get("APcontent"))
                    self.sapproval.update_approval_by_name(approval.get("APname"), {"APstatus": 445, "APremark": apremark})

                else:
                    update_approval["APstatus"] = 443
                    self.sapproval.update_approval_by_name(approval.get("APname"), {"APstatus": 442, "APremark": apremark})
                    recevie_list = self.sapproval.get_permission_by_petype_pesublevel(petype, permission.PEsubLevel + 1)

            else:
                update_approval["APstatus"] = 444
                update_approval["APreceive"] = approval.get("APstart")
                self.sapproval.update_approval_by_name(approval.get("APname"), {"APstatus": 444, "APremark": apremark})

            if recevie_list:
                for recevie in recevie_list:
                    update_approval["APreceive"] = recevie.MAid
                    self.sapproval.add_model("Approval", **update_approval)
            else:
                self.sapproval.add_model("Approval", **update_approval)

            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("update approval", e.message)
            return SYSTEM_ERROR

    def dealapproval(self, petypem, APcontent):
        if petypem == 304:
            from ManagerSystem.service.SProducts import SProducts
            spro = SProducts()
            pb = {
                "PBstatus": 201
            }
            pb_list = [PB.PBid for PB in spro.get_pbid_by_prid(APcontent)]
            log.info("len pblist", len(pb_list))
            for pbid in pb_list:
                spro.update_pb(pbid, pb)
        # todo 补充其他审批的处理

    def get_approval(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR

        page_size = int(args.get("page_size"))
        page_num = int(args.get("page_num"))

        approval_filter = {
            Approval.APreceive == maid,
        }
        if args.get("APname"):
            approval_filter.add(Approval.APname.like("%{0}%".format(get_str(args, "APname"))))
        if args.get("APstart"):
            apstart = [ma.MAid for ma in self.smanager.get_manager_by_name(args.get("APstart"))]
            approval_filter.add(Approval.APstart.in_(apstart))
        pn, count = self.check_page_value(page_num, page_size, "model.Approval.APid", approval_filter, set())
        start_num = (pn - 1) * page_size
        try:
            approval_list = tolist(self.sapproval.get_approval_by_and_filter(start_num, page_size, approval_filter))
            log.info("approval", approval_list)
            for approval in approval_list:
                approval["APstatus"] = conversion_APstatus.get(approval.get("APstatus", 441))
                approval["PEtype"] = conversion_PEtype.get(approval.get("PEtype", 304))
                manager = self.smanager.get_manager_by_maid(approval.get("APstart"))
                log.info("manager", manager)
                approval["APstart"] = manager.MAname
                approval["APtime"] = TimeManager.get_web_time_str(approval.get("APtime"))
            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = {
                "approvals": approval_list,
                "count": count,
                "page_size": page_size,
                "page_num": page_num
            }
            return response
        except Exception as e:
            log.error("get approval", e.message)
            return SYSTEM_ERROR

    def check_page_value(self, page_num, page_size, model_name, and_params, or_params):
        count = self.sapproval.get_count_by_or_filter(model_name, and_params, or_params)
        if page_size * page_num > count:
            page_num = count / page_size
        page_num = page_num if page_num > 0 else 1
        return page_num, count

    def add_permission(self):
        args = request.args.to_dict()
        log.info("args", args)
        data = json.loads(request.data)
        log.info("data", data)
        if "token" not in args:
            return PARAMS_MISS
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR
        params_list = ["MAtelphone", "PEtype"]
        for k in params_list:
            if k not in data:
                return PARAMS_MISS
        manager = self.smanager.get_manager_by_maid(maid)
        if not manager:
            return TOKEN_ERROR
        petype = conversion_PEtype_resverse.get(get_str(data, "PEtype"), 304)
        try:
            permissioner = self.smanager.get_manager_by_matelphone(data.get("MAtelphone"))
            log.info("permissioner", permissioner)

            if manager.MAidentity != 100:
                return get_response("ERROR_MESSAGE_NO_PERMISSION", "MANAGERSYSTEMERROR", "ERROR_CODE_NO_PERMISSION")
            permission = self.sapproval.get_permission_by_maid_petype(permissioner.MAid, petype)
            log.info("permission", permission)
            if not permission:
                self.sapproval.add_model("Permission", **{
                    "PEid": str(uuid.uuid1()),
                    "PEname": data.get("PEname", ""),
                    "MAid": permissioner.MAid,
                    "PEtype": petype,
                    "PEsubLevel": data.get("PEsubLevel", 1)
                })
            else:
                self.sapproval.update_permission(permission.PEid, {"PEsubLevel": data.get("PEsubLevel", 1)})
            return get_response("SUCCESS_MESSAGE_ADD_DATA", "OK")
        except Exception as e:
            log.error("add permission", e.message)
            return SYSTEM_ERROR

    def update_permission(self):
        args = request.args.to_dict()
        log.info("args", args)
        data = json.loads(request.data)
        log.info("data", data)
        if "token" not in args:
            return PARAMS_MISS
        maid = token_to_usid(args.get("token"))
        manager = self.smanager.get_manager_by_maid(maid)
        if manager.MAidentity != 100:
            return get_response("ERROR_MESSAGE_NO_PERMISSION", "MANAGERSYSTEMERROR", "ERROR_CODE_NO_PERMISSION")
        if "PEid" not in data:
            return PARAMS_MISS
        permission = {
            "PEtype": data.get("PEtype"),
            "PEsubLevel": data.get("PEsubLevel"),
        }
        try:
            update_result = self.sapproval.update_permission(data.get("PEid"), permission)
            if not update_result:
                return get_response("ERROR_MESSAGE_DB_ERROR", "MANAGERSYSTEMERROR", "ERROR_CODE_DB_ERROR")
            return get_response("SUCCESS_MESSAGE_UPDATE_DATA", "OK")
        except Exception as e:
            log.error("update permission", e.message)
            return SYSTEM_ERROR
