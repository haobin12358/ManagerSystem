# *- coding:utf8 *-
from flask import Flask
import flask_restful


from ManagerSystem.apis.AManager import AManager
from ManagerSystem.apis.AStocks import AStocks
from ManagerSystem.apis.AProducts import MSProduct
from ManagerSystem.apis.AOrder import MSOrder
from ManagerSystem.apis.ACotegory import MSCategory


sg = Flask(__name__)
api = flask_restful.Api(sg)


api.add_resource(AManager, "/sharp/manager/user/<string:manager>")
api.add_resource(AStocks, "/sharp/manager/stock/<string:stock>")
api.add_resource(MSProduct, "/sharp/manager/product/<string:product>")
api.add_resource(MSOrder, "/sharp/manager/order/<string:order>")
api.add_resource(MSCategory, "/sharp/manager/category/<string:category>")


'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 443, debug=False, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))

'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 7443, debug=False)
# '''
