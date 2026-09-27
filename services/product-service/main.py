import os
import json
import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)


class Product(BaseModel):
    id: int
    name: str
    price: float


products = [
    Product(id=1, name="Laptop", price=899.99),
    Product(id=2, name="Keyboard", price=49.99),
    Product(id=3, name="Mouse", price=29.99),
]


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "product-service"
    }


@app.get("/products")
def get_products():
    cached = redis_client.get("products")

    if cached:
        return {
            "source": "redis-cache",
            "products": json.loads(cached)
        }

    product_data = [product.model_dump() for product in products]

    redis_client.set(
        "products",
        json.dumps(product_data),
        ex=60
    )

    return {
        "source": "application",
        "products": product_data
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.post("/products")
def create_product(product: Product):
    products.append(product)

    redis_client.delete("products")

    return {
        "message": "Product created",
        "product": product
    }
