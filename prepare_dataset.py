from models.customer import Customer
from models.product import Product
from models.transaction import Transaction
from db import SessionLocal
import pandas as pd
from db import engine

db=SessionLocal() #we dont directly use sessionlocal.query cause SessionLocal is a factory, not an actual session. so we create here instance

result =db.query(Transaction,Customer,Product).join(Customer,Transaction.customer_id==Customer.customer_id).join(Product,Transaction.product_id==Product.product_id).all()


data=[]

for txn,cust,prod in result:
    data.append({
        "transaction_id":txn.transaction_id,
        "customer_id":cust.customer_id,
        "customer_name":cust.name,
        "product_id":prod.product_id,
        "product_name":prod.name,
        "purchase_date":txn.purchase_date

    })

df=pd.DataFrame(data)
df.to_csv("transaction_dataset.csv",index=False) #here index become false cause in dataset it takes one column so when we preprocess we have to remove it so double work

#CREATE A PIVOT TABLE 
#A pivot table is a way to reshape a DataFrame — it's like turning your raw data into a structured grid.
#It helps you summarize or aggregate data across two dimensions: rows and columns.

#each rouw=customer each column= product
print(df.columns)
print(df.head())
user_item_matrix=df.pivot_table(
    index='customer_id',
    columns='product_id',
    aggfunc='size',  #basically here how many times the customer bought the product
    fill_value=0
)

#KNN MODEL BUILDING
from sklearn.neighbors import NearestNeighbors
import pickle

model=NearestNeighbors(metric='cosine',algorithm='brute')
model.fit(user_item_matrix)

with open('knn_model.pkl','wb') as f:
    pickle.dump(model,f)

user_item_matrix.to_pickle("user_item_matrix.pkl")

