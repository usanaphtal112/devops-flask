#!/usr/bin/python3
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_transaction(client):
    """
    Should approve transaction and deduct amount from limit
    """
    card = {
        "status": True,
        "number": 123456,
        "limit": 1000,
        "transaction": {"amount": 500},
    }
    response = client.post("/api/transaction", json=card)
    data = response.get_json()

    assert data.get("approved") is True
    assert data.get("newLimit") == 500


def test_above_limit(client):
    """
    Should reject transaction above card limit
    """
    card = {
        "status": True,
        "number": 123456,
        "limit": 1000,
        "transaction": {"amount": 1500},
    }
    response = client.post("/api/transaction", json=card)
    data = response.get_json()

    assert data.get("approved") is False
    assert "Transaction above the limit" in data.get("reason")


def test_blocked_card(client):
    """
    Should reject transaction for blocked card
    """
    card = {
        "status": False,
        "number": 123456,
        "limit": 1000,
        "transaction": {"amount": 500},
    }
    response = client.post("/api/transaction", json=card)
    data = response.get_json()

    assert data.get("approved") is False
    assert "Blocked Card" in data.get("reason")
