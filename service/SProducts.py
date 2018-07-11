import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session
from models.model import Products
from models.model import ProductsBrands as PB


class SProducts(SBase):
    @close_session
    def get_product_by_maid(self, maid):
        return self.session.query(
            Products.PRid, Products.PRname, Products.PRvideo, Products.PRimage, Products.PRtype,
            Products.PRaboimage, Products.PRinfo,  Products.PRbrand, Products.PRvideostart
        ).filter(Products.MAid == maid).all()

    @close_session
    def get_productbrand_by_prid(self, prid):
        for i in prid:
            print(type(i), i)
        return self.session.query(
            PB.PBid, PB.PRid, PB.BRid, PB.PBprice, PB.PBunit, PB.PBstatus,
            PB.PBsalesvolume, PB.PBscore, PB.PBimage
        ).filter(PB.PRid == prid).all()