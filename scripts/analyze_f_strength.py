import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from analyze_f_strength_utilis import*
import statsmodels.api as sm

# Path to csv file
path = r"C:\Users\bjorn\Desktop\sonar\data\sonar.csv"

# Path to store the sound profile.
path_2 = r"C:\Users\bjorn\Desktop\sonar\plots\sound_profile_3.txt"

# Loading the data set.
df = pd.read_csv(path, delimiter=",", names=list(range(2000)))

# Get a specific row in the data set. Parameters: dataset, row_start, row_end
row = get_row(df, 4754, 4755)

# Cleans the dataset from nan and empty cells. Parameter: the row to clean
clean = clean_data_row(row)

# 
nd_array_of_data = get_range_of_rows(100, df)
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
#xx = df[0]
#yy = df[1]
#xXx = sm.add_constant(xx)
#model = sm.OLS(yy, xXx).fit()
#print(model.summary())


#hist, bin_edges = np.histogram(clean)
#histo = plt.hist(hist, bins)
#plt.show()

#####
# Plotting a horizontal histogram of frequency strength at each depth.
#
x = np.arange(len(clean))
plt.barh(x, clean)
plt.ylabel("Columns from csv")
plt.xlabel("Frequency strength in each column")
ax = plt.gca()
ax.invert_yaxis()

# save plot to file  
#plt.savefig(r"C:\Users\bjorn\Desktop\sonar\Plots\test.png")

plt.show()    







