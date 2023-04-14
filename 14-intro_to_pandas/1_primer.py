# pip install pandas   
# Import pandas
import pandas as pd

# Series - very similar to list

data = [['Alex',10],['Bob',12],['Clarke',13], ['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data, columns=['Name','Age'])
print (df)
df.head()
df.info()
df.shape
# df [ <condition> ]
df[ df['Age'] >= 12 ]

# read `data/books.csv`

df = pd.read_csv("14-intro_to_pandas/books.csv")

# Find all penguin books, look for dataframe filtering
# Try with a different publisher

print (df[df["Publisher"]=="Penguin"])

# Add your favorite book

new_df = pd.DataFrame([{"Title": "AM","Author": "CS","Genre": "PR","Height": None,"Publisher": None}, {"Title": "PN","Author": "DM","Genre": "PR","Height": None,"Publisher": None}])

df.append(new_df)


# Export the dataframe to JSON

df.to_json("data/new-books.json", orient="records")

# Write it to DB using to_sql

df = pd.read_json("data/books.json")
df.to_csv("data/new-books.csv")

# Go through pandas documentation and look at the methods you find interesting