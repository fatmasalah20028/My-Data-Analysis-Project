import pandas as pd

df = pd.read_csv("3) Sentiment dataset.csv")

print("Dataset info before processing:")
df.info()

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop(columns=["Unnamed: 0.1"], inplace=True)


df['Text'] = df['Text'].str.strip()
df['Text'] = df['Text'].str.replace(r'\s+', ' ', regex=True)


df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

df.dropna(subset=['Text', 'Sentiment', 'Timestamp'], inplace=True)

df['Platform'].fillna('unknown', inplace=True)
df['Country'].fillna('unknown', inplace=True)

df.drop_duplicates(inplace=True)

text_cols = ['Sentiment', 'Platform', 'Country']
for col in text_cols:
    df[col] = df[col].astype(str).str.lower().str.strip()
df['Retweets'] = pd.to_numeric(df['Retweets'], errors='coerce')
df['Likes'] = pd.to_numeric(df['Likes'], errors='coerce')

print("\n" + "="*50)
print("Dataset info after processing:")
print(f"Shape: {df.shape}")
print(f"Total rows: {len(df)}")
print("\nMissing values:")
print(df.isnull().sum())

print("\nSentiment distribution:")
print(df['Sentiment'].value_counts())

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned data saved to 'cleaned_dataset.csv'")
