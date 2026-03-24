# E-commerce-reviews
Women Clothing E-commerce Reviews
Data source from https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews

>>> %Run 'data audit.py'
Results :   Audit Dataset Women’s E-Commerce Clothing Reviews

<img width="900" height="361" alt="image" src="https://github.com/user-attachments/assets/1529234d-b12d-44f9-97ba-e6e6551b5263" />


Apply fixes to data
<img width="623" height="128" alt="image" src="https://github.com/user-attachments/assets/bf29924d-f0e8-4e35-b5bd-ca465feaa53f" />

df['Title'] = df['Title'].fillna("No Title")
df = df.dropna(subset=['Review Text'])
df['Division Name'] = df['Division Name'].fillna("Unknown")
df['Department Name'] = df['Department Name'].fillna("Unknown")
df['Class Name'] = df['Class Name'].fillna("Unknown")
