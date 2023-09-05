from mock import get_mocked_order
from datetime import datetime
from dataclasses import dataclass
from typing import List
from types import SimpleNamespace
import attr



class OrderPlainDataClass():

    def __init__(self, order_id:int, email_address:str, checkout_date:datetime, phone_number:str, tags:List[str]):
        self.order_id = order_id
        self.email_address = email_address
        self.checkout_date = checkout_date
        self.phone_number = phone_number
        self.tags = tags

order = OrderPlainDataClass(**get_mocked_order())
order.order_id = "ASdsad"
print(order)
print(order.order_id)

@dataclass
class OrderDataClass:
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]

order = OrderDataClass(**get_mocked_order())
order.order_id = "ASdsad"
print(order)
print(order.order_id)

@attr.define
class OrderDataAttrClass:
    order_id: int
    email_address: str
    checkout_date: datetime
    phone_number: str
    tags: List[str]

order = OrderDataAttrClass(**get_mocked_order())
order.order_id = "ASdsad"
print(order)
print(order.order_id)

order = SimpleNamespace(**get_mocked_order())
order.order_id = "ASdsad"
print(order)
print(order.order_id)
