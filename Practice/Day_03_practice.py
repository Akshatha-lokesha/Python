# Write the Code

# records = [
#     {"order_id": 1001, "amount": 499.95,  "currency": "inr"},
#     {"order_id": 1002, "amount": -50.00,  "currency": "USD"},
#     {"order_id": 1003, "amount": 820.00,  "currency": "  gbp  "},
#     {"order_id": 1004, "amount": 0.0,     "currency": "INR"},
#     {"order_id": 1005, "amount": 1200.00, "currency": "usd"},
# ]
# Write two functions:

# def clean_record(record) — returns a new dict with:

# amount replaced with 0.0 if it is negative
# currency stripped of whitespace and uppercased
# def is_valid(record) — returns True if amount > 0

# Then write a loop that calls both functions on every record and prints:



# Order 1001 | Amount: 499.95 | Currency: INR | Valid: True
# Order 1002 | Amount: 0.0    | Currency: USD | Valid: False
# ...
# Write and run in VS Code. Share your code.

records = [
    {"order_id": 1001, "amount": 499.95,  "currency": "inr"},
    {"order_id": 1002, "amount": -50.00,  "currency": "USD"},
    {"order_id": 1003, "amount": 820.00,  "currency": "  gbp  "},
    {"order_id": 1004, "amount": 0.0,     "currency": "INR"},
    {"order_id": 1005, "amount": 1200.00, "currency": "usd"},
]

def clean_record(record):
    return {
       "order_id" :  record["order_id"],
       "amount" : max(record["amount"], 0.0),
       "currency" : record["currency"].strip().upper()
    }

def is_valid(record):
    return record["amount"] > 0

for rec in records:
    cleaned = clean_record(rec)
    if is_valid(cleaned):
        print(f"Order {cleaned["order_id"]:<5} | Amount: {cleaned["amount"]:<8} | Currency: {cleaned["currency"]:<5} | Valid: True")
    else:
        print(f"Order {cleaned["order_id"]:<5} | Amount: {cleaned["amount"]:<8} | Currency: {cleaned["currency"]:<5} | Valid: False")

# DSA

# customer_ids = [101, 202, 303, 101, 404, 202, 505]
# Write contains_duplicate() using the seen = set() loop approach (no one-liner)
# Call it on customer_ids and print the result
# Then modify it to also print which IDs are duplicated (not just True/False)
# For part 3, the output should be:

# Duplicates found: {101, 202}

customer_ids = [101, 202, 303, 101, 404, 202, 505]

def contains_duplicate(ids):
    sets = set()
    duplicates = []
    for id in ids:
        if id in sets:
            duplicates.append(id)
        sets.add(id)
    return duplicates

result = contains_duplicate(customer_ids)
sorted_dup= sorted(result)
if result:
    print("Result is True")
    print(f"Duplicates found: {sorted_dup}")
else:
    print("Result is False")
    print("Duplicates not found")
