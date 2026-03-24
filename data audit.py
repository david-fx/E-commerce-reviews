import pandas as pd
# 1. Load dataset
df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")
# 2. Cek missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)
# 3. Cek duplikat
duplicates = df.duplicated().sum()
print("Jumlah duplikat:", duplicates)
# 4. Cek format error
# Contoh: Rating harus antara 1–5
invalid_rating = df[~df['Rating'].between(1,5)]
print("Jumlah rating invalid:", len(invalid_rating))
# Contoh: Age harus numeric dan positif
invalid_age = df[df['Age'] <= 0]
print("Jumlah age invalid:", len(invalid_age))
