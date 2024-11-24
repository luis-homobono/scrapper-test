
from marshmallow import Schema, fields

class ScrapperRequestSchema(Schema):
    url = fields.Str(required=True)

class ProductSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    price_promo = fields.Str(dump_only=True)

class ScrapperResponseSchema(Schema):
    url = fields.Str(required=True)
    products = fields.List(
        fields.Nested(ProductSchema), 
        required=False
    )
