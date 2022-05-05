from datetime import date

from sanic_motor import BaseModel


# Auctioned Item
class Item(BaseModel):
    __coll__ = 'item'
    auctioneer_id: int
