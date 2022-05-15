import pandas as pd
from analysis import reflection_analysis
from matplotlib import pyplot as plt
import numpy as np

# Paths to csv files
path_swimming = r"C:\Users\bjorn\Desktop\sonar\data\gaustahallen\pm111\sonar.csv"
path = r"C:\Users\bjorn\Desktop\sonar\data\test_data_deeper\sonar_test.csv"
path_engelsviken = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\sonar.csv"
path_engelsviken_UDP = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\bathymetry.csv"
path_b = r"C:\Users\bjorn\Desktop\sonar\data\bathymetry_test.csv"
path_polle_rope = r"C:\Users\bjorn\Desktop\sonar\data\pollesundet_14_03_22\Pollesundet\rope_test\narrow\sonar.csv"

# Path to store the sound profile.
path_2 = r"C:\Users\bjorn\Desktop\sonar\plots\sound_profile_3.txt"


# Loading the data set.
df_reflection_strength = pd.read_csv(path_swimming, delimiter=",", names=list(range(2000)))
df_UDP = pd.read_csv(path_engelsviken_UDP, delimiter=",")
depth = df_UDP["depth"]
ra = reflection_analysis()

# Getting a row and plotting its histogram
data_1 = ra.get_processed_row_of_data(475, df_reflection_strength)
data_1[1].reverse()
#data_2 = ra.get_processed_row_of_data(637, df_reflection_strength)
ra.plot_refletion_strength(data_1)

# Used to plot many histograms against each other.
#x_2 = np.arange(len(data_1[1]))
#x_3 = np.arange(len(data_2[1]))
#plt.barh(x_2, data_1[1], label="Hit rope")
#plt.barh(x_3, data_2[1], label="No hit")
#plt.ylabel("Columns from csv", fontsize=20)
#plt.xlabel("Recieved reflection intensity", fontsize=20)
#ax = plt.gca()
#ax.invert_yaxis()
#plt.legend()
#plt.show() 

#data_1 = ra.get_range_of_rows(281, 444, df_reflection_strength)

#for i in range(len(data_1)):
#    data_1[i][1].reverse()


# Correlation test between n number of rows in csv file and actual measured depth
#data = ra.get_range_of_rows(0, 500, df_reflection_strength)
#peaks = ra.get_peaks(data)
#corr = ra.correlation_test(depth, peaks, 500)
#print(corr)












   







