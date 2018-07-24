# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session
from ManagerSystem.models.model import Actives
from ManagerSystem.models.model import Coupons


class SActive(SBase):
    @close_session
    def get_actives_by_maid(self, maid):
        return self.session.query(
            Actives.ACid, Actives.ACabo, Actives.ACstart, Actives.ACimage,
            Actives.ACend).filter(Actives.MAid == maid).all()

    @close_session
    def get_coupons_by_acid(self, acid):
        return self.session.query(
            Coupons.COtype, Coupons.COid, Coupons.COdiscount,
            Coupons.COfilter, Coupons.COamount, Coupons.COutype,
            Coupons.CObrand, Coupons.COstart, Coupons.COend).filter(Coupons.ACid == acid).all()

    @close_session
    def get_coupons_by_coid(self, coid):
        return self.session.query(
            Coupons.COtype, Coupons.COid, Coupons.COdiscount,
            Coupons.COfilter, Coupons.COamount, Coupons.COutype,
            Coupons.CObrand, Coupons.COstart, Coupons.COend).filter(Coupons.ACid == coid).first()
