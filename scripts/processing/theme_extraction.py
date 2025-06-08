import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load sentiment-labeled data
df = pd.read_csv("data/processed/fintech_reviews_with_sentiment.csv")

# Set up stopwords
stop_words = stopwords.words('english')

# Define TF-IDF extractor
def extract_keywords_tfidf(texts, top_n=15):
    tfidf = TfidfVectorizer(stop_words=stop_words, max_df=0.85, ngram_range=(1,2))
    tfidf_matrix = tfidf.fit_transform(texts)
    scores = zip(tfidf.get_feature_names_out(), tfidf_matrix.sum(axis=0).tolist()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return [kw for kw, score in sorted_scores[:top_n]]

# Define rule-based theme grouping
def map_keywords_to_themes(keywords):
    themes = {
        'Account Access Issues': ['login', 'password', 'authentication', 'account lock'],
        'Transaction Performance': ['transfer', 'delay', 'failed', 'slow', 'load'],
        'User Interface & Experience': ['ui', 'interface', 'design', 'navigation'],
        'Customer Support': ['support', 'help', 'response', 'call center'],
        'Feature Requests': ['add feature', 'biometric', 'notification', 'statement'],
    }
    result = set()
    for theme, words in themes.items():
        for kw in keywords:
            if any(w in kw for w in words):
                result.add(theme)
    return list(result) if result else ['Uncategorized']

# Extract themes per bank
bank_theme_summary = []
for bank in df['bank_name'].unique():
    bank_reviews = df[df['bank_name'] == bank]['review_text'].dropna().tolist()
    keywords = extract_keywords_tfidf(bank_reviews)
    themes = map_keywords_to_themes(keywords)
    bank_theme_summary.append({'bank': bank, 'keywords': keywords, 'themes': themes})

# Print results
for row in bank_theme_summary:
    print(f"\n🔍 {row['bank']}")
    print("Top Keywords:", ", ".join(row['keywords']))
    print("Themes:", ", ".join(row['themes']))

# Save result
summary_df = pd.DataFrame(bank_theme_summary)
summary_df.to_csv("data/processed/theme_summary_by_bank.csv", index=False)
print("✅ Saved theme summary to data/processed/theme_summary_by_bank.csv")
