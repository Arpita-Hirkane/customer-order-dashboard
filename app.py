from flask import Flask, render_template
from repository.order_repository import (
    get_order_history,
    get_highest_value_order,
    get_most_active_customer
)

app = Flask(__name__)


@app.route("/")
def home():
    history = get_order_history()
    highest_order = get_highest_value_order()
    active_customer = get_most_active_customer()

    return render_template(
        "orders.html",
        history=history,
        highest_order=highest_order,
        active_customer=active_customer
    )


if __name__ == "__main__":
    app.run(debug=True)
