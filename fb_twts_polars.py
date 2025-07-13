import polars as pl

CSV_FILE = "D:/OPT Work/Task 4/2024_tw_posts_president_scored_anon.csv"  # Adjust path if needed

def print_overall_stats(df):
    print("\n=== Overall Numeric Summary ===")
    print(df.describe())

    print("\n=== Overall Non-Numeric Summary ===")
    for col in df.columns:
        if df[col].dtype in [pl.Utf8, pl.Boolean]:
            unique_count = df[col].n_unique()
            top = df[col].value_counts().sort("count", descending=True).row(0)
            print(f"\nColumn: {col}")
            print(f"  Unique Values: {unique_count}")
            print(f"  Most Frequent: {top[0]} ({top[1]})")

def print_grouped_stats(df, group_col):
    unique_vals = df[group_col].unique().to_list()
    for group_value in unique_vals:
        group_df = df.filter(pl.col(group_col) == group_value)
        print(f"\n=== Grouped by {group_col} = {group_value} ===")

        print("\n--- Numeric Columns ---")
        print(group_df.describe())

        print("\n--- Non-Numeric Columns ---")
        for col in group_df.columns:
            if group_df[col].dtype in [pl.Utf8, pl.Boolean]:
                unique_count = group_df[col].n_unique()
                top = group_df[col].value_counts().sort("count", descending=True).row(0)
                print(f"\nColumn: {col}")
                print(f"  Unique Values: {unique_count}")
                print(f"  Most Frequent: {top[0]} ({top[1]})")

if __name__ == "__main__":
    df = pl.read_csv(CSV_FILE)

    # Optional: Clean column names
    df = df.rename({col: col.strip() for col in df.columns})

    # Overall stats
    print_overall_stats(df)

    # Grouped stats
    if 'source' in df.columns:
        print_grouped_stats(df, 'source')

    if 'month_year' in df.columns:
        print_grouped_stats(df, 'month_year')

