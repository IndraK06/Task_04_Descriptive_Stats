# Social Media Data Analysis of 2024 US Presidential Elections

This project analyzes Facebook and Twitter content related to the 2024 US Presidential elections using:

**Base Python**  
**Pandas**  
**Polars**

---

## 📊 Features

- Descriptive statistics: mean, std, min, max, count
- Grouped analysis by `page_id`, `Facebook_Id`, `month_year`, etc.
- Comparison of efficiency and usability across Base Python, Pandas, and Polars
- Lightweight data parsing and summarization with no external dependencies in Base Python

---

## 📈 Summary of Findings & Insights

Across all three datasets — Facebook Ads, Facebook Posts, and Twitter Posts — key engagement patterns and targeting strategies emerged. Facebook Ads data showed that certain political pages ran highly concentrated campaigns, particularly in states like Texas. Interestingly, some low-budget ads achieved disproportionately high engagement, while high-spend ads underperformed, pointing to issues in creative effectiveness or audience targeting.

For Facebook Posts, posts containing rich media (images or videos) consistently received more interactions. Engagement patterns peaked mid-week (Tuesday to Thursday), with noticeable drops on weekends, suggesting the timing of content release plays a significant role in audience reach. A few pages posted repetitively with similar content, hinting at automated or templated campaign strategies.

In the Twitter dataset, the majority of tweets received modest interaction (<500 likes or retweets), with only a small subset going viral — often those tied to major events or figures. Engagement metrics like likes, views, and retweets showed high variability, reinforcing the unpredictable nature of virality on social platforms. Cleaning null-heavy columns (like `quoteId` and `inReplyToId`) helped simplify analysis and improve clarity.

Overall, timing, content type, and regional focus were strong indicators of post/ad effectiveness, while performance varied sharply between high-cost and high-engagement content. Pandas offered ease of use and flexibility for exploratory work, while Polars delivered faster performance with a bit more complexity. Base Python, though dependency-free, lacked scalability for large datasets.

---

## 🧠 Lessons Learned

- Polars lacks `is_numeric_dtype`; manual type checking is needed.
- Dropping null-heavy fields early (like `quoteId`, `inReplyToId`) simplifies analysis.
- Proper datetime handling is essential for accurate temporal insights.

---

## 🧪 Requirements

When using Pandas or Polars versions, use below commands to install both the libraries:

pip install pandas

pip install polars

## ▶️ How to Run the Code

The development, testing of the code and the subsequent analysis was done using Visual Studio Code. The code files can be run independently as well using terminal or another IDE.
