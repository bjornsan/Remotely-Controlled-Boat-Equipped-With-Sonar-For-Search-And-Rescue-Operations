import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt


class reflection_analysis:
    def __init__(self):
        pass

    def get_data_sets(self, n, depth_data, reflection_data):

        # n number of rows to extact from csv
        #n = 1245

        # Initialazing a list to contain depth values from UDP file.
        depth_list = []

        # Appending n rows from UDP_csv to the depth list.
        for i in range(n):
            depth_list.append(depth_data[i])
        
        # List containing n rows of frequency strength from reflection strength csv.
        reflection_strength = self.get_range_of_rows(n, reflection_data)

        return depth_list, reflection_strength
    
    def get_range_of_rows(self, r, data):
        '''
            Gets and cleans r rows from the data set.

            Parameters: r: number of rows to get.
                        data: The data set.
            
            returns:    The cleaned up dataset
        '''
        tmp_array = []
        for i in range(r):
            time, row = self.get_row_of_data(i, data)
            tmp_array.append([time, row])
        return tmp_array

    def get_row_of_data(self, row_number, data_set):
        # Get a specific row in the data set. Parameters: dataset, row_start, row_end
        row = self.get_row(data_set, row_number, row_number+1)
        clean = self.clean_data_row(row)
        filter = self.smooth_data(clean[1])
        return [clean[0], filter]
    
    def get_row(self, data, start_row, stop_row):
        '''
        Get a specific row from data set

        Parameters: data: the data set
                    start_row: From this row
                    end_row: To this row
                
        Returns: The row
        '''
        row = []
        for i in range(start_row,stop_row):
            for j in range(2000):
                row.append(data[j][i])
        return row

    def clean_data_row(self, data):
        '''
            Cleans a row from faulty data.

            Parameters: data: row to clean
            
            Returns:    clean_data: The cleaned up data.
        '''
        clean_data = [] 
        for k in range(2):
            clean_data.append([])

        clean_data[0] = data[0]
        for i in range(1,len(data)): 
            if not math.isnan(data[i]):
                clean_data[1].append(int(data[i]))
        return clean_data

    def smooth_data(self, data):
        x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = 0
        smooth_data = []
        
        for tt in range(len(data)):
            smooth_data.append(0)

        for t in range(len(data)):
            if t < 3:
                x_1 = data[t]
                x_2 = data[t+1]
                x_3 = data[t+2]
                smooth_data[t] = round( ( (1 / 3) * (x_1 + x_2 + x_3) ), 2)
            elif t == len(data)-2 or t == len(data)-1 or t == len(data):
                x_1 = data[t]
                x_2 = data[t-1]
                x_3 = data[t-2]
                smooth_data[t] = round( ( (1 / 3) * (x_1 + x_2 + x_3) ), 2)
            else:
                x_1 = data[t-3]
                x_2 = data[t-2]
                x_3 = data[t-1]
                x_4 = data[t]
                x_5 = data[t+1]
                x_6 = data[t+2]
                x_7 = data[t+2]
                smooth_data[t] = round( ( (1 / 7) * (x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7) ), 2 )  
        
        return smooth_data  

    def correlation_test(self, depth_data, reflection_data):
        # Storing the number of columns per row into a list.
        # This is done to do a correlation test between depth in meters and the number of columns in the reflection strength data. 
        columns_per_row = []

        for row in reflection_data:
            columns_per_row.append(len(row))

        # Combining the depth in meters with the columns per row to make a simple visualization of the correlation.
        zipped = zip(depth_data, columns_per_row)

        x = depth_data
        y = columns_per_row

        avg_depth = self.smooth_data(x)
        avg_columns = self.smooth_data(y)

        correlation_matrix = np.corrcoef(avg_depth, avg_columns) 
        return correlation_matrix

    def plot_refletion_strength(self, data, save_plot=False):
        #####
        # Plotting a horizontal histogram of frequency strength at each depth.
        #
        x_2 = np.arange(len(data))
        plt.barh(x_2, data)
        plt.ylabel("Columns from csv", fontsize=20)
        plt.xlabel("Recieved reflection intensity", fontsize=20)
        ax = plt.gca()
        ax.invert_yaxis()
        plt.show() 

        # save plot to file  
        if save_plot:
            plt.savefig(r"C:\Users\bjorn\Desktop\sonar\Plots\test.png")

    def create_bins(self, start, stop, step):
        '''
            Create bins for use to plot.

            Parameters: start: first bin
                        stop: last bin
                        step: step between each bin
            
            Returns:    Array of bins.
        '''
        bins = []
        for i in range(start, stop, step):
            bins.append(i)
        return bins

    def print_sound_profile(self, data, length, path):
        '''
            Based on the length of the rows, prints the horizontal histogram to file.

            Parameters: data: The data set.
                        length: Length of the data set
                        path: path to store the sound profile.
            
            Returns: None
        '''
        for i in range(length):
            tmp = int( data[i] / 100 )
            for k in range(tmp):
                if k == tmp-1:
                    with open(path, "a") as f:
                        f.write("*")
                        f.write("\n")
                    print("*")
                with open(path, "a") as f:
                    f.write("*")
                print("*", end=" ")
   



class udp_analysis:   

    def __init__(self):
        pass

    def get_data(self, path):
        print(path)
        df = pd.read_csv(path, delimiter=",")
        data = df[["time", "depth", "latitude", "longtitude"]]
        clean = self.clean_row(data, "latitude")
        return clean

    def clean_row(self, data, key):
        cleaned_data = []
        idx = 0
        for row in data[key]:
            if not math.isnan(row):
                cleaned_data.append( [data["time"][idx], data["longtitude"][idx], row, data["depth"][idx]] )
            idx = idx+1
        return cleaned_data

    