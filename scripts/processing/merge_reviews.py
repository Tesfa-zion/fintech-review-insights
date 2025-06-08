import pandas as pd
import os

data_dir = "data"
output_file = os.path.join(data_dir, "fintech_reviews_clean.csv")

# Load all CSVs that match *_reviews_*.csv
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv") and "_reviews_" in f]

all_reviews = []

for file in csv_files:
    path = os.path.join(data_dir, file)
    df = pd.read_csv(path)
    all_reviews.append(df)

# Combine all reviews
df_all = pd.concat(all_reviews, ignore_index=True)

# Clean up
df_all.dropna(inplace=True)
df_all.drop_duplicates(subset=["review_text"], inplace=True)
df_all['date'] = pd.to_datetime(df_all['date'], errors='coerce').dt.strftime('%Y-%m-%d')
df_all.dropna(subset=['date'], inplace=True)

# Save the cleaned data
df_all.to_csv(output_file, index=False)
print(f"✅ Merged and cleaned dataset saved to {output_file}")
print(df_all['bank_name'].value_counts())
