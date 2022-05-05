from sanic import Sanic, json as json_response
from datetime import datetime
from models.item import Item
from bson import ObjectId
from helpers.date_helper import convert_date


class ItemController:
    _app: Sanic

    def __init__(self, app):
        self._app = app

    async def create_item(self, request):
        item = request.json
        item_start_time = convert_date(item["start_time"])
        item_end_time = convert_date(item["end_time"])
        new_item = await Item.insert_one({
            "_id": str(ObjectId()),
            "name": str(item["name"]),
            "description": str(item["description"]),
            "start_time": item_start_time,
            "end_time": item_end_time,
            "min_amount": item["min_amount"],
            "min_increase": item["min_increase"],
            "highest_bid": item["highest_bid"]
        })
        created_item = await Item.find_one({
            "_id": new_item.inserted_id
        }, as_raw=True)
        return json_response(created_item)

    async def find_item_by_id(self, request, id):
        item_id = id
        item = await Item.find_one({
            "_id": item_id
        }, as_raw=True)
        return json_response(item)
