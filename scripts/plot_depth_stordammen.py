from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

path = r"C:\Users\bjorn\Desktop\sonar\data\Stordammen\bathymetry.csv"
df = pd.read_csv(path, delimiter=",")
depth = df["depth"].to_numpy()

x = np.arange(len(depth))

plt.bar(x, depth)
plt.xlabel("Measurement over time", fontsize=20)
plt.ylabel("Depth in meters", fontsize=20)
plt.show()