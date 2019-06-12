from mongoengine import *


class Product (Document):
    image = StringField()
    name = StringField()
    price = StringField()
    detail = StringField()
    code = StringField()
    cate_name = StringField()


class Category (Document):
    cate = StringField()


class Manage (Document):
    customer_name = StringField()
    customer_phone = StringField()
    customer_email = StringField()
    customer_address = StringField()
    # customer_payments = ReferenceField(customer_payments)
