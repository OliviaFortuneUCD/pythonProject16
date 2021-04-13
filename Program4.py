import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("GBvideos.csv")

category_count = data['category_id'].value_counts()


ax = category_count.plot.bar()
ax.set_xticklabels(labels=category_count.index, rotation=45, fontsize=10)

plt.show()