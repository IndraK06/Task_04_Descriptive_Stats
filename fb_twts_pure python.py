import csv
from collections import defaultdict, Counter
from statistics import mean, stdev
from math import isnan

CSV_FILE = "D:/OPT Work/Task 4/2024_tw_posts_president_scored_anon.csv"  # change path if needed

# Utility
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def load_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def compute_stats(data):
    columns = data[0].keys()
    stats = {col: {'values': [], 'is_numeric': True} for col in columns}

    for row in data:
        for col in columns:
            val = row[col]
            if is_number(val):
                stats[col]['values'].append(float(val))
            else:
                stats[col]['values'].append(val)
                stats[col]['is_numeric'] = False

    summary = {}
    for col, info in stats.items():
        vals = info['values']
        summary[col] = {'count': len(vals)}
        if info['is_numeric']:
            nums = [v for v in vals if isinstance(v, float)]
            summary[col].update({
                'mean': round(mean(nums), 2) if nums else None,
                'min': min(nums) if nums else None,
                'max': max(nums) if nums else None,
                'stdev': round(stdev(nums), 2) if len(nums) > 1 else None
            })
        else:
            freq = Counter(vals)
            top = freq.most_common(1)
            summary[col].update({
                'unique_values': len(freq),
                'most_frequent': top[0] if top else None
            })
    return summary

def group_and_compute(data, group_by_col):
    grouped = defaultdict(list)
    for row in data:
        key = row[group_by_col]
        grouped[key].append(row)

    all_group_stats = {}
    for key, group_rows in grouped.items():
        all_group_stats[key] = compute_stats(group_rows)
    return all_group_stats

def print_summary(summary, title="Dataset Summary"):
    print(f"\n=== {title} ===")
    for col, stats in summary.items():
        print(f"\nColumn: {col}")
        for stat, val in stats.items():
            print(f"  {stat}: {val}")

# Main logic
if __name__ == "__main__":
    data = load_data(CSV_FILE)

    # Overall dataset stats
    overall_stats = compute_stats(data)
    print_summary(overall_stats, "Overall Dataset")

    # Group by source
    source_stats = group_and_compute(data, "source")
    for group, stats in source_stats.items():
        print_summary(stats, f"Grouped by Source = {group}")

    # Group by month_year
    if "month_year" in data[0]:
        month_stats = group_and_compute(data, "month_year")
        for group, stats in month_stats.items():
            print_summary(stats, f"Grouped by Month = {group}")
