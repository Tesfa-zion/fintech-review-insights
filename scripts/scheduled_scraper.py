from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import schedule
import logging
import time
import os

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Apps to scrape
APP_IDS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

def scrape_play_store_reviews():
    logging.info("🔄 Scheduled scraping started...")
    for bank_name, app_id in APP_IDS.items():
        try:
            logging.info(f"Fetching reviews for {bank_name}...")
            results, _ = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=1000
            )

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_bank = bank_name.lower().replace(" ", "_")
            filename = f"{safe_bank}_reviews_{timestamp}.csv"
            filepath = os.path.join("data", filename)

            os.makedirs("data", exist_ok=True)

            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
                writer.writeheader()

                for entry in results:
                    writer.writerow({
                        'review_text': entry['content'],
                        'rating': entry['score'],
                        'date': entry['at'].strftime('%Y-%m-%d'),
                        'bank_name': bank_name,
                        'source': 'Google Play'
                    })

            logging.info(f"✅ Saved {len(results)} reviews to {filename}")
        except Exception as e:
            logging.error(f"❌ Error scraping {bank_name}: {e}")

# Schedule it to run daily at 1 AM (can be changed)
schedule.every().day.at("01:00").do(scrape_play_store_reviews)

# Keep the script running
if __name__ == "__main__":
    logging.info("🔁 Scraper scheduler started")
    scrape_play_store_reviews()  # this above `while True`due to work on datas before
    while True:
        schedule.run_pending()
        time.sleep(1)
