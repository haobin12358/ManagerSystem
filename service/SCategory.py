# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session

from ManagerSystem.models.model import Category, CategoryBrand
from sqlalchemy import or_, and_

class SCategory(SBase):
    @close_session
    def get_category_by_or_filter(self, cate_filter):
        return self.session.query(
            Category.CTfromid, Category.CTid, Category.CTname).filter(or_(*cate_filter)).all()

    @close_session
    def get_category_by_and_filter(self, cate_filter):
        return self.session.query(
            Category.CTfromid, Category.CTid, Category.CTname).filter(and_(*cate_filter)).all()

    @close_session
    def get_categorybrands_by_filter(self, cate_filter):
        return self.session.query(
            CategoryBrand.CBid, CategoryBrand.CTid,
            CategoryBrand.CBname, CategoryBrand.CBvalue).filter(*cate_filter).all()
