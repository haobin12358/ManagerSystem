# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session

class SActive(SBase):
    @close_session
    def get_actives_by_maid(self, maid):
        return self.session.query().all()

    @close_session
    def get_coupons_by_acid(self, acid):
        return self.session.query().filter().all()

    @close_session
    def get_coupons_by_coid(self, coid):
        return self.session.query().filter().first()
