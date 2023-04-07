# pip install pandas   
# Import pandas
import pandas as pd


# read `data/books.csv`

df = pd.read_csv('data/books.csv')

# Find all penguin books, look for dataframe filtering
# Try with a different publisher

print (df[df["Publisher"]=="Penguin"])

# Add your favorite book

new_df = pd.DataFrame([{"Title": "AM","Author": "CS","Genre": "PR","Height": None,"Publisher": None}])

df.append(new_df)


# Export the dataframe to JSON

df.to_json("data/new-books.json", orient="records")

# Write it to DB using to_sql

df = pd.read_json("data/books.json")
df.to_csv("data/new-books.csv")

# Go through pandas documentation and look at the methods you find interesting