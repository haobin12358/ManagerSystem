import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from ManagerSystem.service.SBase import SBase, close_session
from ManagerSystem.models.model import Permission


class SPermission(SBase):
    pass


