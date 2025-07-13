import csv
from collections import defaultdict, Counter
from statistics import mean, stdev

# Utility functions
def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def summarize_column(col_data):
    numeric_data = [float(x) for x in col_data if is_float(x)]
    non_numeric_data = [x for x in col_data if not is_float(x)]

    summary = {
        "count": len(col_data),
        "mean": mean(numeric_data) if numeric_data else None,
        "min": min(numeric_data) if numeric_data else None,
        "max": max(numeric_data) if numeric_data else None,
        "std_dev": stdev(numeric_data) if len(numeric_data) > 1 else None,
        "unique_values": len(set(non_numeric_data)) if non_numeric_data else None,
        "most_frequent": Counter(non_numeric_data).most_common(1)[0] if non_numeric_data else None,
    }
    return summary

def group_by(rows, headers, group_keys):
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row[headers.index(k)] for k in group_keys)
        grouped[key].append(row)
    return grouped

def grouped_summaries(data, headers, group_keys):
    grouped = group_by(data, headers, group_keys)
    summaries = {}
    for key, group_rows in grouped.items():
        group_columns = {h: [] for h in headers}
        for row in group_rows:
            for i, value in enumerate(row):
                group_columns[headers[i]].append(value)
        summaries[key] = {col: summarize_column(values) for col, values in group_columns.items()}
    return summaries

# === MAIN EXECUTION ===

# Replace this with your actual file path
file_path = "D:/OPT Work/Task 4/2024_fb_posts_president_scored_anon.csv"

# Load data
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = list(csv.reader(csvfile))
    headers = reader[0]
    data = reader[1:]

# Overall column-wise summary
columns = {h: [] for h in headers}
for row in data:
    for i, value in enumerate(row):
        columns[headers[i]].append(value)

overall_summary = {col: summarize_column(values) for col, values in columns.items()}

# Print overall summary
print("\n=== OVERALL SUMMARY ===")
for col, stats in overall_summary.items():
    print(f"\nColumn: {col}")
    for k, v in stats.items():
        print(f"  {k}: {v}")

# Grouped by Facebook_Id
grouped_fb = grouped_summaries(data, headers, ["Facebook_Id"])
print("\n=== GROUPED BY Facebook_Id (Sample) ===")
for key, col_stats in list(grouped_fb.items())[:5]:
    print(f"\nGroup: {key}")
    for col, stats in col_stats.items():
        print(f"  {col}: {stats}")

# Grouped by (Facebook_Id, post_id)
grouped_fb_post = grouped_summaries(data, headers, ["Facebook_Id", "post_id"])
print("\n=== GROUPED BY (Facebook_Id, post_id) (Sample) ===")
for key, col_stats in list(grouped_fb_post.items())[:5]:
    print(f"\nGroup: {key}")
    for col, stats in col_stats.items():
        print(f"  {col}: {stats}")
