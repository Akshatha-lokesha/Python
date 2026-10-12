# records = [
#     {"order_id": 3001, "amount": 500.0,  "status": "VALID"},
#     {"order_id": 3002, "amount": -50.0,  "status": "FAILED"},
#     {"order_id": 3003, "amount": 820.0,  "status": "VALID"},
#     {"order_id": 3004, "amount": 0.0,    "status": "VALID"},
#     {"order_id": 3005, "amount": 1200.0, "status": "COMPLETED"},
# ]

# Use map() + lambda to floor all negative amounts to 0.0
# Use filter() + lambda to keep only records where amount > 0
# Sort the filtered results by amount descending using sorted() + lambda
# Print each result in this format: Order 3005 | Rs. 1200.0 | COMPLETED

# Written as clean Python. Docstrings on functions if you write any.

records = [
    {"order_id": 3001, "amount": 500.0,  "status": "VALID"},
    {"order_id": 3002, "amount": -50.0,  "status": "FAILED"},
    {"order_id": 3003, "amount": 820.0,  "status": "VALID"},
    {"order_id": 3004, "amount": 0.0,    "status": "VALID"},
    {"order_id": 3005, "amount": 1200.0, "status": "COMPLETED"},
]

floor_negatives = list(map(lambda x: {**x, "amount": max(x["amount"], 0.0)}, records))
print(floor_negatives)

filtered_amt = list(filter(lambda x: x["amount"] > 0, floor_negatives))
print(filtered_amt)

sorted_amt = sorted(filtered_amt, key= lambda x: x["amount"], reverse= True)
print(sorted_amt)

for val in sorted_amt:
    print(f"Order {val['order_id']} | Rs. {val['amount']:<7} | {val['status']}")