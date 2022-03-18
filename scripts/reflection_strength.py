import pandas as pd
from analysis import reflection_analysis

# Path to csv file
path = r"C:\Users\bjorn\Desktop\sonar\data\sonar_test.csv"
path_engelsviken = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\sonar.csv"
path_engelsviken_UDP = r"C:\Users\bjorn\Desktop\sonar\data\engelsviken_marine_11_03_2022\engelsviken_11_march_reflection_strength_narrow\bathymetry.csv"
path_b = r"C:\Users\bjorn\Desktop\sonar\data\bathymetry_test.csv"
# Path to store the sound profile.
path_2 = r"C:\Users\bjorn\Desktop\sonar\plots\sound_profile_3.txt"
# Loading the data set.
df_reflection_strength = pd.read_csv(path_engelsviken, delimiter=",", names=list(range(2000)))
df_UDP = pd.read_csv(path_engelsviken_UDP, delimiter=",")
depth=  df_UDP["depth"]

ra = reflection_analysis()

data_1 = ra.get_row_of_data(400, df_reflection_strength)

depth_list, reflect_list = ra.get_data_sets(1000, depth, df_reflection_strength)
corr = ra.correlation_test(depth_list, reflect_list)
print(corr)

ra.plot_refletion_strength(data_1)









   







