from flask import abort, render_template
from customer.models import Customer


def index():
    customers = Customer.query.all()
    return render_template("index.html", customers=customers)


def customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("customer.html", customer=customer)
