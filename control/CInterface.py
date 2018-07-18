import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from ManagerSystem.service.SInterface import SInterface
from ManagerSystem.common.MakeToken import usid_to_token, token_to_usid
from ManagerSystem.globals import log
from ManagerSystem.common.TimeManagert import TimeManager
from ManagerSystem.common.ImportManager import get_response
from ManagerSystem.config.response import SYSTEM_ERROR, PARAMS_MISS
from ManagerSystem.common.ResultManager import todict, tolist
import uuid

class CInterface():
    def __init__(self):
        self.sinterface = SInterface()

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
        print(menu_dict)
        menu_list = []
        for mnid in menu_dict:
            menu = todict(self.sinterface.get_menu_by_mnid(mnid))
            menu["children"] = menu_dict.get(mnid)
            menu_list.append(menu)

        print(menu_list)
        return menu_list



if __name__ == "__main__":
    cint = CInterface()
    menu = cint.get_interface("123")
    print(menu)