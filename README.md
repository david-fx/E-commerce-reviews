# E-commerce-reviews
Women Clothing E-commerce Reviews
Data source from https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews

>>> %Run 'data audit.py'
Missing values per column:
 Unnamed: 0                    0
Clothing ID                   0
Age                           0
Title                      3810
Review Text                 845
Rating                        0
Recommended IND               0
Positive Feedback Count       0
Division Name                14
Department Name              14
Class Name                   14
dtype: int64
Jumlah duplikat: 0
Jumlah rating invalid: 0
Jumlah age invalid: 0
>>>

Results :   Hasil Audit Dataset Women’s E-Commerce Clothing Reviews

1. Missing Values
Title → 3,810 baris kosong.
Review Text → 845 baris kosong.
Division Name → 14 baris kosong.
Department Name → 14 baris kosong.
Class Name → 14 baris kosong.

2. Duplicates
Jumlah duplikat → 0.

3. Format Errors
Rating → semua valid (1–5).
Age → semua valid (>0).
