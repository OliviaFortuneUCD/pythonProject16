import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("GBvideos.csv")

data[['likes', 'dislikes']].plot.hist(alpha=0.5)

plt.show()
