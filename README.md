# E-commerce-reviews
Women Clothing E-commerce Reviews
Data source from https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews

>>> %Run 'data audit.py'
Results :   Hasil Audit Dataset Women’s E-Commerce Clothing Reviews

Issue Type	                 Count	  Example	  Fix Applied
Missing Title	               3,810	  NULL	    Isi placeholder “No Title”
Missing Review Text          845	    NULL	    Drop rows (tidak usable)
Missing Division/Dept/Class	 14 	    NULL	    Isi dengan “Unknown”
Duplicates	0	–	Tidak ada tindakan
Invalid Rating	0	–	Tidak ada tindakan
Invalid Age	0	–	Tidak ada tindakan
