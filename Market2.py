''
import pandas as pd


data= pd.read_csv("GBvideos.csv")
x = data['channel_title'].head(3)
y1 = data['views'].head(3)
y2 = data['likes'].head(3)
print(x ,y1 , y2)
