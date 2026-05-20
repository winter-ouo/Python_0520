import pandas as pd

data1 = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data1)

data2 = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data2, columns=["Product", "Price", "Sales"])

print(df2.head())

print(df2.tail())

print(df2.shape)

print(df2.columns)

print(df2.dtypes)

print(df2.count())

info = df2.describe().round(2)

print(info)

info.to_csv(
    "0520_stock2.csv",
    encoding="utf-8-sig"
)

print("0520_stock2.csv 存檔完成")