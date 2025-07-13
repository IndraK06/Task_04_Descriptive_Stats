import csv
import math
from collections import defaultdict, Counter

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def compute_basic_stats(rows):
    stats = {}
    for col in rows[0].keys():
        values = [row[col] for row in rows]
        numeric_vals = [float(v) for v in values if is_number(v)]
        non_numeric_vals = [v for v in values if not is_number(v)]

        mean_val = sum(numeric_vals) / len(numeric_vals) if numeric_vals else None
        stddev = (
            math.sqrt(sum((x - mean_val) ** 2 for x in numeric_vals) / len(numeric_vals))
            if numeric_vals else None
        )

        col_stats = {
            'count': len(values),
            'mean': mean_val,
            'min': min(numeric_vals) if numeric_vals else None,
            'max': max(numeric_vals) if numeric_vals else None,
            'stddev': stddev,
            'unique_values': len(set(non_numeric_vals)) if non_numeric_vals else 0,
            'most_frequent': Counter(non_numeric_vals).most_common(1)[0] if non_numeric_vals else None
        }
        stats[col] = col_stats
    return stats

def group_by(rows, group_keys):
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row[k] for k in group_keys)
        grouped[key].append(row)
    return grouped

def print_stats(title, stats):
    print(f"\n===== {title} =====")
    for col, s in stats.items():
        print(f"\nColumn: {col}")
        for stat_name, val in s.items():
            print(f"  {stat_name}: {val}")

def main():
    file_path = r'D:\OPT Work\Task 4\2024_fb_ads_president_scored_anon.csv'
    print("Script started...")

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    print(f"\n✅ Total rows loaded: {len(data)}")
    if not data:
        print("⚠️ No data loaded. Check file path, encoding, or format.")
        return

    # Overall stats
    print_stats("Overall Dataset", compute_basic_stats(data))

    # Group by page_id
    page_groups = group_by(data, ['page_id'])
    for page_id, rows in list(page_groups.items())[:3]:  # show first 3 groups for brevity
        print_stats(f"Group by page_id = {page_id}", compute_basic_stats(rows))

    # Group by (page_id, ad_id)
    page_ad_groups = group_by(data, ['page_id', 'ad_id'])
    for group_key, rows in list(page_ad_groups.items())[:3]:
        print_stats(f"Group by (page_id, ad_id) = {group_key}", compute_basic_stats(rows))

if __name__ == "__main__":
    main()
