import pandas as pd
from analysis import reflection_analysis

path_reflection_csv = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\sonar.csv"
path_bathymetric_csv = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\bathymetry.csv"

df_reflection_strength = pd.read_csv(path_reflection_csv, delimiter=",", names=list(range(2000)))
df_UDP = pd.read_csv(path_bathymetric_csv, delimiter=",")
depth=  df_UDP[["time", "depth"]]

ra = reflection_analysis()
#depth_list, reflect_list = ra.get_data_sets(1000, depth, df_reflection_strength)
#data_1 = ra.get_row_of_data( (len(df_reflection_strength)-1 ), df_reflection_strength)
data_2 = ra.get_range_of_rows(len(df_reflection_strength), df_reflection_strength)

#print(len(data_2))
#print(len(df_reflection_strength))

#print(data_2[0])

peak_at_column_nr = []
'''
for j in range(len(data_2)):
    max_intensity = 0
    value = 0

    for k in range(len(data_2[j][1])):
        data_2[j][1].reverse()
        if k == 0:
            max_intensity = k
        
        if data_2[j][1][k] > data_2[j][1][max_intensity]:
            max_intensity = k
            value = data_2[j][1][max_intensity]
            print(f"k: {k}\t\t{max_intensity}\t\t{value}")
    peak_at_column_nr.append([max_intensity, value, k])

print(peak_at_column_nr)
'''

#for l in range(len(data_2)):
#   data_2[l].append(peak_at_column_nr[l])


#for z in range(len(data_2[0])):
#    print(data_2[0][z])

#data_2[0][1].reverse()


max = 0
column_nr = 0
for hh in range(len(data_2[0][1])):
#for hh in range(len(cc)):    
    if data_2[0][1][hh] > max:
        print(f"hh: {hh}\t\tmax: {max}")
        max = data_2[0][1][hh]
        column_nr = hh
        
print(max, column_nr)


