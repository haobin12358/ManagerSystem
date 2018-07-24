# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy import or_, and_
from SBase import SBase, close_session

from ManagerSystem.models.model import Manager, IdentifyingCode, Users

class SManager(SBase):

    @close_session
    def update_manager(self, maid, manager):
        return self.session.query(Manager).filter(Manager.MAid == maid).update(manager)

    @close_session
    def get_manager_by_maid(self, maid):
        return self.session.query(
            Manager.MAname, Manager.MAbusinessLicense, Manager.MAcreatTime,
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

    @close_session
    def get_uptime_by_utel(self, utel):
        return self.session.query(IdentifyingCode.ICtime).filter_by(ICtelphone=utel) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def get_manager_by_matelphone(self, matel):
        return self.session.query(Manager.MAid, Manager.MAname, Manager.MAbusinessLicense, Manager.MAcreatTime,
            Manager.MAcredit, Manager.MAemail, Manager.MAendTime, Manager.MAidentity,
            Manager.MAidImageFront, Manager.MAidImageReverse, Manager.MAidNumber,
            Manager.MApassword, Manager.MAstatus, Manager.MAtelphone).filter(Manager.MAtelphone == matel).first()

    @close_session
    def get_code_by_utel(self, utel):
        return self.session.query(IdentifyingCode.ICcode).filter_by(ICtelphone=utel) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def update_users_by_matel(self, matel, manager):
        return self.session.query(Manager).filter(Manager.MAtelphone == matel).update(manager)

    @close_session
    def get_manager_by_name(self, name):
        return self.session.query(Manager.MAid, Manager.MAname, Manager.MAbusinessLicense, Manager.MAcreatTime,
            Manager.MAcredit, Manager.MAemail, Manager.MAendTime, Manager.MAidentity,
            Manager.MAidImageFront, Manager.MAidImageReverse, Manager.MAidNumber,
            Manager.MApassword, Manager.MAstatus, Manager.MAtelphone).filter(Manager.MAname.like("%{0}%".format(name))).all()

    @close_session
    def get_managers(self, start_num, page_size, or_filter):
        return self.session.query(
            Manager.MAid, Manager.MAnicname, Manager.MAtelphone, Manager.MAcreatTime,
            Manager.MAemail, Manager.MAidentity, Manager.MAstatus,
            Manager.MAloginTime).filter(or_(*or_filter)).offset(start_num).limit(page_size).all()

    @close_session
    def get_users(self, start_num, page_size, or_filter):
        return self.session.query(Users.USname, Users.UStelphone, Users.UScreateTime,
                                  Users.USloginTime, Users.USsex, Users.USstatus)\
            .filter(or_(*or_filter)).offset(start_num).limit(page_size).all()

    @close_session
    def update_user_by_filter(self, and_filter, user):
        return self.session.query(Users).filter(and_(*and_filter)).update(user)
