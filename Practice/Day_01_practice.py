# Exercise 1 — String Cleaning Pipeline: You receive this raw CSV line from a dirty data source:

# "   AKSHAY KUMAR   ", "  akshay@email.com  ", "  ACTIVE   "
# Write a Python script that:

# Stores this as 3 separate raw string variables
# Cleans each one (strip whitespace, lowercase everything)
# Prints the cleaned output

raw_data_name = "   AKSHAY KUMAR   "
raw_data_email = "  akshay@email.com  "
raw_data_status = "  ACTIVE   "

cleaned_raw_data_name = raw_data_name.strip().lower()
cleaned_raw_data_email = raw_data_email.strip().lower()
cleaned_raw_data_status = raw_data_status.strip().lower()

print(f"Cleaned Name: {cleaned_raw_data_name} \n Cleaned Email: {cleaned_raw_data_email} \n Cleaned Status: {cleaned_raw_data_status}")

#  Dictionary Operations: You have an order record:

# {"order_id": 2001, "amount": 850.0}
# Write code that:

# Safely gets the "discount" key, defaulting to 0.0 if missing
# Adds a "tax" key with value 153.0 (18% of 850)
# Updates "amount" to the final value: amount + tax - discount
# Prints the full updated order

ordered_record = {"order_id": 2001, "amount": 850.0}
print(ordered_record.get("discount", 0.0))
print(ordered_record.setdefault("tax", 153.0))
final_val = ordered_record["amount"] + ordered_record["tax"] - ordered_record.get("discount", 0.0)
print(final_val)
print(ordered_record.update({"amount": final_val}))
print(ordered_record)

# Set Deduplication: You have two raw lists from two separate API calls for the same day's active users:

# morning_batch  = [1, 2, 3, 4, 5, 3, 2]
# evening_batch  = [4, 5, 6, 7, 8, 5, 4]
# Write code that finds:

# The total unique users across both batches combined
# Users who were active in BOTH batches (the overlap)
# Users only in the morning batch (not in evening)

morning_batch  = [1, 2, 3, 4, 5, 3, 2]
evening_batch  = [4, 5, 6, 7, 8, 5, 4]

set_morning_batch  = set(morning_batch)
set_evening_batch  = set(evening_batch)

print(f"The total unique users across both batches combined {set_morning_batch | set_evening_batch}")
print(f"Users who were active in BOTH batches (the overlap {set_morning_batch & set_evening_batch})")
print(f"Users only in the morning batch (not in evening) {set_morning_batch - set_evening_batch}")

def run_pipeline(records):
    total = len(records)
    errors = [r for r in records if r["status"] == "ERROR"]
    success = total - len(errors)
    return(total, len(errors), success)
    # YOUR CODE: return total, success, and error count as a TUPLE

sample = [
    {"id": 1, "status": "OK"},
    {"id": 2, "status": "ERROR"},
    {"id": 3, "status": "OK"},
    {"id": 4, "status": "ERROR"},
    {"id": 5, "status": "OK"},
]
Total, Error, Success = run_pipeline(sample)
print(f"Total : {Total} | Success: {Success} | Errors: {Error}")
# YOUR CODE: call run_pipeline and unpack the result into 3 variables
# Then print: "Total: X | Success: Y | Errors: Z"