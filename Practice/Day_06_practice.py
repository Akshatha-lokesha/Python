# Create day6_csv.py in c:\Data Engineering\Python\. Write code that:

# Reads raw_orders.csv using csv.DictReader
# Calls clean_record() on every row (with type conversion)
# Calls is_valid() on every cleaned row
# Prints:

# Loaded: 10 records
# Valid  : X
# Invalid: X

import csv
import mysql.connector


def sqlConnector():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your_PassWord",    # replace with your actual password
        database="de_learning"
    )

def clean_record(record):
    return {"order_id" : int(record["order_id"]),
            "amount" : max(float(record["amount"]), 0.0),
            "status" : record["status"].strip().upper(),
            "currency" : record["currency"].strip().upper(),
            "customer_id" : int(record["customer_id"])
    }

def is_valid(record):
    return record["amount"] > 0 and record["status"] in ("VALID", "COMPLETED")

def csv_reader(filePath):
    valid_records = []
    invalid_records = []

    conn = sqlConnector()
    curr = conn.cursor()

    with open(filePath, 'r', encoding= 'utf-8') as f:
        raw_records = csv.DictReader(f)
        sql_query = """ INSERT INTO orders (order_id, amount, status, currency, customer_id) VALUES (%s, %s, %s, %s, %s) """

        for rec in raw_records:
            cleaned_rec = clean_record(rec)
            if is_valid(cleaned_rec):
                values = (
                    cleaned_rec["order_id"],
                    cleaned_rec["amount"],
                    cleaned_rec["status"],
                    cleaned_rec["currency"],
                    cleaned_rec["customer_id"]
                )
                # Values sent to execute the sql query are always supposed to be a tuple
                curr.execute(sql_query, values)
                valid_records.append(cleaned_rec)
            else:
                invalid_records.append(cleaned_rec)

        conn.commit()

        curr.close()
        conn.close()

    return valid_records, invalid_records


valid_records, invalid_records = csv_reader("../CSV_Files/raw_orders.csv")

print(f"Loaded  : {len(valid_records) + len(invalid_records)} records")
print(f"Valid   : {len(valid_records)}")
print(f"Invalid : {len(invalid_records)}")

# DSA
# # Trace this manually (no running):
# nums   = [1, 5, 3, 7, 2]
# target = 8
# Trace through two_sum(nums, target) step by step — show seen dict at every iteration
# What does the function return?
# What would brute force do for this same input? How many total comparisons?

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed_sum = target - num

        if needed_sum in seen:
            return [seen[needed_sum], i]
        
        seen[num] = i

two_sum([1, 5, 3, 7, 2], 8)

# tracing manually:
# on call of the func - two_sum([1, 5, 3, 7, 2], 8)
# seen = {}
# on iteration - 
# index = 0 , num = 1
# needed_sum = 8-1 which is 7
# checks if 7 is in seen - not there
# so the num 1 gets added to the dict with it's index
# seen = {1:0}
# index = 1 , num = 5
# needed_sum = 8-5 which is 3
# checks if 3 is in seen - not there
# so the num 5 gets added to the dict with it's index
# seen = {1:0, 5:1}
# index = 2 , num = 3
# needed_sum = 8-3 which is 5
# checks if 5 is in seen - it's there
# now it'll return return [seen[needed_sum], i] which is return [seen[5], 2]
# which is [1,2]
# brute force would compare it multiple times - O(N**2) that is 5**2 = 25 times 
