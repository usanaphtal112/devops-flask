#!/usr/bin/python3
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)


def check_card(f):
    @wraps(f)
    def validation(*args, **kwargs):
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


@app.route("/api/transaction", methods=["POST"])
@check_card
def transaction():
    card = request.get_json()
    amount = card.get("transaction", {}).get("amount", 0)
    new_limit = card.get("limit") - amount

    return jsonify({"approved": True, "newLimit": new_limit})


if __name__ == "__main__":
    app.run(debug=True)
