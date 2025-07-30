from db import SessionLocal
from models.customer import Customer
from models.product import Product
from models.transaction import Transaction
from datetime import datetime, timedelta
import random

db = SessionLocal()

# Clear old data (optional: only if you're testing fresh)
db.query(Transaction).delete()
db.query(Customer).delete()
db.query(Product).delete()
db.commit()

# Insert 10 Customers
customers = []
for i in range(1, 11):
    cust = Customer(
        name=f"Customer{i}",
        email=f"customer{i}@example.com",
        phone_number=1000000000 + i,
        location=random.choice(["Mumbai", "Pune", "Delhi", "Bangalore"])
    )
    db.add(cust)
    customers.append(cust)

# Insert 10 Products
products = []
for i in range(1, 11):
    prod = Product(
        name=f"Product{i}",
        description=f"This is Product {i}",
        price=round(random.uniform(100, 1000), 2)
    )
    db.add(prod)
    products.append(prod)

db.commit()

# Insert 50 Random Transactions
for i in range(50):
    txn = Transaction(
        customer_id=random.choice(customers).customer_id,
        product_id=random.choice(products).product_id,
        purchase_date=datetime.now() - timedelta(days=random.randint(0, 365))
    )
    db.add(txn)

db.commit()
db.close()

print("✅ Dummy data inserted: 10 customers, 10 products, 50 transactions.")
