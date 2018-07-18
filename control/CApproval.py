# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import uuid
import json
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.common.MakeToken import token_to_usid

from ManagerSystem.config.conversion import conversion_PBunit, \
    conversion_PBunit_reverse, conversion_PRbrand, conversion_PRbrand_reverse, \
    conversion_PRtype, conversion_PRtype_reverse

from ManagerSystem.config.imageconfig import PRSWINGIMAGE, PRABOIMAGE
from ManagerSystem.globals import log


class CApproval():
    def __init__(self):
        pass