# 🗃️ Task 3 – Store Cleaned Data in Oracle Database

This branch (`task-3`) implements persistent storage of processed fintech app review data into an Oracle Database as part of the 10 Academy AI Mastery Week 2 challenge.

---

## 🎯 Objectives

- Design and create a normalized relational schema in Oracle
- Insert >1000 reviews labeled with sentiment using Python
- Ensure banks and reviews are properly linked via foreign keys
- Export database structure as an SQL dump

---

## 🏗️ Schema Overview

**`banks` table**  
- `bank_id` (PK)  
- `bank_name` (unique)

**`reviews` table**  
- `review_id` (PK)  
- `review_text`, `rating`, `review_date`  
- `bank_id` (FK → `banks.bank_id`)  
- `sentiment_label`, `sentiment_score`

---

## 📂 Project Structure

fintech-review-insights/
├── data/
│ └── processed/
│ └── fintech_reviews_with_sentiment.csv
├── scripts/
│ └── database/
│ ├── create_tables_oracle.sql
│ ├── upload_to_oracle.py
│ └── dump_bank_reviews.sql

---

## ⚙️ How to Run

Make sure Oracle XE is running.

```bash
python scripts/database/upload_to_oracle.py
