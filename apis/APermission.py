# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from ManagerSystem.control.CPermission import CPermission
from ManagerSystem.config.response import APIS_WRONG
from ManagerSystem.globals import log

