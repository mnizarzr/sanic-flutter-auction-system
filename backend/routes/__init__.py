from pprint import pprint

from sanic import Sanic, Blueprint
from controllers.item_controller import ItemController
from controllers.bidding_controller import BiddingController


def load_routes(app: Sanic):

    bidding_controller = BiddingController(app)

    # bp = Blueprint("mymymy", url_prefix="/bpbp")
    # bp.add_websocket_route(bidding_controller.create_bid, "/bid")
    # app.blueprint(bp)

    # item_controller = ItemController(app)
    #
    # app.add_route(item_controller.create_item, uri="/item", methods={"POST"})
    # app.add_route(item_controller.find_item_by_id, uri="/item/<id>", methods={"GET"})
    app.add_websocket_route(bidding_controller.create_bid, "/bid")

    for route in app.router.routes_all:
        pprint(route)

    # item_blueprint = Blueprint("item", url_prefix="/item")
    # bidding_blueprint = Blueprint("bid", url_prefix="/bid")
    #
    # item_blueprint.add_route(item_controller.create_item, "/", methods={"POST"})
    # item_blueprint.add_route(item_controller.find_item_by_id, "/<id>", methods={"GET"})
    #
    # bidding_blueprint.add_websocket_route(bidding_controller.create_bid, "/")
    #
    # bp = Blueprint.group(item_blueprint, bidding_blueprint)
    # app.blueprint(bp)
