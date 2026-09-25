from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")


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
    return {"status": "healthy", "service": "product-service"}


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {
        "message": "Product created",
        "product": product
    }
