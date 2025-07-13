import pandas as pd

# === CONFIG ===
INPUT_FILE = "D:/OPT Work/Task 4/2024_fb_posts_president_scored_anon.csv"

# === LOAD DATA ===
df = pd.read_csv(INPUT_FILE)
print("✅ Data loaded:", df.shape)

# === FUNCTION TO SUMMARIZE A DATAFRAME ===
def summarize_dataframe(df):
    summary = []

    for col in df.columns:
        col_data = df[col].dropna()
        entry = {
            "column": col,
            "count": col_data.count(),
            "mean": col_data.mean() if pd.api.types.is_numeric_dtype(col_data) else None,
            "min": col_data.min() if pd.api.types.is_numeric_dtype(col_data) else None,
            "max": col_data.max() if pd.api.types.is_numeric_dtype(col_data) else None,
            "std_dev": col_data.std() if pd.api.types.is_numeric_dtype(col_data) else None,
            "unique_values": col_data.nunique(),
            "most_frequent": col_data.mode().iloc[0] if not col_data.mode().empty else None,
        }
        summary.append(entry)

    return pd.DataFrame(summary)

# === OVERALL SUMMARY ===
print("\n📊 === OVERALL SUMMARY ===")
overall_summary_df = summarize_dataframe(df)
print(overall_summary_df.to_string(index=False))

# === GROUPED BY Facebook_Id (First 3 Only) ===
print("\n📊 === GROUPED BY Facebook_Id (First 3 Samples) ===")
grouped_fb = df.groupby("Facebook_Id")
for i, (fb_id, group_df) in enumerate(grouped_fb):
    print(f"\n🧵 Group {i+1}: Facebook_Id = {fb_id}")
    print(summarize_dataframe(group_df).to_string(index=False))
    if i == 2:
        break

# === GROUPED BY (Facebook_Id, post_id) (First 3 Only) ===
print("\n📊 === GROUPED BY (Facebook_Id, post_id) (First 3 Samples) ===")
grouped_fb_post = df.groupby(["Facebook_Id", "post_id"])
for i, ((fb_id, post_id), group_df) in enumerate(grouped_fb_post):
    print(f"\n🧵 Group {i+1}: Facebook_Id = {fb_id}, post_id = {post_id}")
    print(summarize_dataframe(group_df).to_string(index=False))
    if i == 2:
        break
