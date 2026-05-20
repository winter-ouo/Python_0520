import pandas as pd

# 1. 用 list 建立 stock1
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])

print("stock1")
print(stock1)

# 2. 建立 stock2
stock2 = pd.Series(
    [120, 80, None, 60, 95, None, 110],
    index=["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
)

print("\nstock2")
print(stock2)

# 3. 轉成字典 stock3
stock3 = stock2.to_dict()

print("\nstock3")
print(stock3)

# 4. Banana 庫存值
print("\nBanana 庫存：", stock2["Banana"])

# 5. 缺失值檢查
print("\n缺失值檢查：")
print(stock2.isnull())

# 6. 缺失值數量
print("\n缺失值數量：", stock2.isnull().sum())

# 7. 存成 CSV 表格
df = stock2.fillna("NULL").to_frame()

df.to_csv(
    "0520_stock.csv",
    header=False,
    encoding="utf-8-sig"
)

print("\n0520_stock.csv 表格存檔完成")