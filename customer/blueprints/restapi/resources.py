from flask import abort, jsonify
from flask_restful import Resource

from customer.models import Customer


class CustomerResource(Resource):
    def get(self):
        customers = Customer.query.all() or abort(204)
        return jsonify(
            {"customers": [customer.to_dict() for customer in customers]}
        )


class CustomerItemResource(Resource):
    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first() or abort(404)
        return jsonify(customer.to_dict())
