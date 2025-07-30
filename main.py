from fastapi import FastAPI
from models import customer
from models import product
from models import transaction
from db import *

from routes.customer_routes import router as customer_router
from routes.product_routes import router as product_router
from routes.transaction_routes import router as transaction_router
from routes.recommendation_routes import router as recommendation_router
Base.metadata.create_all(engine)

app=FastAPI()
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(transaction_router)
app.include_router(recommendation_router)