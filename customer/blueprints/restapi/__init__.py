from flask import Blueprint
from flask_restful import Api

from .resources import CustomerItemResource, CustomerResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(CustomerResource, "/customers/")
    api.add_resource(CustomerItemResource, "/customers/<customer_id>")
    app.register_blueprint(bp)
