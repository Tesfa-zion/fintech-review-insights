# fintech-review-insights
Analyzing user reviews of Ethiopian fintech apps from Google Play Store
# 📌 Task 1 – Data Collection & Preprocessing

This branch (`task-1`) contains all scripts and data preparation work for **Task 1** of the 10 Academy Week 2 challenge.

---

## ✅ Objectives

- Scrape reviews from 3 Ethiopian bank mobile apps on the Google Play Store
- Store raw reviews in structured CSV files
- Clean, combine, and preprocess review data
- Organize scripts and data clearly

---

## 🗂️ Project Structure

.
├── data/
│ ├── raw/ # Raw scraped reviews per bank
│ └── processed/ # Cleaned and merged review dataset
├── scripts/
│ ├── scraping/ # Google Play scraping script
│ └── processing/ # Merging, cleaning, sentiment scripts
├── requirements.txt
└── README.md

---

## 📜 Scripts

- `scripts/scraping/scrape_reviews.py`: Scrapes 1000 reviews for each bank app
- `scripts/processing/merge_reviews.py`: Merges all raw CSVs and cleans the combined dataset

---

## 📁 Output

- `data/raw/*.csv`: Raw scraped files for each bank
- `data/processed/fintech_reviews_clean.csv`: Cleaned and deduplicated dataset

---

## 🧼 Preprocessing Steps

- Remove duplicates
- Drop nulls
- Normalize date format
- Organize per bank

---

## ✅ Status

✅ Completed and pushed under `task-1` branch  
📦 Ready for merge into `main`  
➡️ Next: Sentiment analysis in `task-2` branch
