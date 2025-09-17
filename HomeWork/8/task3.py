"""
Серіалізація списку товарів в інтернет-магазині.
"""

import pickle
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

products = [
    {"id": 1, "name": "Ноутбук", "price": 1200.0, "in_stock": True},
    {"id": 2, "name": "Смартфон", "price": 800.0, "in_stock": True},
    {"id": 3, "name": "Навушники", "price": 150.0, "in_stock": False},
    {"id": 4, "name": "Клавіатура", "price": 50.0, "in_stock": True},
]

pkl_path = os.path.join(BASE_DIR, "products.pkl")
json_path = os.path.join(BASE_DIR, "products.json")

with open(pkl_path, "wb") as pkl_file:
    pickle.dump(products, pkl_file)

with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=4)

print("Список товарів збережено у файли products.pkl та products.json")
