import json
from datetime import datetime

from models.item import Item
from sanic import Sanic
from sanic.exceptions import SanicException

EVENT_BID_CREATE = "bid:create"


class BiddingController:
    _app: Sanic = None

    def __init__(self, app):
        self._app = app

    async def create_bid(cls, request, ws):
        while True:
            # guest_user = request.id
            item = await ws.recv()
            item = json.loads(item)
            if item["event"] == EVENT_BID_CREATE:
                # await self.check_item_eligibility(item["payload"]["item_id"], {"bid": {"amount": item["payload"][
                # "amount"]}})
                print("HAREEEEEE")
                try:
                    await Item.update_one({
                        "_id": item["payload"]["item_id"]
                    }, {"highest": item["payload"]["amount"]})
                except Exception:
                    print("error")
                async with self._app.ctx.redis as redis:
                    await redis.set(f'item:{item["payload"]["item_id"]}:highest', item["payload"]["amount"])

            print("hereeeee")
            highest = await self._app.ctx.redis.get("item:{}:highest".format(item["payload"]["item_id"]))
            await ws.send(highest.decode())

    async def check_item_eligibility(self, item_id, bid):
        item = await Item.find_one({"_id": item_id})
        async with self._app.ctx.redis as redis:
            current_item_highest_bid = await redis.get("item:{}:highest".format(item_id))

        if datetime.strptime(item["start_time"], "%Y-%m-%d %H:%M:%S") >= datetime.now():
            raise SanicException(
                f'Biding for item {item["_id"]} has not started yet!', status_code=400)

        if datetime.strptime(item["end_time"], "%Y-%m-%d %H:%M:%S") <= datetime.now():
            raise SanicException(
                f'Biding for item {item["_id"]} has ended!', status_code=400)

        if bid.amount <= current_item_highest_bid:
            raise SanicException("Invalid bid amount", status_code=400)
