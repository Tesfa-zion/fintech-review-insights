import pandas as pd
import oracledb

# ----------------------
# 🔧 Connection Config
# ----------------------
username = "system"           # or your Oracle username
password = "vulture4th"     # change this to your actual password
dsn = "localhost:1521/XEPDB1"  # Easy Connect string for Oracle XE (21c)

# ----------------------
# 📄 Load Data
# ----------------------
df = pd.read_csv("data/processed/fintech_reviews_with_sentiment.csv")

# Keep only the needed columns and rename for DB
df = df[['review_text', 'rating', 'date', 'bank_name', 'source', 'sentiment', 'sentiment_score']]
df.rename(columns={'date': 'review_date', 'sentiment': 'sentiment_label'}, inplace=True)

# ----------------------
# 🔌 Connect to Oracle
# ----------------------
conn = oracledb.connect(user=username, password=password, dsn=dsn)
cursor = conn.cursor()

# ----------------------
# 🏦 Insert Unique Banks
# ----------------------
bank_ids = {}
for bank in df['bank_name'].unique():
    # Insert or ignore (MERGE-style)
    cursor.execute("""
        MERGE INTO banks b
        USING (SELECT :bank_name AS bank_name FROM dual) src
        ON (b.bank_name = src.bank_name)
        WHEN NOT MATCHED THEN
            INSERT (bank_name) VALUES (:bank_name)
    """, {"bank_name": bank})

    # Retrieve bank_id
    cursor.execute("SELECT bank_id FROM banks WHERE bank_name = :bank_name", {"bank_name": bank})
    bank_ids[bank] = cursor.fetchone()[0]

# ----------------------
# 📝 Insert Review Records
# ----------------------
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (
            review_text, rating, review_date, bank_id, source,
            sentiment_label, sentiment_score
        )
        VALUES (
            :review_text, :rating, TO_DATE(:review_date, 'YYYY-MM-DD'),
            :bank_id, :source, :sentiment_label, :sentiment_score
        )
    """, {
        'review_text': row['review_text'],
        'rating': int(row['rating']),
        'review_date': row['review_date'],
        'bank_id': bank_ids[row['bank_name']],
        'source': row['source'],
        'sentiment_label': row['sentiment_label'],
        'sentiment_score': float(row['sentiment_score'])
    })

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ All data inserted into Oracle Database successfully.")
