from flask import Flask
from flask_smorest import Api

from resources.scrapper import blp as ScrapperBlueprint

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Scrapper API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    api = Api(app)

    @app.route("/healt-check")
    def healt_check():
        return {"message": "API is Running"}
    
    api.register_blueprint(ScrapperBlueprint)

    return app