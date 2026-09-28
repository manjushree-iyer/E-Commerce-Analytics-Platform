import pandas as pd

file_path = "data/raw/online_retail_II.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print()

print("Shape:", df.shape)
print()

print("Columns:")
print(df.columns.tolist())
print()

print("First 5 rows:")
print(df.head())

print()
print("Missing values:")
print(df.isnull().sum())

print()
print("Rows with missing Customer ID:")
print(df[df["Customer ID"].isnull()].head())

print()
print("Negative quantity rows:")
print((df["Quantity"] < 0).sum())

print()
print("Examples of negative quantities:")
print(df[df["Quantity"] < 0].head(10))


print()
print("Invoices starting with C:")
print(df["Invoice"].astype(str).str.startswith("C").sum())

print()
print("Examples of C invoices:")
print(df[df["Invoice"].astype(str).str.startswith("C")].head(10))

print()
print("C invoices with positive quantities:")
print(
    df[
        (df["Invoice"].astype(str).str.startswith("C")) &
        (df["Quantity"] > 0)
    ].shape[0]
)

print()
print("C invoice with positive quantity:")
print(
    df[
        (df["Invoice"].astype(str).str.startswith("C")) &
        (df["Quantity"] > 0)
    ]
)

print()
print("Rows with price less than or equal to zero:")
print((df["Price"] <= 0).sum())

print()
print("Examples of rows with price <= 0:")
print(df[df["Price"] <= 0].head(10))


print()
print("Date range:")
print("Earliest date:", df["InvoiceDate"].min())
print("Latest date:", df["InvoiceDate"].max())


print()
print("Duplicate rows:")
print(df.duplicated().sum())


print()
print("Example duplicate rows:")
print(df[df.duplicated()].head(10))