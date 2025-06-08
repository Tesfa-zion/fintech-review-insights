
import pandas as pd
from transformers import pipeline

# Load cleaned reviews
df = pd.read_csv("data/processed/fintech_reviews_clean.csv")

# Load HuggingFace DistilBERT sentiment model
print("Loading model...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Apply sentiment analysis
print("Classifying sentiment...")
df['sentiment'] = df['review_text'].astype(str).apply(lambda x: classifier(x[:512])[0]['label'].lower())

# Map label to numeric score for aggregation
sentiment_to_score = {'positive': 1, 'neutral': 0, 'negative': -1}
df['sentiment_score'] = df['sentiment'].map(sentiment_to_score)

# Save full labeled dataset
output_file = "data/processed/fintech_reviews_with_sentiment.csv"
df.to_csv(output_file, index=False)
print(f"✅ Sentiment data saved to {output_file}")

# ➕ Aggregate sentiment score by bank and rating
summary = df.groupby(['bank_name', 'rating'])['sentiment_score'].mean().reset_index()

# Save summary
summary_file = "data/processed/sentiment_summary_by_bank_and_rating.csv"
summary.to_csv(summary_file, index=False)
print(f"✅ Aggregated sentiment summary saved to {summary_file}")
print(summary)
