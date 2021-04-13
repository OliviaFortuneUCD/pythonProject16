import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("GBvideos.csv")

x = data['channel_title'].head(4)
#x = data['views'].head(10)
y = data['likes'].head(4)

# Area plot
plt.fill_between(x, y)
plt.show()

