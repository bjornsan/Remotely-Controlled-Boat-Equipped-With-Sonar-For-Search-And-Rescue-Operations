from cmath import isnan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analysis import udp_analysis
import statsmodels.api as sm

'''
def clean_row(data, key):
    cleaned_data = []
    idx = 0
    for row in data[key]:
        if not math.isnan(row):
            cleaned_data.append( [data["time"][idx], data["longtitude"][idx], row, data["depth"][idx]] )
        idx = idx+1
    return cleaned_data
'''

# Path to csv file
path_narrow = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_narrow_sonar_data.csv"
path_mid = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_mid_sonar_data.csv"
path_wide = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\test_wide_sonar_data.csv"

# Narrow frequency band data
#df_narrow = pd.read_csv(path_narrow, delimiter=",")
#data_narrow = df_narrow[["time", "depth", "latitude", "longtitude"]]
#cleaned_narrow = clean_row(data_narrow, "latitude")

# Mid frequency band data
#df_mid = pd.read_csv(path_mid, delimiter=",")
#data_mid = df_mid[["time", "depth", "latitude", "longtitude"]]
#cleaned_mid = clean_row(data_mid, "latitude")

# Wide frequency band data
#df_wide = pd.read_csv(path_wide, delimiter=",")
#data_wide = df_wide[["time", "depth", "latitude", "longtitude"]]
#cleaned_wide = clean_row(data_wide, "latitude")
ua = udp_analysis()
cleaned_narrow = ua.get_data(path_narrow)
cleaned_mid = ua.get_data(path_mid)
cleaned_wide = ua.get_data(path_wide)

####
#
#   Making sure all data has the same length.
#
#   This method could be automated. Find out what data set is the longest, 
#   and then use that data set to set the length of the other data sets.
#
#   Should think about some way to make better validation of data.
#   
#   Perhaps a better way would be to check for equal coordinateas, and depth 
#   at those very same coordinates.
#
#   Round the coordinates, and find coordinates that are close enough to think
#   of as in the same spot. From this very spot, do make a comparsion of depth.
#

#   print(len(cleaned_narrow), len(cleaned_mid), len(cleaned_wide))

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
error_margin = 0.0001
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
#plt.style.use('dark_background')
fig, ax = plt.subplots()
#ax.set_facecolor("grey")
ax.bar(x-0.3, npNarrow, color="#BDCCE4", width=0.30, label="Narrow") 
ax.bar(x, npMid, color="#6488BF", width=0.30, label="Mid")  
ax.bar(x+0.3, npWide, color="#2255A4", width=0.30, label="Wide")  
ax.legend()
ax.set_ylabel("Depth in meters", fontsize=20)
ax.set_xlabel("Mesurements over time", fontsize=20)
plt.show()

####
#
#   Printing data from one data set to the console.
#
#print("##########################################################################")
#print("#\tTIMESTAMP:\tLATITUDE\tLONGITUDE\tDEPTH\t\t#")
#print("##########################################################################")
#
#for x in cleaned_narrow:
#    print(f"#\t{x[0]}\t{round(x[1], 4)}\t\t{round(x[2], 4)}\t\t{x[3]} meters\t#")
#
#print()
#print("##########################################################################")


####
#
#   Comparing depth data from different frequency bands.
#
#print("\n\n##########################################################################")
#print("#\tTIMESTAMP:\tNARROW\t\tMID\t\tWIDE\t\t#")
#print("##########################################################################")
#
#for i in range(len(cleaned_mid)):
#    narrow_depth = cleaned_narrow[i][3]
#    mid_depth = correct_length_mid[i][3]
#    wide_depth = correct_length_wide[i][3]
#    print(f"#\t{cleaned_narrow[i][0]}\t{narrow_depth}\t\t{mid_depth}\t\t{wide_depth} meters\t#")

#print()
#print("##########################################################################\n\n")