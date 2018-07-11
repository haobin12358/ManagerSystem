# *- coding:utf8 *-
from flask import Flask
import flask_restful


from apis.AManager import AManager
from apis.AStocks import AStocks


sg = Flask(__name__)
api = flask_restful.Api(sg)


api.add_resource(AManager, "/sharp/manager/user/<string:manager>")
api.add_resource(AStocks, "/sharp/manager/stock/<string:stock>")


'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 443, debug=False, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))

'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 7444, debug=False)
# '''
