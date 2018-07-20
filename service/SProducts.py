import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from sqlalchemy import or_, and_
from SBase import SBase, close_session
from ManagerSystem.models.model import Products
from ManagerSystem.models.model import Brands
from ManagerSystem.models.model import ProductsBrands as PB


class SProducts(SBase):
    @close_session
    def get_product_by_maid(self, maid):
        return self.session.query(
            Products.PRid, Products.PRname, Products.PRvideo, Products.PRimage, Products.PRtype,
            Products.PRaboimage, Products.PRinfo, Products.PRbrand, Products.PRvideostart
        ).filter(Products.MAid == maid).all()

    @close_session
    def get_productbrand_by_prid(self, prid):
        for i in prid:
            print(type(i), i)
        return self.session.query(
            PB.PBid, PB.PRid, PB.BRid, PB.PBprice, PB.PBunit, PB.PBstatus,
            PB.PBsalesvolume, PB.PBscore, PB.PBimage
        ).filter(PB.PRid == prid).all()

    @close_session
    def get_product_by_pbid_filters(self, pbid):
        return self.session.query(
            PB.PRid, PB.BRid, PB.PBunit, PB.PBprice,
            PB.PBsalesvolume, PB.PBscore, PB.PBimage) \
            .filter_by(PBstatus=201).filter_by(PBid=pbid).first()

    @close_session
    def get_all_brand_by_brid_last(self, brid):
        brand_list = {}
        while brid != "0":
            brand = self.session.query(Brands.BRfromid, Brands.BRkey,
                                       Brands.BRvalue).filter_by(BRid=brid).first()
            brid, brkey, brvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
            brand_list.keys().append(brkey)
            brand_list[brkey] = brvalue
        return brand_list

    @close_session
    def get_brand_by_brid(self, brid):
        return self.session.query(Brands.BRfromid, Brands.BRkey, Brands.BRvalue) \
            .filter_by(BRid=brid).first()

    @close_session
    def get_product_by_prid(self, prid):
        return self.session.query(Products.PRname, Products.PRbrand, Products.PRinfo,
                                  Products.PRvideo, Products.PRtype, Products.PRimage,
                                  Products.PRaboimage, Products.PRvideostart, Products.PRtime).filter_by(
            PRid=prid).first()

    @close_session
    def get_pbimg_by_prid(self, prid):
        return self.session.query(PB.PBimage).filter_by(PRid=prid).all()

    @close_session
    def get_brid_by_prid(self, prid):
        pbid = None
        try:
            pbid = self.session.query(PB.BRid).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbid

    @close_session
    def get_all_prid(self, start_num, page_size, and_filter, or_fillter):
        return self.session.query(Products.PRid).filter(and_(*and_filter), or_(*or_fillter)).offset(start_num).limit(page_size).all()

    @close_session
    def get_brid_by_key_value(self, key, value):
        return self.session.query(Brands.BRid).filter_by(BRkey=key).filter_by(BRvalue=value).all()

    @close_session
    def get_brfromid_by_brid(self, brid):
        return self.session.query(Brands.BRfromid).filter(Brands.BRid == brid).scalar()

    @close_session
    def get_pball_by_brid(self, brid):
        return self.session.query(PB.PBimage, PB.PBunit, PB.PBprice, PB.PBscore,
                                  PB.PBsalesvolume, PB.PBid).filter_by(BRid=brid).first()

    @close_session
    def get_pball_by_prid(self, prid):
        return self.session.query(
            PB.PBimage, PB.PBunit, PB.PBprice, PB.PBscore, PB.PBstatus,
            PB.PBsalesvolume, PB.PBid).filter(PB.PRid == prid, PB.PBstatus != 207).all()

    @close_session
    def get_pball_by_prid_pbstatus(self, prid, pbstatus):
        return self.session.query(
            PB.PBimage, PB.PBunit, PB.PBprice, PB.PBscore,
            PB.PBsalesvolume, PB.PBid, PB.PBstatus).filter(PB.PRid == prid, PB.PBstatus == pbstatus).all()

    def get_volue_score_by_pbid(self, pbid):
        volue_score = None
        try:
            volue_score = self.session.query(PB.PBsalesvolume, PB.PBscore) \
                .filter_by(PBid=pbid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return volue_score

    def update_score_by_pbid(self, pbid, product_brand):
        try:
            self.session.query(PB).filter_by(PBid=pbid).update(product_brand)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            print e.message
            self.session.rollback()
            self.session.close()
            return False

    @close_session
    def get_pbid_by_prid(self, prid):
        pbid = None
        try:
            pbid = self.session.query(PB.PBid).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbid

    @close_session
    def get_pbprice_by_prid(self, prid):
        return self.session.query(PB.PBprice).filter_by(PRid=prid).all()

    @close_session
    def get_pbvolume_by_prid(self, prid):
        pbvolume = None
        try:
            pbvolume = self.session.query(PB.PBsalesvolume).filter_by(PRid=prid).all()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return pbvolume

    def get_prid_by_pbid(self, pbid):
        prid = None
        try:
            prid = self.session.query(PB.PRid).filter_by(PBid=pbid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return prid

    @close_session
    def get_product_by_pbid(self, pbid):
        return self.session.query(
            PB.PRid, PB.BRid, PB.PBunit, PB.PBprice,
            PB.PBsalesvolume, PB.PBscore, PB.PBimage).filter_by(PBid=pbid).first()

    @close_session
    def update_product(self, prid, product):
        return self.session.query(Products).filter_by(PRid=prid).update(product)

    @close_session
    def update_pb(self, pbid, pb):
        return self.session.query(PB).filter_by(PBid=pbid).update(pb)

    @close_session
    def get_product_by_filter(self, pr_filter):
        return self.session.query(
            Products.PRid, Products.PRname, Products.PRvideo, Products.PRimage, Products.PRtype, Products.CTid,
            Products.PRaboimage, Products.PRinfo, Products.PRbrand, Products.PRvideostart).filter(*pr_filter).all()
