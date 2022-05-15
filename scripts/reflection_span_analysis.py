from cmath import nan
import pandas as pd
from analysis import reflection_analysis
import numpy as np
import math
from matplotlib import pyplot as plt
import scipy.stats as stats
from datetime import datetime as dt

def prep_for_plot(peaks):
    r = []
    t = []

    for i in range(len(peaks)):
        r.append(peaks[i][2])
        t.append(peaks[i][0])
    np_t = np.array(t)
    np_r = np.array(r)
    
    return np_r, np_t


path_gaustad = r"C:\Users\bjorn\Desktop\sonar\data\gaustahallen\pm111\sonar.csv"
path_diver = r"C:\Users\bjorn\Desktop\sonar\data\dive_test_firedepartment\sonar.csv"
path_no_diver = r"C:\Users\bjorn\Desktop\sonar\data\dive_test_firedepartment\no_divers\sonar.csv"

df_gaustad = pd.read_csv(path_gaustad, delimiter=",", names=list(range(2000)))
df_diver = pd.read_csv(path_diver, delimiter=",", names=list(range(2000)))
df_no_diver = pd.read_csv(path_no_diver, delimiter=",", names=list(range(2000)))

gaustad_ref_data = df_gaustad.to_numpy()
diver_ref_data = df_diver.to_numpy()
no_diver_ref_data = df_no_diver.to_numpy()


# GAUSTADHALLEN
gaustad_t_1_start = 1647432735033
gaustad_t_1_end = 1647432747054
gaustad_col_start = 281
gaustad_col_end = 444

# Divers start stop times  
diver_1_start = dt(2022, 4,1, 15, 5, 52).timestamp() # 1648818352014 COL : 9008
diver_1_end = dt(2022, 4,1, 15, 6, 29).timestamp() # 1648818389041 COL : 9533
diver_1_col_start = 9008
diver_1_col_end = 9533

diver_2_start = dt(2022, 4,1, 15, 10, 17).timestamp() # 1648818617009 COL : 12545
diver_2_end = dt(2022, 4,1, 15, 10, 36).timestamp() # 1648818636049 COL : 12815
diver_2_col_start = 12545
diver_2_col_end = 12815

diver_3_start = dt(2022, 4,1, 15, 17, 53).timestamp() # 1648819073008 COL : 18792
diver_3_end = dt(2022, 4,1, 15, 18, 54).timestamp() # 1648819134005 COL : 19616
diver_3_col_start = 18792
diver_3_col_end = 19616

# No diver data start stop times
no_diver_1_start = dt(2022, 4, 5, 15, 51, 39).timestamp() # 1649166699038 COL : 773
no_diver_1_end = dt(2022, 4, 5, 15, 51, 46).timestamp() # 1649166706039 COL : 873
no_diver_1_col_start = 773
no_diver_1_col_end = 873

no_diver_2_start = dt(2022, 4, 5, 15, 54, 44).timestamp() # 1649166884750 COL : 2911
no_diver_2_end = dt(2022, 4, 5, 15, 55, 2).timestamp() # 1649166902048 COL : 3101
no_diver_2_col_start = 2911
no_diver_2_col_end = 3101

no_diver_3_start = dt(2022, 4, 5, 15, 56, 45).timestamp() # 1649167005028 COL : 4448
no_diver_3_end = dt(2022, 4, 5, 15, 57, 4).timestamp() # 1649167024020 COL : 4688
no_diver_3_col_start = 4448
no_diver_3_col_end = 4688


ra = reflection_analysis()
gaustad_data = ra.get_range_of_rows(gaustad_col_start, gaustad_col_end, gaustad_ref_data, use_np=True) #gaustad_ref_data  df_gaustad 
diver_1_data = ra.get_range_of_rows(diver_1_col_start, diver_1_col_end, diver_ref_data, use_np=True) #diver_ref_data df_diver
diver_2_data = ra.get_range_of_rows(diver_2_col_start, diver_2_col_end, diver_ref_data, use_np=True)
diver_3_data = ra.get_range_of_rows(diver_3_col_start, diver_3_col_end, diver_ref_data, use_np=True)

no_diver_1_data = ra.get_range_of_rows(no_diver_1_col_start, no_diver_1_col_end, no_diver_ref_data, use_np=True) #no_diver_ref_data  df_no_diver
no_diver_2_data = ra.get_range_of_rows(no_diver_2_col_start, no_diver_2_col_end, no_diver_ref_data, use_np=True)
no_diver_3_data = ra.get_range_of_rows(no_diver_3_col_start, no_diver_3_col_end, no_diver_ref_data, use_np=True)

gaustad_peaks = ra.get_peaks(gaustad_data)

diver_1_peaks = ra.get_peaks(diver_1_data)
diver_2_peaks = ra.get_peaks(diver_2_data)
diver_3_peaks = ra.get_peaks(diver_3_data)

no_diver_1_peaks = ra.get_peaks(no_diver_1_data)
no_diver_2_peaks = ra.get_peaks(no_diver_2_data)
no_diver_3_peaks = ra.get_peaks(no_diver_3_data)

r_gaustad, t_gaustad = prep_for_plot(gaustad_peaks)  

r_diver_1, t_diver_1 = prep_for_plot(diver_1_peaks)
r_diver_2, t_diver_2 = prep_for_plot(diver_2_peaks)
r_diver_3, t_diver_3 = prep_for_plot(diver_3_peaks)

r_no_diver_1, t_no_diver_1 = prep_for_plot(no_diver_1_peaks)
r_no_diver_2, t_no_diver_2 = prep_for_plot(no_diver_2_peaks)
r_no_diver_3, t_no_diver_3 = prep_for_plot(no_diver_3_peaks)



#plt.plot(t_gaustad, r_gaustad, "o")
#plt.plot(np_t_gaustad, m*np_t_gaustad+b)
#plt.show()

fig, axs = plt.subplots(2, 2)
fig.suptitle('Assumed detected diver')
axs[0][0].bar(t_gaustad, r_gaustad)
axs[0][0].set_title("Reflection intensity from detection in Gaustadhallen")
axs[0][1].bar(t_diver_1, r_diver_1)
axs[0][1].set_title("Reflection intensisty from figure 5.21.a")
axs[1][0].bar(t_diver_2, r_diver_2)
axs[1][0].set_title("Reflection intensisty from figure 5.22.a")
axs[1][1].bar(t_diver_3, r_diver_3)
axs[1][1].set_title("Reflection intensisty from figure 5.23.a")

fig2, axs2 = plt.subplots(1, 3)
fig2.suptitle('No diver present')
axs2[0].bar(t_no_diver_1, r_no_diver_1)
axs2[0].set_title("Reflection intensisty from figure 5.21.b")
axs2[1].bar(t_no_diver_2, r_no_diver_2)
axs2[1].set_title("Reflection intensisty from figure 5.22.b")
axs2[2].bar(t_no_diver_3, r_no_diver_3)
axs2[2].set_title("Reflection intensisty from figure 5.23.b")
fig.autofmt_xdate()
fig2.autofmt_xdate()
plt.tight_layout()
plt.show()




