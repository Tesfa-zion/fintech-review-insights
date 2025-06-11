t matplotlib.pyplot as plt
import seaborn as sns

# Load the processed reviews with sentiment
df = pd.read_csv("data/processed/fintech_reviews_with_sentiment.csv")

# Convert dates to datetime
df['review_date'] = pd.to_datetime(df['review_date'])

# === 1. Sentiment Distribution per Bank ===
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='bank_name', hue='sentiment_label', palette='Set2')
plt.title("Sentiment Distribution per Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("data/processed/plot_sentiment_distribution_per_bank.png")
plt.close()

# === 2. Average Sentiment by Rating ===
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='rating', y='sentiment_score', estimator='mean', ci=None, hue='bank_name')
plt.title("Average Sentiment Score by Star Rating")
plt.xlabel("Rating")
plt.ylabel("Avg Sentiment Score")
plt.tight_layout()
plt.savefig("data/processed/plot_avg_sentiment_by_rating.png")
plt.close()

# === 3. Sentiment Score Over Time (Line Plot) ===
plt.figure(figsize=(10, 6))
