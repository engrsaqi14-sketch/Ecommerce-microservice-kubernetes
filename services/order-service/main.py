from fastapi import FastAPI

app = FastAPI(title="Order Service")


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "order-service"
    }


@app.get("/orders")
def get_orders():
    return [
        {
            "id": 1,
            "product_id": 1,
            "quantity": 2,
            "status": "created"
        }
    ]


@app.post("/orders")
def create_order():
    return {
        "message": "Order created",
        "status": "created"
    }
