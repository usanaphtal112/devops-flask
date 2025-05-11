#!/usr/bin/python3
"""
This	code	is	used	as	an	example	for	the	Chapter10	of	the	book
DevOps	With	Linux
"""
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)


def check_card(f):
    """
    This	function	validates	the	credit	card	transactions
    """

    @wraps(f)
    def validation(*args, **kwargs):
        """
        This	function	is	a	decorator,
        which	will	return	the	function	corresponding	to	the	respective
        action
        """
        data = request.get_json()

        # Check if card status is blocked
        if not data.get("status"):
            return jsonify(
                {
                    "approved": False,
                    "newLimit": data.get("limit"),
                    "reason": "Blocked Card",
                }
            )

        # Check if transaction amount exceeds card limit
        if data.get("limit") < data.get("transaction", {}).get("amount", 0):
            return jsonify(
                {
                    "approved": False,
                    "newLimit": data.get("limit"),
                    "reason": "Transaction above the limit",
                }
            )

        return f(*args, **kwargs)

    return validation


@app.route("/api/transaction/", methods=["POST"])
@check_card
def transaction():
    """
    This	function	is	resposible	to	expose	the	endpoint	for	receiving
    the	incoming	transactions
    """
    card = request.get_json()
    amount = card.get("transaction", {}).get("amount", 0)
    new_limit = card.get("limit") - amount

    return jsonify({"approved": True, "newLimit": new_limit})


if __name__ == "__main__":
    app.run(debug=True)
