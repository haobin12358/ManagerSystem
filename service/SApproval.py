import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session
from ManagerSystem.models.model import Permission as PE, Approval


class AApproval(SBase):
    @close_session
    def get_permission_by_petype_pesublevel(self, petype, pesublevel):
        return self.session.query(PE.MAid, PE.PEid, PE.PEname, PE.PEsubLevel, PE.PEtype)\
            .filter(PE.PEtype == petype, PE.PEsubLevel == pesublevel).all()

