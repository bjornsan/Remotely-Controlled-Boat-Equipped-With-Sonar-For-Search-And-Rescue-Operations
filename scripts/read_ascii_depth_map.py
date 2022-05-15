from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"C:\Users\bjorn\Desktop\stordammen\stordammen_test.txt", delimiter=" ")

ax = sns.heatmap(data, cmap="YlGnBu")
plt.show()