# Create day6_csv.py in c:\Data Engineering\Python\. Write code that:

# Reads raw_orders.csv using csv.DictReader
# Calls clean_record() on every row (with type conversion)
# Calls is_valid() on every cleaned row
# Prints:

# Loaded: 10 records
# Valid  : X
# Invalid: X

import csv

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

    with open(filePath, 'r', encoding= 'utf-8') as f:
        raw_records = csv.DictReader(f)

        for rec in raw_records:
            cleaned_rec = clean_record(rec)
            if is_valid(cleaned_rec):
                valid_records.append(cleaned_rec)
            else:
                invalid_records.append(cleaned_rec)
    return valid_records, invalid_records


valid_records, invalid_records = csv_reader("../CSV_Files/raw_orders.csv")

print(f"Loaded  : {len(valid_records) + len(invalid_records)} records")
print(f"Valid   : {len(valid_records)}")
print(f"Invalid : {len(invalid_records)}")