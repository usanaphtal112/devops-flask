# Flask Transaction API with Jenkins CI/CD

This project is a simple Flask-based REST API that simulates credit card transactions. It includes basic validation logic and is integrated with a Jenkins pipeline for CI/CD. It's part of my journey to learn DevOps concepts, including continuous integration and delivery.

## 🔧 Tech Stack

- **Flask** – Python micro web framework used to build the API.
- **Jenkins** – Used for automating the build, test, and deployment pipeline.
- **Pytest** – Testing framework for validating API behavior.

## 🚀 API Endpoint

- `POST /api/transaction`  
  Accepts card data and transaction details, approves or rejects based on card status and limit.

## ✅ Example Request

```json
{
  "status": true,
  "number": 123456,
  "limit": 1000,
  "transaction": {
    "amount": 500
  }
}
