# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from SBase import SBase, close_session

from models.model import Stocks, StocksProducts

class SStocks(SBase):
    @close_session
    def get_stocks_by_PBid(self, pbid):
        return self.session.query(
            StocksProducts.STid, StocksProducts.SPid, StocksProducts.PBnumber).filter(StocksProducts.PBid == pbid).all()

    @close_session
    def get_stock_by_stid(self, stid):
        return self.session.query(Stocks.STabo, Stocks.STamount, Stocks.STname).filter(Stocks.STid == stid).all()

    @close_session
    def update_stock(self, stid, stock):
        return self.session.query(Stocks).filter(Stocks.STid == stid).update(stock)

    @close_session
    def update_stock_product(self, spid, sp):
        return self.session.query(StocksProducts).filter(StocksProducts.SPid == spid).update(sp)