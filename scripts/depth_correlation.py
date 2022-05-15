
from cmath import nan
import pandas as pd
from analysis import reflection_analysis
import numpy as np
import math

path_reflection_csv = r"C:\Users\bjorn\Desktop\sonar\data\femsjøen\test\sonar.csv"
path_bathymetric_csv = r"C:\Users\bjorn\Desktop\sonar\data\femsjøen\test\bathymetry.csv"

df_reflection_strength = pd.read_csv(path_reflection_csv, delimiter=",", names=list(range(2000)))
df_UDP = pd.read_csv(path_bathymetric_csv, delimiter=",", float_precision='round_trip')
depth=  df_UDP[["time", "depth"]]   

ra = reflection_analysis()
data = ra.get_range_of_rows(0, len(df_reflection_strength), df_reflection_strength)
peaks = ra.get_peaks(data)
#print(peaks)
np_depth = depth.to_numpy()

mapped = ra.map_reflection_strength_to_depth(np_depth, peaks)

d = [mapped[x][1] for x in range(len(mapped))]
r = [mapped[y][2] for y in range(len(mapped))]
#for k in range(len(mapped)):
#    d.append(mapped[k][1])
#    r.append(mapped[k][2])
        
 
ra.plot_reflection_strength_against_depth(d, r)

