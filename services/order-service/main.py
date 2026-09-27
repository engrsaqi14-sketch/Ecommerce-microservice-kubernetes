import os
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="Order Service")


def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "order-service"
    }


@app.get("/orders")
def get_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER,
            status VARCHAR(50)
        )
    """)

    cursor.execute(
        "SELECT id, product_id, quantity, status FROM orders"
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.commit()
    conn.close()

    return [
        {
            "id": row[0],
            "product_id": row[1],
            "quantity": row[2],
            "status": row[3]
        }
        for row in rows
    ]


@app.post("/orders")
def create_order():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER,
            status VARCHAR(50)
        )
    """)

    cursor.execute("""
        INSERT INTO orders (product_id, quantity, status)
        VALUES (1, 1, 'created')
        RETURNING id
    """)

    order_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "id": order_id,
        "message": "Order created"
    }
