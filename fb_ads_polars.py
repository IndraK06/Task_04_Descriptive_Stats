import polars as pl

# === Load dataset ===
file_path = r'D:\OPT Work\Task 4\2024_fb_ads_president_scored_anon.csv'
df = pl.read_csv(file_path)

# === Function: Describe a DataFrame ===
def describe_dataframe(df):
    numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Float64, pl.Int64]]
    non_numeric_cols = [col for col in df.columns if df[col].dtype == pl.Utf8]

    # Numeric stats
    numeric_stats = {}
    for col in numeric_cols:
        numeric_stats[col] = {
            "count": df[col].drop_nulls().len(),
            "mean": df[col].mean(),
            "min": df[col].min(),
            "max": df[col].max(),
            "stddev": df[col].std()
        }

    # Non-numeric stats
    non_numeric_stats = {}
    for col in non_numeric_cols:
        mode_result = (
            df.group_by(col)
            .agg(pl.count(col).alias("count"))
            .sort("count", descending=True)
        )
        most_freq = tuple(mode_result.row(0)) if mode_result.height > 0 else None
        non_numeric_stats[col] = {
            "count": df[col].drop_nulls().len(),
            "unique_values": df[col].n_unique(),
            "most_frequent": most_freq
        }

    return numeric_stats, non_numeric_stats

# === Function: Print stats ===
def print_stats(title, numeric_stats, non_numeric_stats):
    print(f"\n===== {title} =====")
    for col, stats in numeric_stats.items():
        print(f"\nColumn: {col}")
        print(f"  count: {stats['count']}")
        print(f"  mean: {stats['mean']}")
        print(f"  min: {stats['min']}")
        print(f"  max: {stats['max']}")
        print(f"  stddev: {stats['stddev']}")
        print(f"  unique_values: 0")
        print(f"  most_frequent: None")

    for col, stats in non_numeric_stats.items():
        print(f"\nColumn: {col}")
        print(f"  count: {stats['count']}")
        print(f"  unique_values: {stats['unique_values']}")
        print(f"  most_frequent: {stats['most_frequent']}")

# === Confirm data loaded ===
print(f"\n✅ Loaded {df.height} rows")
print(df.head(3))

# === Run: Overall stats ===
overall_numeric, overall_non_numeric = describe_dataframe(df)
print_stats("Overall Dataset", overall_numeric, overall_non_numeric)

# === Group by page_id (first 2 values) ===
unique_page_ids = df.select("page_id").unique().limit(2).to_series().to_list()
for page_id in unique_page_ids:
    group = df.filter(pl.col("page_id") == page_id)
    numeric, non_numeric = describe_dataframe(group)
    print_stats(f"Group by page_id = {page_id}", numeric, non_numeric)

# === Group by (page_id, ad_id) (first 2 values) ===
unique_page_ad = df.select(["page_id", "ad_id"]).unique().limit(2).rows()
for page_id, ad_id in unique_page_ad:
    group = df.filter((pl.col("page_id") == page_id) & (pl.col("ad_id") == ad_id))
    numeric, non_numeric = describe_dataframe(group)
    print_stats(f"Group by (page_id, ad_id) = ({page_id}, {ad_id})", numeric, non_numeric)
