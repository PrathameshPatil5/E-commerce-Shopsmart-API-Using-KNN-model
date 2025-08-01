from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from db import SessionLocal
from models.transaction import Transaction

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema
class TransactionCreate(BaseModel):
    customer_id: int
    product_id: int
    purchase_date: datetime

# POST: Create transaction
@router.post("/transactions/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    new_txn = Transaction(
        customer_id=transaction.customer_id,
        product_id=transaction.product_id,
        purchase_date=transaction.purchase_date
    )
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return {"message": "Transaction added", "transaction_id": new_txn.transaction_id}

# GET: All transactions
@router.get("/transactions/")
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

# GET: Transactions by customer ID
@router.get("/transactions/customer/{customer_id}")
def get_transactions_by_customer(customer_id: int, db: Session = Depends(get_db)):
    txns = db.query(Transaction).filter(Transaction.customer_id == customer_id).all()
    if not txns:
        raise HTTPException(status_code=404, detail="No transactions found for this customer")
    return txns
