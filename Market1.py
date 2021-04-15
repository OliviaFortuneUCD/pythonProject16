import matplotlib.pyplot as plt
fig,ax = plt.subplots()
import pandas as pd


data= pd.read_csv("GBvideos.csv")
x = data['channel_title'].head(3)
y1 = data['views'].head(3)
y2 = data['likes'].head(3)
ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y1, marker="v", linestyle="--", color="r")
plt.show()
