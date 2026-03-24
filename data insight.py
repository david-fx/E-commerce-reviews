import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Pastikan folder images ada
if not os.path.exists("images"):
    os.makedirs("images")
    
# 1. Load dataset yang sudah dibersihkan
df = pd.read_csv("Womens_Clothing_E-commerce_Reviews_Cleaned.csv")

# 2. Distribusi Rating
plt.figure(figsize=(8,6))
sns.countplot(x="Rating", data=df, color="skyblue")  
plt.title("Distribution of Product Ratings", fontsize=14)
plt.xlabel("Rating (1-5)")
plt.ylabel("Count of Reviews")
plt.tight_layout()
plt.savefig("images/rating_distribution.png")
plt.show()

# 3. Produk dengan Positive Feedback terbanyak
top_feedback = df.groupby("Clothing ID")["Positive Feedback Count"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_feedback.index, y=top_feedback.values, color="orange")
plt.title("Top 10 Products by Positive Feedback", fontsize=14)
plt.xlabel("Clothing ID")
plt.ylabel("Total Positive Feedback")
plt.tight_layout()
plt.savefig("images/top_feedback_products.png")
plt.show()

