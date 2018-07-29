# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy import and_, or_
from ManagerSystem.service.SBase import SBase, close_session
from ManagerSystem.models.model import CouponsActives as CA, CouponsManager as CM, Cardpackage as CP


class SActive(SBase):
    @close_session
    def get_actives_by_filter(self, and_filter, or_filter):
        return self.session.query(
            CA.COid, CA.COabo, CA.COimage, CA.COname, CA.COstatus, CA.COstart, CA.COend, CA.COfilter,
            CA.COother, CA.COutype, CA.COdiscount, CA.COamount, CA.COtype, CA.COnumber, CA.COgenre, CA.COunit,
            CA.COused, CA.COtime, CA.COuserfilter,
        ).filter(and_(*and_filter), or_(*or_filter)).order_by(CA.COtime.desc()).all()

    @close_session
    def get_cm_by_filter(self, and_filter, or_filter):
        return self.session.query(
            CM.MAid, CM.COid, CM.PRid, CM.CMprobability
        ).filter(and_(*and_filter), or_(*or_filter)).all()

    @close_session
    def get_cp_by_filter(self, and_filter, or_filter):
        return self.session.query(
            CP.COid, CP.CAid, CP.USid, CP.CAstatus, CP.CPstart, CP.CPend, CP.CPtime
        ).filter(and_(*and_filter), or_(*or_filter)).all()

    @close_session
    def update_actives(self, coid, actives):
        return self.session.query(CA).filter(CA.COid == coid).update(actives)