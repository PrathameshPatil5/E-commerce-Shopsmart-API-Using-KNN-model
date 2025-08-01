# E-commerce-Shopsmart-API-Using-KNN-model
# 🛒 ShoppersSmart API System - KNN Recommendation Model

A lightweight, FastAPI-powered backend system that provides product recommendations for an e-commerce platform using a K-Nearest Neighbors (KNN) machine learning model.

---

## 🚀 Features

✅ REST APIs for:
- Customer Management  
- Product Catalog  
- Purchase Transactions

✅ Machine Learning:
- Collaborative Filtering via KNN  
- Real-time recommendations based on purchase history  

✅ Data:
- SQLite database (ORM via SQLAlchemy)  
- Preprocessed user-item matrix with transaction logs

---

## 📦 Tech Stack

| Tool           | Purpose                        |
|----------------|--------------------------------|
| **FastAPI**    | Web Framework (REST APIs)      |
| **SQLite**     | Lightweight Database           |
| **SQLAlchemy** | ORM to handle DB models        |
| **Pandas**     | Data manipulation              |
| **scikit-learn** | ML Model (KNN for recommendation) |
| **Uvicorn**    | ASGI Server                    |

---

## 📸 Screenshots



## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://PrathameshPatil5/E-commerce-Shopsmart-API-Using-KNN-model.git
cd E-commerce-Shopsmart-API-Using-KNN-model
```

### 2. Create & Activate Environment
```base
conda create -n shoppersmart python=3.10
conda activate shoppersmart
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🧪 Run the App

### 1. Start the FastAPI Server
```bash
uvicorn main:app --reload
```
Visit: http://127.0.0.1:8000/docs to access Swagger UI

## 📊 Recommendation Model (KNN)

### Prepare dataset
```bash
python prepare_dataset.py
```
-Builds user-item matrix from transactions
-Trains KNN model
-Saves knn_model.pkl and user_item_matrix.pkl

### Populate Dummy Data (Optional)
```bash
python dummy_data_entry.py
```

## 🔎 Example API Endpoints

| Endpoint                         | Method | Description                   |
|----------------------------------|--------|-------------------------------|
| /customers/                      | GET    | Get all customers             |
| /customers/                      | POST   | Create a customer             |
| /products/                       | GET    | Get all products              |
| /transactions/                   | POST   | Create a transaction          |
| /recommendations/{customer_id}   | GET    | Get product recommendations   |

## 📁 Folder Structure

shoppersmart-api-knn/
├── main.py                         # FastAPI app entry point
├── db.py                           # Database engine, SessionLocal, Base
├── dummy_data_entry.py             # Script to generate dummy customer/product/transaction data
├── prepare_dataset.py              # Prepares user-item matrix & trains/saves KNN model
├── requirements.txt                # Python dependencies
├── shopsmart.db                    # SQLite database file (can be .gitignored)
├── knn_model.pkl                   # Pickled KNN model
├── user_item_matrix.pkl            # Saved user-item matrix for inference
├── transaction_dataset.csv         # Exported CSV of transaction history (for ML/data reuse)

├── models/                         # SQLAlchemy ORM models
│   ├── customer.py
│   ├── product.py
│   └── transaction.py

├── routes/                         # API route handlers (FastAPI routers)
│   ├── customer_routes.py
│   ├── product_routes.py
│   ├── transaction_routes.py
│   └── recommendation_routes.py

├── Schemas/                        # Pydantic models for request/response validation
│   └── schema.py

├── README.md                       # Project documentation (you’re working on this)
└── .gitignore                      # (optional) Ignore .db, __pycache__, .pkl files, etc.









