import pandas as pd
from transformers import pipeline

# Load cleaned data
df = pd.read_csv("data/fintech_reviews_clean.csv")

# Load sentiment pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Run sentiment analysis
df['sentiment'] = df['review_text'].astype(str).apply(lambda x: classifier(x[:512])[0]['label'].lower())

# Save result
df.to_csv("data/fintech_reviews_with_sentiment.csv", index=False)
print("✅ Sentiment analysis done.")
print(df['sentiment'].value_counts())
