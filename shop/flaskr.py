# *- coding:utf8 *-
from flask import Flask
import flask_restful
from apis.AUsers import AUsers
from apis.AProduct import AProduct
from apis.ACarts import ACarts
from apis.ACategory import ACategory
from apis.AShop import AShop
from apis.AReview import AReview
from apis.AOrders import AOrders
from apis.ALocations import ALocations
from apis.ACoupons import ACoupons
from apis.AAddress import AAddress

bk = Flask(__name__)
api = flask_restful.Api(bk)

api.add_resource(AUsers, "/love/shop/users/<string:users>")
api.add_resource(AProduct, "/love/shop/product/<string:product>")
api.add_resource(ACarts, "/love/shop/salelist/<string:cart>")
api.add_resource(AReview, "/love/shop/review/<string:review>")
api.add_resource(ACategory, "/love/shop/category/<string:category>")
api.add_resource(AShop, "/love/shop/shop/<string:shop>")
api.add_resource(AOrders, "/love/shop/orders/<string:orders>")
api.add_resource(ALocations, "/love/shop/locations/<string:locations>")
api.add_resource(ACoupons, "/love/shop/cardpkg/<string:card>")
api.add_resource(AAddress, "/love/shop/address/<string:address>")

if __name__ == '__main__':
    bk.run('0.0.0.0', 7444, debug=True)
