import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analyze_f_strength_utilis import*
import statsmodels.api as sm

# Path to csv file
path = r"C:\Users\bjorn\Desktop\sonar\data\sonar_test.csv"

path_b = r"C:\Users\bjorn\Desktop\sonar\data\bathymetry_test.csv"
# Path to store the sound profile.
path_2 = r"C:\Users\bjorn\Desktop\sonar\plots\sound_profile_3.txt"

# Loading the data set.
df_reflection_strength = pd.read_csv(path, delimiter=",", names=list(range(2000)))

df_UDP = pd.read_csv(path_b, delimiter=",")

depth=  df_UDP["depth"]

# n number of rows to extact from csv
n = 5000

# Initialazing a list to contain depth values from UDP file.
depth_list = []

# Appending n rows from UDP_csv to the depth list.
for i in range(n):
    depth_list.append(depth[i])

# Get a specific row in the data set. Parameters: dataset, row_start, row_end
row = get_row(df_reflection_strength, 3000, 3001)

# Cleans the dataset from nan and empty cells. Parameter: the row to clean
clean = clean_data_row(row)

# List containing n rows of frequency strength from reflection strength csv.
reflection_strength = get_range_of_rows(n, df_reflection_strength)

# Storing the number of columns per row into a list.
# This is done to do a correlation test between depth in meters and the number of columns in the reflection strength data. 
columns_per_row = []

for row in reflection_strength:
    columns_per_row.append(len(row))

# Combining the depth in meters with the columns per row to make a simple visualization of the correlation.
zipped = zip(depth_list, columns_per_row)

#for z in zipped:
#    print(z)

print("\n\n\n")
#print_sound_profile(nd_array_of_data[0], len(nd_array_of_data[0]), path_2)

#####
# Print each row in data set
#
#for idx, r in enumerate(nd_array_of_data):
#    print("[ROW: " + str(idx) + "]")
#    print(r)

#####
# Prints t-test, correlation etc.
#
x = depth_list
y = columns_per_row
#x_3 = sm.add_constant(x)
#model = sm.OLS(y, x_3).fit()
#print(model.summary())

print("Correlation matrix")
print( np.corrcoef(x, y) )
#print("\n\n\n")
#hist, bin_edges = np.histogram(clean)
#histo = plt.hist(hist, bins)
#plt.show()

#####
# Plotting a horizontal histogram of frequency strength at each depth.
#
x_2 = np.arange(len(clean))
plt.barh(x_2, clean)
plt.ylabel("Columns from csv")
plt.xlabel("Frequency strength in each column")
ax = plt.gca()
ax.invert_yaxis()

# save plot to file  
#plt.savefig(r"C:\Users\bjorn\Desktop\sonar\Plots\test.png")

plt.show()    







