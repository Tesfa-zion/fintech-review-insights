from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime
import os

# Make sure data/ folder exists
os.makedirs('data', exist_ok=True)

# App package IDs
apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

# Collect reviews from all banks
all_reviews = []

for bank, app_id in apps.items():
    print(f"📥 Scraping reviews for: {bank}")
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=550
        )

        for r in result:
            all_reviews.append({
                "review": r['content'],
                "rating": r['score'],
                "date": r['at'].strftime('%Y-%m-%d'),
                "bank": bank,
                "source": "Google Play"
            })

    except Exception as e:
        print(f"❌ Error scraping {bank}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Save to CSV
output_path = "data/fintech_reviews_raw.csv"
df.to_csv(output_path, index=False)
print(f"✅ Saved {len(df)} reviews to {output_path}")
