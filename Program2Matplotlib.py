import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("annual.csv")

x = data['Date']
#x = data['views'].head(10)
y = data['Price']

# Area plot
plt.fill_between(x, y)
plt.show()

