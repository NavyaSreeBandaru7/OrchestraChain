import pandas as pd

def get_inventory_impact(sku_id: str, delay_days: int) -> dict:
    df = pd.read_csv("data/inventory_db.csv")
    sku_data = df[df["sku_id"] == sku_id]
    
    if sku_data.empty:
        return {"error": "SKU not found"}
    
    row = sku_data.iloc[0]
    penalty_per_day = float(row["unit_delay_penalty"])
    total_penalty = penalty_per_day * delay_days
    
    return {
        "sku_id": sku_id,
        "product_name": row["product_name"],
        "current_stock": int(row["current_stock"]),
        "delay_days": delay_days,
        "total_penalty_usd": total_penalty
    }
