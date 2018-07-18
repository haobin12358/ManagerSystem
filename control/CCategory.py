# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid
import json
from ManagerSystem.globals import log
from ManagerSystem.service.SCategory import SCategory
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS, TOKEN_ERROR
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.common.Tools import get_str
from ManagerSystem.common.ResultManager import tolist
from ManagerSystem.models.model import Category, CategoryBrand


class CCategory():
    def __init__(self):
        self.scategory = SCategory()

    def get_first(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args:
            return PARAMS_MISS

        category_filter = {
            Category.CTfromid == "0"
        }
        try:
            cate_list = tolist(self.scategory.get_category_by_filter(category_filter))
            log.info("cate list", cate_list)
            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = cate_list
            return response
        except Exception as e:
            log.error("get first", e.message)
            return SYSTEM_ERROR

    def get_child(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args or "CTid" not in args:
            return PARAMS_MISS

        ctid = get_str(args, "CTid")
        try:
            category_filter = {
                Category.CTfromid == ctid
            }
            ct_list = tolist(self.scategory.get_category_by_filter(category_filter))
            log.info("ct_list", ct_list)
            response =get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = ct_list
            return response
        except Exception as e:
            log.error("get child", e.message)
            return SYSTEM_ERROR

    def get_categorybrands(self):
        args = request.args.to_dict()
        log.info("args", args)
        if "token" not in args or "CTid" not in args:
            return PARAMS_MISS

        ctid = get_str(args, "CTid")
        try:
            category_filter = {
                CategoryBrand.CTid == ctid
            }
            cb_list = tolist(self.scategory.get_categorybrands_by_filter(category_filter))
            log.info("cb list", cb_list)
            response = get_response("SUCCESS_MESSAGE_GET_INFO", "OK")
            response["data"] = cb_list
            return response
        except Exception as e:
            log.error("get categprybrands", e.message)
            return SYSTEM_ERROR

    def add_category(self):
        args = request.args.to_dict()
        log.info("args", args)
        data = json.loads(request.data)
        if "token" not in args:
            return PARAMS_MISS

        # todo 权限审核
        try:
            maid = token_to_usid(args.get("token"))
        except:
            return TOKEN_ERROR

        ctfromid = "0"
        if "CTid" in data:
            ctfromid = get_str(data, "CTid")

        try:
            ctid = str(uuid.uuid1())
            cateary = {
                "CTid": ctid,
                "CTfromid": ctfromid,
                "MAid": maid,
                "CTname": data.get("CTname")
            }
            self.scategory.add_model("Category", **cateary)
        except Exception as e:
            log.error("add category", e.message)
            return SYSTEM_ERROR

    # def add_categorybranch(self):
