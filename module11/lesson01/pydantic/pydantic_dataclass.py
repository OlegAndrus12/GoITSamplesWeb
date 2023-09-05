from mock import get_mocked_order
from datetime import date
from pydantic import BaseModel, field_validator, ValidationError
from typing import List
from pprint import pprint


class OrderPydantic(BaseModel):
    order_id: int
    email_address: str
    checkout_date: date
    phone_number: str
    tags: List[str]

    @field_validator("email_address")
    def email_address_validator(cls, val):
        if not "@" in val:
            raise ValueError("Invalid email")
        return val

class OrdersList(BaseModel):
    list_name: str
    orders: List[OrderPydantic]


try:
    order = OrderPydantic(**get_mocked_order())
except ValidationError as e:
    pprint(e.json())

data = """
        {   
            "order_id": 82, 
            "email_address": "zmartinez@example.com",
            "checkout_date": "2008-09-23",
            "phone_number": "9353830438",
            "tags": ["west", "save", "military"]
        }
        """
order = OrderPydantic.model_validate_json(data)
pprint(order)
print(order.order_id)


print("*" * 10)
orders = [get_mocked_order() for i in range(2)]
orders[1]["email_address"] = "asd"
try:
    data2 = OrdersList(**{"list_name" : "Silpo", "orders" : orders})
    print(data2.model_dump_json())
except ValidationError as e:
    pprint(e.json())
