# # Data Profiling or Data Exploration :-> Understanding what exactly our data consists of 

import pandas as pd

# File Path
file_path = "data/raw/online_retail_II.xlsx"

df = pd.read_excel(file_path)

# # Checking if the file was loaded successfully
# print("Dataset loaded successfully!")
# print()

# # Size of the dataset : rows and columns
# print("Shape:", df.shape)
# print()

# # Returns the names of all the columns in the dataset
# print("Columns:")
# print(df.columns.tolist())
# print()

# # Returns the first 5 rows in the dataset
# print("First 5 rows:")
# print(df.head())

# # Checks every cell and if its empty then names it False and if it contains any value then names it as True and then returns the sum of all the cells that are empty i.e marked as True
# print()
# print("Missing values:")
# print(df.isnull().sum())

# # Returns the rows that have missing Customer ID
# print()
# print("Rows with missing Customer ID:")
# print(df[df["Customer ID"].isnull()].head())

# # Checking which rows have Negative values in the QUantity Column
# print()
# print("Negative quantity rows:")
# print((df["Quantity"] < 0).sum())

# # This displays examples of those negative-quantity records.
# print()
# print("Examples of negative quantities:")
# print(df[df["Quantity"] < 0].head(10))

# # Checks whether this invoice start with C?
# print()
# print("Invoices starting with C:")
# print(df["Invoice"].astype(str).str.startswith("C").sum())

# # Returns the examples of those
# print()
# print("Examples of C invoices:")
# print(df[df["Invoice"].astype(str).str.startswith("C")].head(10))

# # Returns the number of  C Invoice which have Positive Quantity
# print()
# print("C invoices with positive quantities:")
# print(
#     df[
#         (df["Invoice"].astype(str).str.startswith("C")) &
#         (df["Quantity"] > 0)
#     ].shape[0]
# )

# # Returns the examples of  C Invoice which have Positive Quantity
# print()
# print("C invoice with positive quantity:")
# print(
#     df[
#         (df["Invoice"].astype(str).str.startswith("C")) &
#         (df["Quantity"] > 0)
#     ]
# )

# # Checks the number of rows whose Prices column have zero or negative values
# print()
# print("Rows with price less than or equal to zero:")
# print((df["Price"] <= 0).sum())

# # Checks the examples of rows whose Prices column have zero or negative values
# print()
# print("Examples of rows with price <= 0:")
# print(df[df["Price"] <= 0].head(10))

# # Checks the date range of the data
# print()
# print("Date range:")
# print("Earliest date:", df["InvoiceDate"].min())
# # print("Latest date:", df["InvoiceDate"].max())

# # It checks whether an entire row has appeared previously with the same values across all columns.
# print()
# print("Duplicate rows:")
# print(df.duplicated().sum())

# # Returns the exampkes of some duplicated rows
# print()
# print("Example duplicate rows:")
# print(df[df.duplicated()].head(10))

# print()
# print("Rows with missing Description:")
# print(df[df["Description"].isnull()].head(20))


# print()
# print("Missing Description + Price = 0:")
# print(
#     df[
#         (df["Description"].isnull()) &
#         (df["Price"] == 0)
#     ].shape[0]
# )

# print()
# print("Missing Description + Missing Customer ID:")
# print(
#     df[
#         (df["Description"].isnull()) &
#         (df["Customer ID"].isnull())
#     ].shape[0]
# )

# print()
# print("Missing Description + Negative Quantity:")
# print(
#     df[
#         (df["Description"].isnull()) &
#         (df["Quantity"] < 0)
#     ].shape[0]
# )

print()
print("Price <= 0 but Description exists:")
print(
    df[
        (df["Price"] <= 0) &
        (df["Description"].notnull())
    ].head(20)
)
