import polars as pl

# === CONFIG ===
INPUT_FILE = "D:/OPT Work/Task 4/2024_fb_posts_president_scored_anon.csv"

# === LOAD DATA ===
df = pl.read_csv(INPUT_FILE)
print("✅ Data loaded:", df.shape)

# === FUNCTION TO SUMMARIZE A POLARS DATAFRAME ===
def summarize_dataframe(df):
    summary = []

    for col in df.columns:
        col_data = df[col].drop_nulls()
        dtype = df.schema[col]

        entry = {
            "column": col,
            "count": col_data.len(),
            "mean": col_data.mean() if dtype in [pl.Float64, pl.Float32, pl.Int64, pl.Int32] else None,
            "min": col_data.min() if dtype in [pl.Float64, pl.Float32, pl.Int64, pl.Int32] else None,
            "max": col_data.max() if dtype in [pl.Float64, pl.Float32, pl.Int64, pl.Int32] else None,
            "std_dev": col_data.std() if dtype in [pl.Float64, pl.Float32, pl.Int64, pl.Int32] else None,
            "unique_values": col_data.n_unique(),
            "most_frequent": col_data.mode().to_list()[0] if col_data.len() > 0 and col_data.mode().len() > 0 else None,
        }
        summary.append(entry)

    return pl.DataFrame(summary)

# === OVERALL SUMMARY ===
print("\n📊 === OVERALL SUMMARY ===")
overall_summary_df = summarize_dataframe(df)
print(overall_summary_df)

# === GROUPED BY Facebook_Id (First 3) ===
print("\n📊 === GROUPED BY Facebook_Id (First 3 Samples) ===")
if "Facebook_Id" in df.columns:
    unique_fb_ids = df.select("Facebook_Id").unique().head(3)["Facebook_Id"].to_list()
    for i, fb_id in enumerate(unique_fb_ids):
        group_df = df.filter(pl.col("Facebook_Id") == fb_id)
        print(f"\n🧵 Group {i+1}: Facebook_Id = {fb_id}")
        print(summarize_dataframe(group_df))

# === GROUPED BY (Facebook_Id, post_id) (First 3) ===
print("\n📊 === GROUPED BY (Facebook_Id, post_id) (First 3 Samples) ===")
if {"Facebook_Id", "post_id"}.issubset(df.columns):
    unique_pairs = df.select(["Facebook_Id", "post_id"]).unique().head(3).rows()
    for i, (fb_id, post_id) in enumerate(unique_pairs):
        group_df = df.filter((pl.col("Facebook_Id") == fb_id) & (pl.col("post_id") == post_id))
        print(f"\n🧵 Group {i+1}: Facebook_Id = {fb_id}, post_id = {post_id}")
        print(summarize_dataframe(group_df))
