import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("annual.csv")

data[['Date', 'Price']].plot.hist(alpha=0.5)

plt.show()
