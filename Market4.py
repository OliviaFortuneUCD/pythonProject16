import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots()
import pandas as pd

data= pd.read_csv("GBvideos.csv")

x = data['category_id']
y = data['views']




sns.lineplot(x,y)
plt.show()
