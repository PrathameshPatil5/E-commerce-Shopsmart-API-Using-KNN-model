from fastapi import APIRouter, HTTPException
import pickle
import pandas as pd

router = APIRouter()

# Load model and user-item matrix only once
with open("knn_model.pkl", "rb") as f:
    knn_model = pickle.load(f)

user_item_matrix = pd.read_pickle("user_item_matrix.pkl")

@router.get("/recommendations/{customer_id}")
def get_recommendations(customer_id: int, k: int = 5):
    if customer_id not in user_item_matrix.index:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_vector = user_item_matrix.loc[customer_id].values.reshape(1, -1)
    distances, indices = knn_model.kneighbors(customer_vector, n_neighbors=k+1)

    similar_customer_ids = user_item_matrix.index[indices.flatten()[1:]]  # skip self

    # Products already bought by target customer
    target_products = set(user_item_matrix.loc[customer_id][user_item_matrix.loc[customer_id] > 0].index)

    # Collect products bought by similar customers
    recommended = set()
    for neighbor_id in similar_customer_ids:
        neighbor_products = user_item_matrix.loc[neighbor_id]
        neighbor_buys = set(neighbor_products[neighbor_products > 0].index)
        recommended.update(neighbor_buys - target_products)

    if not recommended:
        return {"message": "No new recommendations for this customer"}

    return {"recommended_product_ids": list(recommended)}
