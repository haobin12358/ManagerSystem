# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session
from ManagerSystem.models.model import OrderMain, Orderpart, Locations


class SOrder(SBase):
    @close_session
    def get_order_part_list_by_pbid(self, pbid):
        return self.session.query(
            Orderpart.OMid, Orderpart.OPid, Orderpart.PBid, Orderpart.PRnumber).filter(Orderpart.PBid == pbid).all()

    @close_session
    def get_location_by_usid(self, userid):
        return self.session.query(
            Locations.LOid, Locations.LOtelphone, Locations.LOname, Locations.LOno, Locations.LOdetail,
            Locations.LOprovince, Locations.LOcity, Locations.LOarea).filter(Locations.USid == userid).first()

    @close_session
    def get_order_part_list_by_omid(self, omid):
        return self.session.query(
            Orderpart.OPid, Orderpart.PBid, Orderpart.PRnumber).filter(Orderpart.OMid == omid).all()

    @close_session
    def get_order_main_list_by_usid(self, usid):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice, OrderMain.OMlogisticsName
        ).filter(OrderMain.USid == usid).order_by(OrderMain.OMtime.desc()).all()

    @close_session
    def get_order_main_by_om_id(self, omid):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid, OrderMain.USid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice, OrderMain.OMlogisticsName
        ).filter(OrderMain.OMid == omid).first()

    @close_session
    def get_order_main_list(self, start, end):
        return self.session.query(OrderMain.OMid, OrderMain.LOid, OrderMain.OMabo, OrderMain.OMtime) \
            .filter(start <= OrderMain.OMtime, OrderMain.OMtime <= end).order_by(OrderMain.OMtime).all()

    @close_session
    def get_location_by_loid(self, loid):
        return self.session.query(
            Locations.LOid,
            Locations.LOname,
            Locations.LOtelphone,
            Locations.LOno,
            Locations.LOdetail,
            Locations.LOprovince,
            Locations.LOcity,
            Locations.LOarea,
            Locations.LOisedit
        ).filter(Locations.LOid == loid).first()

    @close_session
    def update_order(self, omid, ordermain):
        return self.session.query(OrderMain).filter(OrderMain.OMid == omid).update(ordermain)

    @close_session
    def get_om_by_filter(self, omfilter):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid, OrderMain.USid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice, OrderMain.OMlogisticsName).filter(*omfilter).all()
