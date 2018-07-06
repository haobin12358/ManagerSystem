# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session

from models.model import Manager

class SManager(SBase):

    @close_session
    def update_manager(self, maid, manager):
        return self.session.query(Manager).filter(Manager.MAid == maid).update(manager)

    @close_session
    def get_manager_by_maid(self, maid):
        return self.session.query(
            Manager.MAid, Manager.MAname, Manager.MAbusinessLicense, Manager.MAcreatTime,
            Manager.MAcredit, Manager.MAemail, Manager.MAendTime, Manager.MAidentity,
            Manager.MAidImageFront, Manager.MAidImageReverse, Manager.MAidNumber,
            Manager.MApassword, Manager.MAstatus, Manager.MAtelphone
        ).filter(Manager.MAid == maid).first()

    @close_session
    def get_manager_by_maname_mapassword(self, maname, mapassword):
        return self.session.query(
            Manager.MAid, Manager.MAname, Manager.MAbusinessLicense, Manager.MAcreatTime,
            Manager.MAcredit, Manager.MAemail, Manager.MAendTime, Manager.MAidentity,
            Manager.MAidImageFront, Manager.MAidImageReverse, Manager.MAidNumber,
            Manager.MApassword, Manager.MAstatus, Manager.MAtelphone
        ).filter(Manager.MAname == maname, Manager.MApassword == mapassword).first()