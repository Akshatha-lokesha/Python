# Exercise: You receive a list of pipeline run records:

# runs = [
#     {"run_id": 1, "status": "SUCCESS", "rows": 50000,  "duration_sec": 45},
#     {"run_id": 2, "status": "FAILED",  "rows": 0,      "duration_sec": 3},
#     {"run_id": 3, "status": "SUCCESS", "rows": 48500,  "duration_sec": 47},
#     {"run_id": 4, "status": "SUCCESS", "rows": 51200,  "duration_sec": 44},
#     {"run_id": 5, "status": "FAILED",  "rows": 0,      "duration_sec": 2},
# ]
# Write a loop that:

# Skips any run where rows == 0 using continue
# For successful runs, prints: "Run 1: 50,000 rows in 45s"
# After the loop, prints the total rows processed across all successful runs

runs = [
    {"run_id": 1, "status": "SUCCESS", "rows": 50000,  "duration_sec": 45},
    {"run_id": 2, "status": "FAILED",  "rows": 0,      "duration_sec": 3},
    {"run_id": 3, "status": "SUCCESS", "rows": 48500,  "duration_sec": 47},
    {"run_id": 4, "status": "SUCCESS", "rows": 51200,  "duration_sec": 44},
    {"run_id": 5, "status": "FAILED",  "rows": 0,      "duration_sec": 2},
]

total_successful_rows = 0

for run in runs:
    if(run['rows'] == 0):
        continue
    else:
        total_successful_rows += run['rows']
        print(f"Run {run['run_id']}: {run['rows']:,} rows in {run['duration_sec']}s")

print(f"Total rows processed across all successful runs: {total_successful_rows:,}")

# Your DSA Exercise

# log_lines = [
#     "2026-09-25 01:00:01 INFO  Pipeline started",
#     "2026-09-25 01:05:22 ERROR Connection timeout",
#     "2026-09-25 01:10:45 INFO  Batch 1 loaded",
#     "2026-09-25 01:15:03 WARN  Slow query detected",
#     "2026-09-25 01:20:11 ERROR Schema mismatch",
#     "2026-09-25 01:25:30 INFO  Batch 2 loaded",
#     "2026-09-25 01:30:05 ERROR Disk space low",
#     "2026-09-25 01:35:44 INFO  Batch 3 loaded",
#     "2026-09-25 01:40:01 WARN  Memory pressure",
#     "2026-09-25 01:45:15 INFO  Pipeline completed",
# ]
# Write a frequency counter that:

# Extracts just the log level from each line (INFO, ERROR, WARN)
# Counts how many times each level appears
# Prints them in sorted order by count (highest first)
# Hint: line.split() will split on spaces. The log level is at split()[2]. No other hints

log_lines = [
    "2026-09-25 01:05:22 ERROR Connection timeout",
    "2026-09-25 01:00:01 INFO  Pipeline started",
    "2026-09-25 01:10:45 INFO  Batch 1 loaded",
    "2026-09-25 01:15:03 WARN  Slow query detected",
    "2026-09-25 01:20:11 ERROR Schema mismatch",
    "2026-09-25 01:25:30 INFO  Batch 2 loaded",
    "2026-09-25 01:30:05 ERROR Disk space low",
    "2026-09-25 01:35:44 INFO  Batch 3 loaded",
    "2026-09-25 01:40:01 WARN  Memory pressure",
    "2026-09-25 01:45:15 INFO  Pipeline completed",
]

frequency = {}

for log_line in log_lines:
    status = log_line.split()[2]
    frequency[status] = frequency.get(status, 0)+1

sorted_fq = dict(sorted(frequency.items(), key= lambda x:x[1], reverse= True))

print(f"Frequency Sorted Order:")

for key, val in sorted_fq.items():
    print(f"{key:12} : {val}")