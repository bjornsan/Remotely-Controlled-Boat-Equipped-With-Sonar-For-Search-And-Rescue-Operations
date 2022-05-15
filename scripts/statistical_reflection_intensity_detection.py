from asyncore import poll
from analysis import reflection_analysis 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot

ra = reflection_analysis()
path_gaustad = r"C:\Users\bjorn\Desktop\sonar\data\gaustahallen\pm111\sonar.csv"
df_gaustad = pd.read_csv(path_gaustad, delimiter=",", names=list(range(2000)))

path_pollesundet = r"C:\Users\bjorn\Desktop\sonar\data\pollesundet_14_03_22\Pollesundet\rope_test\narrow\sonar.csv"
df_pollesundet = pd.read_csv(path_pollesundet, delimiter=",", names=list(range(2000)))

path_diver = r"C:\Users\bjorn\Desktop\sonar\data\dive_test_firedepartment\sonar.csv"
df_diver = pd.read_csv(path_diver, delimiter=",", names=list(range(2000)))

path_engel = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\sonar.csv"
df_engel = pd.read_csv(path_engel, delimiter=",", names=list(range(2000)))

diver_row_1 = ra.get_processed_row_of_data(22901, df_diver)
diver_row_2 = ra.get_processed_row_of_data(22446, df_diver)
engel_row = ra.get_processed_row_of_data(512, df_engel)
diver_np_1 = np.array(diver_row_1)
diver_np_2 = np.array(diver_row_2)
engel_np = np.array(engel_row)

pollesundet_ref_data = df_pollesundet.to_numpy()
polle_start = 384
polle_end = 510
polle_data = ra.get_range_of_rows(polle_start, polle_end, pollesundet_ref_data, use_np=True)
polle_peaks = ra.get_peaks(polle_data)
polle_np = np.array(polle_peaks)

gaustad_ref_data = df_gaustad.to_numpy()
gaustad_col_start = 281
gaustad_col_end = 444
gaustad_data = ra.get_range_of_rows(gaustad_col_start, gaustad_col_end, gaustad_ref_data, use_np=True)
gaustad_peaks = ra.get_peaks(gaustad_data)
gaustad_np = np.array(gaustad_peaks)
peaks_only = gaustad_np[:, 2]


peaks_average = np.average(peaks_only)
print(peaks_average)

peaks_var = np.var(peaks_only)
peaks_sd = np.sqrt(peaks_var)
print(peaks_var)
print(peaks_sd)

alpha = 0.05
percentile = stats.norm.ppf(1-(alpha/2))
print(percentile)

h = percentile * peaks_sd

print(f"95% CI: {peaks_average} +- {round(h, 3)}")
print(f"[{round(peaks_average-h, 3)}, {round(peaks_average+h, 3)}]")

mu_0 = 2800

z = (peaks_average - mu_0) / ( peaks_sd / len(peaks_only) )


if mu_0 > percentile:
    print("Throw away H0")
else:
    print("Dont throw away H0")

qqplot(peaks_only, line="s")
plt.show()


x_gaustad = np.arange(len(gaustad_data[0][1]))
x_polle = np.arange(len(polle_data[0][1]))
x_engel = np.arange(len(engel_np[1]))
x_diver_1 = np.arange(len(diver_np_1[1]))
x_diver_2 = np.arange(len(diver_np_2[1]))

gaustad_data[0][1].reverse()
polle_data[0][1].reverse()
engel_np[1].reverse()
diver_np_1[1].reverse()
diver_np_2[1].reverse()

plt.barh(x_gaustad, gaustad_data[0][1], label="Gaustad swimming hall")
plt.barh(x_polle, polle_data[0][1], label="Pollesundet")
plt.barh(x_engel, engel_np[1], label="Engelsviken")
plt.barh(x_diver_1, diver_row_1[1], label="Diver test asuumably noise by bubbles")
plt.barh(x_diver_2, diver_row_2[1], label="Diver test no noise from bubbles")
plt.ylabel("Columns from csv", fontsize=20)
plt.xlabel("Recieved reflection intensity", fontsize=20)
ax = plt.gca()
ax.invert_yaxis()
plt.legend()
plt.show() 

#ra.plot_refletion_strength(diver_np_1)
#ra.plot_refletion_strength(diver_np_2)
#ra.plot_refletion_strength(engel_np)
#ra.plot_refletion_strength(gaustad_data[0])
#ra.plot_refletion_strength(polle_data[0])

#gaustad_data[0][1].reverse()
#ra.plot_refletion_strength(gaustad_data[0])