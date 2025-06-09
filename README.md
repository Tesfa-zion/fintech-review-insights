# fintech-review-insights
Analyzing user reviews of Ethiopian fintech apps from Google Play Store
# 🎯 Task 2 – Sentiment and Thematic Analysis

This branch (`task-2`) implements sentiment classification and theme extraction on user reviews of three Ethiopian banking apps collected from the Google Play Store.

---

## ✅ Goals

- Label reviews with `positive`, `negative`, or `neutral` sentiments
- Compute sentiment scores per review
- Extract top keywords per bank using **TF-IDF**
- Group keywords into 3–5 themes (e.g., Transaction Performance, UI/UX)
- Save labeled and summarized results for downstream tasks

---

## 📁 Project Structure

| Path                             | Description                               |
|----------------------------------|-------------------------------------------|
| `data/processed/`                | Cleaned, labeled, and summarized datasets |
| `scripts/processing/`            | Python scripts for NLP analysis           |
| `requirements.txt`               | Python dependencies                       |

---

## 🧪 Scripts

- `sentiment_analysis.py`: Adds sentiment labels and scores using DistilBERT
- `theme_extraction.py`: Extracts top TF-IDF keywords and maps to custom themes

---

## 📊 Data Output

| File Name                                     | Description                                  |
|----------------------------------------------|----------------------------------------------|
| `fintech_reviews_with_sentiment.csv`         | All reviews labeled with sentiment & score   |
| `sentiment_summary_by_bank_and_rating.csv`   | Aggregated sentiment score per bank + rating |
| `theme_summary_by_bank.csv`                  | Top keywords + mapped themes per bank        |

---

## 📌 Notes

- Review data is originally from Task 1 (`fintech_reviews_clean.csv`)
- All code is modular and reproducible
