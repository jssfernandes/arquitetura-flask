from flask import Blueprint

from .views import index, customer

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/customers", view_func=index)
bp.add_url_rule("/customers/<customer_id>", view_func=customer, endpoint="customerview")


def init_app(app):
    app.register_blueprint(bp)
