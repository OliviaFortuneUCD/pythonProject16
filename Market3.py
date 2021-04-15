import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots()
import pandas as pd

data= pd.read_csv("GBvideos.csv")

x = data['video_id'].head(3)
y = data['views'].head(3)




sns.lineplot(x,y)
plt.show()

