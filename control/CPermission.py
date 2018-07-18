# *- coding:utf-8 *-
import sys
import json
import uuid
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request

from ManagerSystem.service.SStocks import SStocks
from ManagerSystem.service.SProducts import SProducts
from ManagerSystem.common.MakeToken import token_to_usid
from ManagerSystem.globals import log
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS
from ManagerSystem.common.ResultManager import todict, tolist


class CPermission():
    pass
