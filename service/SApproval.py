import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from sqlalchemy import func, and_
from SBase import SBase, close_session
from ManagerSystem.models.model import Permission as PE, Approval


class SApproval(SBase):
    @close_session
    def get_permission_by_petype_pesublevel(self, petype, pesublevel):
        return self.session.query(PE.MAid, PE.PEid, PE.PEname, PE.PEsubLevel, PE.PEtype)\
            .filter(PE.PEtype == petype, PE.PEsubLevel == pesublevel).all()

    @close_session
    def get_max_level(self, petype):
        return self.session.query(func.max(PE.PEsubLevel)).filter(PE.PEtype == petype).scalar()

    @close_session
    def get_approval_by_apid(self, apid):
        return self.session.query(
            Approval.APid, Approval.APname, Approval.APremark, Approval.APstart,
            Approval.APreceive, Approval.APstatus, Approval.PEtype, Approval.APcontent, Approval.APtime
        ).filter(Approval.APid == apid).first()

    @close_session
    def gert_pemission_by_maid_petype(self, maid, petype):
        return self.session.query(PE.MAid, PE.PEid, PE.PEname, PE.PEsubLevel, PE.PEtype).filter(
            PE.PEtype == petype, PE.MAid == maid
        ).first()

    @close_session
    def update_approval(self, apid, approval):
        return self.session.query(Approval).filter(Approval.APid == apid).update(approval)

    @close_session
    def get_approval_by_and_filter(self, start_num, page_size, approval_filter):
        return self.session.query(
            Approval.APid, Approval.APname, Approval.APremark, Approval.APstart,
            Approval.APreceive, Approval.APstatus, Approval.PEtype, Approval.APcontent, Approval.APtime
        ).filter(and_(*approval_filter)).offset(start_num).limit(page_size).all()

    @close_session
    def get_permission_by_peid(self, peid):
        return self.session.query(PE.MAid, PE.PEid, PE.PEname, PE.PEsubLevel, PE.PEtype).filter(
            PE.PEid == peid).first()

    @close_session
    def update_permission(self, peid, permission):
        return self.session.query(PE).filter(PE.PEid == peid).update(permission)

    @close_session
    def get_permission_by_maid_petype(self, maid, petype):
        return self.session.query(PE.MAid, PE.PEid, PE.PEname, PE.PEsubLevel, PE.PEtype).filter(
            PE.MAid == maid, PE.PEtype == petype).first()

    @close_session
    def update_approval_by_name(self, apname, approval):
        return self.session.query(Approval).filter(Approval.APname == apname).update(approval)

    @close_session
    def get_approval_by_maid(self, maid):
        return self.session.query(Approval.APid, Approval.APname, Approval.APremark, Approval.APstart,
            Approval.APreceive, Approval.APstatus, Approval.PEtype, Approval.APcontent, Approval.APtime
        ).filter(Approval.APstart == maid, Approval.APstatus == 405).all()