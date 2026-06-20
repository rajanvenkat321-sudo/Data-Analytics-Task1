import pandas as pd
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")
print("========== DATASET INFO ==========")
print(df.info())
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())
print("\n========== DUPLICATES ==========")
print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())
if "City" in df.columns:
    df["City"] = df["City"].fillna(df["City"].mode()[0])
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
if "Total_Sales" in df.columns:
    Q1 = df["Total_Sales"].quantile(0.25)
    Q3 = df["Total_Sales"].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[
        (df["Total_Sales"] < lower) |
        (df["Total_Sales"] > upper)
    ]
    print("\n========== OUTLIERS ==========")
    print("Outliers Found:", len(outliers))
df.to_csv("Cleaned_Sales_Dataset.csv", index=False)

print("\n========== SUCCESS ==========")
print("Cleaned dataset saved as:")
print("Cleaned_Sales_Dataset.csv")