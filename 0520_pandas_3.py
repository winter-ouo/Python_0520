import pandas as pd

# 讀取資料
df = pd.read_csv("HW_DATA.csv")

# 1. 檢視資料筆數與前5筆內容
print("===== 資料維度 =====")
print(df.shape)

print("\n===== 前5筆資料 =====")
print(df.head())

# 2. 篩選 Branch 為 A 且 Customer type 為 Member
df_filter = df[
    (df["Branch"] == "A") &
    (df["Customer type"] == "Member")
]

print("\n===== Branch=A 且 Customer type=Member =====")
print(df_filter.head())

print("\n符合條件的資料筆數：")
print(df_filter.shape[0])

# 3. 依 Product line 分組
# 計算總銷售額(Sales)與平均評分(Rating)
product_summary = (
    df.groupby("Product line")
      .agg({
          "Sales": "sum",
          "Rating": "mean"
      })
      .round(2)
)

print("\n===== 各產品線銷售額與平均評分 =====")
print(product_summary)

# 4. 依 City 與 Gender 分組
# 計算平均銷售額與交易筆數
city_gender_summary = (
    df.groupby(["City", "Gender"])
      .agg(
          Avg_Sales=("Sales", "mean"),
          Transaction_Count=("Invoice ID", "count")
      )
      .round(2)
)

print("\n===== City 與 Gender 統計 =====")
print(city_gender_summary)

# 5. 找出總銷售額最高的產品線
top_product = product_summary["Sales"].idxmax()
top_sales = product_summary["Sales"].max()

print("\n===== 總銷售額最高的產品線 =====")
print("Product Line :", top_product)
print("Total Sales  :", format(top_sales, ".2f"))

# 6. 輸出 CSV 檔
product_summary.to_csv(
    "0520_pandas_3OK.csv",
    encoding="utf-8-sig",
    float_format="%.2f"
)

print("\n0520_pandas_3OK.csv 存檔完成")