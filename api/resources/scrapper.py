from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.scrapper import ScrapperRequestSchema, ScrapperResponseSchema
from utils.scrapper import search
blp = Blueprint(
    "Scrapper API",
    __name__,
    description="Operaciones para scrapear la pagina de www.tiendasjumbo.co",
)

@blp.route("/category/")
class Categories(MethodView):
    @blp.arguments(ScrapperRequestSchema)
    @blp.response(201, ScrapperResponseSchema)
    def post(self, post_data):
        if not post_data['url']:
            abort(
                400,
                message="Scrapper need url parmeter.",
            )
        try:
            data = search(
                url=post_data['url']
            )
            response = {"url": post_data['url'], "products": data}
        except Exception:
            abort(500, message="An error occurred creating the category.")

        return response
