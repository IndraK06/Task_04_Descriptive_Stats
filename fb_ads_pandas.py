import pandas as pd

# === Load dataset ===
file_path = r'D:\OPT Work\Task 4\2024_fb_ads_president_scored_anon.csv'
df = pd.read_csv(file_path)

# === Function: Describe a DataFrame ===
def describe_dataframe(df):
    numeric_stats = df.describe(include='number').T

    non_numeric_stats = {}
    for col in df.select_dtypes(include='object').columns:
        mode = df[col].mode()
        most_freq = (
            (mode.iloc[0], (df[col] == mode.iloc[0]).sum())
            if not mode.empty else None
        )
        non_numeric_stats[col] = {
            'count': df[col].count(),
            'unique_values': df[col].nunique(),
            'most_frequent': most_freq
        }

    return numeric_stats, non_numeric_stats

# === Function: Print stats nicely ===
def print_stats(title, numeric_stats, non_numeric_stats):
    print(f"\n===== {title} =====")
    for col, stats in numeric_stats.iterrows():
        print(f"\nColumn: {col}")
        print(f"  count: {stats['count']}")
        print(f"  mean: {stats['mean']}")
        print(f"  min: {stats['min']}")
        print(f"  max: {stats['max']}")
        print(f"  stddev: {stats['std']}")
        print(f"  unique_values: 0")
        print(f"  most_frequent: None")

    for col, stats in non_numeric_stats.items():
        print(f"\nColumn: {col}")
        print(f"  count: {stats['count']}")
        print(f"  unique_values: {stats['unique_values']}")
        print(f"  most_frequent: {stats['most_frequent']}")

# === Confirm data loaded ===
print(f"\n✅ Loaded {len(df)} rows")
print(df.head(3))  # preview to verify structure

# === Run: Overall stats ===
overall_numeric, overall_non_numeric = describe_dataframe(df)
print_stats("Overall Dataset", overall_numeric, overall_non_numeric)

# === Run: Group by page_id ===
grouped_by_page = df.groupby('page_id')
for name, group in list(grouped_by_page)[:2]:  # First 2 groups
    numeric, non_numeric = describe_dataframe(group)
    print_stats(f"Group by page_id = {name}", numeric, non_numeric)

# === Run: Group by (page_id, ad_id) ===
grouped_by_page_ad = df.groupby(['page_id', 'ad_id'])
for name, group in list(grouped_by_page_ad)[:2]:  # First 2 groups
    numeric, non_numeric = describe_dataframe(group)
    print_stats(f"Group by (page_id, ad_id) = {name}", numeric, non_numeric)
