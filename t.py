'''
1.建立 Series：import pandas as pd
s = pd.Series([10, 20, 30, 40])
print(s)

方法二：自訂索引
import pandas as pd
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)

方法三：用字典建立
import pandas as pd
s = pd.Series({"Amy": 88, "Bob": 92, "Cathy": 79})#字典記得用大括號
print(s)

2.to_dict() 是 pandas 的「轉成字典」方法
import pandas as pd
a = pd.Series([10, 20],index=["A", "B"])
print(a.to_dict())

3.取值方式 ：
import pandas as pd
s = pd.Series([10, 20, 30, 40])
print(s[0])
print(s[0:2])

4.檢查缺失值 
Pandas 提供 isnull()函式來檢查資料是否為缺失值。
若資料為缺失值會顯示 True，不是缺失值則顯示 False。
此外，搭配 sum() 可以快速統計每個欄位缺失值的數量，方便分析資料品質。 
read_csv()， pandas 的「固定內建函式名稱」，用來讀取 CSV 檔案 

import pandas as pd
s = pd.read_csv("data.csv")
print(s.isnull().sum())

5.to_csv() pandas 的「固定內建函式名稱」，用來儲存 CSV 檔案 
import pandas as pd
s = pd.Series([10, 20, 30, 40])
s.to_csv("stock.csv", index=False)
print("存檔完成")
'''