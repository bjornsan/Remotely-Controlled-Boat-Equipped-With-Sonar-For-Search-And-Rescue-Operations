from cmath import isnan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analysis import udp_analysis
import statsmodels.api as sm


# Path to csv file
#path_narrow = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_narrow_sonar_data.csv"
#path_mid = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_mid_sonar_data.csv"
#path_wide = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_wide_sonar_data.csv"

path_narrow = r"C:\Users\bjorn\Desktop\sonar\data\pollesundet_14_03_22\Pollesundet\beamtest\narrow\bathymetry.csv"
path_mid = r"C:\Users\bjorn\Desktop\sonar\data\pollesundet_14_03_22\Pollesundet\beamtest\mid\bathymetry.csv"
path_wide = r"C:\Users\bjorn\Desktop\sonar\data\pollesundet_14_03_22\Pollesundet\beamtest\wide\bathymetry.csv"

# Analysis object containing functionalilty to
ua = udp_analysis()

# Reading data from CSV
cleaned_mid = ua.get_data(path_narrow)
cleaned_narrow = ua.get_data(path_mid)
cleaned_wide = ua.get_data(path_wide)

# Making sure the data is of the same length
correct_length_mid = []
correct_length_wide = []

for i in range(len(cleaned_mid)):
    correct_length_mid.append(cleaned_mid[i])
    correct_length_wide.append(cleaned_wide[i])

narrow_plot = []
mid_plot = []
wide_plot = []

print("\n\n#########################################################################################################")
print("#\tLATITUDE\t\tLONGITUDE\t\tNARROW\t\tMID\t\tWIDE\t\t#")
print("#########################################################################################################")
error_margin=0.0001
for j in range(len(cleaned_mid)):
    lat = abs( (round(cleaned_mid[j][1], 6) - round(cleaned_narrow[j][1], 6) ) )
    lon = abs( (round(cleaned_mid[j][2], 6) - round(cleaned_narrow[j][2], 6) ) )
    if  lat < error_margin and lon < error_margin:
        print(f"#\t{round(cleaned_narrow[j][1], 6)}\t\t{round(cleaned_narrow[j][2], 6)}\t\t{cleaned_narrow[j][3]}\t\t{cleaned_mid[j][3]}\t\t{cleaned_wide[j][3]}\t\t#" )
        narrow_plot.append(cleaned_narrow[j][3])
        mid_plot.append(cleaned_mid[j][3])
        wide_plot.append(cleaned_wide[j][3])  
print("#########################################################################################################\n\n")


x = np.arange(len(narrow_plot) )
npNarrow = np.array(narrow_plot)
npMid = np.array(mid_plot)
npWide = np.array(wide_plot)
width = 0.30
fig, ax = plt.subplots()
ax.bar(x-0.3, npNarrow, color="#BDCCE4", width=0.30, label="Narrow") 
ax.bar(x, npMid, color="#6488BF", width=0.30, label="Mid")  
ax.bar(x+0.3, npWide, color="#2255A4", width=0.30, label="Wide")  
ax.legend()
ax.set_ylabel("Depth in meters", fontsize=20)
ax.set_xlabel("Mesurements over time", fontsize=20)
plt.show()
