import random
from faker import Faker

def get_mocked_order():
    fake = Faker()

    mock = {
        "order_id": "asdsadasd",
        "email_address": "andrusoleg123gmail.com",
        "checkout_date": fake.date(),
        "phone_number": fake.phone_number(),
        "tags": fake.words(),
    }
    return mock