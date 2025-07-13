import pandas as pd

CSV_FILE = "D:/OPT Work/Task 4/2024_tw_posts_president_scored_anon.csv"  # Change if needed

def print_overall_stats(df):
    print("\n=== Overall Numeric Summary ===")
    print(df.describe().T.round(2))

    print("\n=== Overall Non-Numeric Summary ===")
    non_numeric_cols = df.select_dtypes(include=['object', 'bool']).columns
    for col in non_numeric_cols:
        print(f"\nColumn: {col}")
        print(f"  Unique Values: {df[col].nunique()}")
        top = df[col].value_counts(dropna=False).head(1)
        print(f"  Most Frequent: {top.index[0]} ({top.iloc[0]})")

def print_grouped_stats(df, group_col):
    grouped = df.groupby(group_col)
    for group, group_df in grouped:
        print(f"\n=== Grouped by {group_col} = {group} ===")
        
        print("\n--- Numeric Columns ---")
        print(group_df.describe().T.round(2))

        print("\n--- Non-Numeric Columns ---")
        non_numeric_cols = group_df.select_dtypes(include=['object', 'bool']).columns
        for col in non_numeric_cols:
            print(f"\nColumn: {col}")
            print(f"  Unique Values: {group_df[col].nunique()}")
            top = group_df[col].value_counts(dropna=False).head(1)
            print(f"  Most Frequent: {top.index[0]} ({top.iloc[0]})")

if __name__ == "__main__":
    df = pd.read_csv(CSV_FILE)

    # Clean column names (optional)
    df.columns = df.columns.str.strip()

    # Overall stats
    print_overall_stats(df)

    # Grouped stats
    if 'source' in df.columns:
        print_grouped_stats(df, 'source')

    if 'month_year' in df.columns:
        print_grouped_stats(df, 'month_year')
