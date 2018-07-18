# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session

from ManagerSystem.models.model import Menu, ManagerMenu


class SInterface(SBase):

    @close_session
    def get_mnid_by_maid(self, maid):
        return self.session.query(ManagerMenu.MNid).filter(ManagerMenu.MAid == maid).all()

    @close_session
    def get_menu_by_mnid(self, mnid):
        return self.session.query(Menu.MNid, Menu.MNparent, Menu.MNicon, Menu.MNname, Menu.MNurl).filter(Menu.MNid == mnid).first()
