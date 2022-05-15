import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
import scipy.stats as stats


class reflection_analysis:
    def __init__(self):
        pass

    def correlation_test(self, depth_data, reflection_data, n):
        '''
            Calculates the correleation matrix between n-columns in the reflection data and
            the actual measured depth in depth data.

            Parameters:
            --------------------
            depth_data (list) : List of measured depth
            reflection_data (list) : List of reflection intensity peaks

            Returns:
            --------------------
            correlation_matrix (list) : The correlation matrix
        '''

        peaks = [peak[2] for peak in reflection_data ]
        depth = depth_data[:n]

        x = depth
        y = peaks

        smooth_depth = self.smooth_data(x)
        smooth_reflection = self.smooth_data(y)

        correlation_matrix = np.corrcoef(smooth_depth, smooth_reflection) 
        return correlation_matrix
    
    def get_range_of_rows(self, start, end, data, use_np=False): 
        '''
            Gets and cleans rows between start and stop from the data set.

            Parameters:
            --------------------
            start (int) : The row number to start with
            end (int) : The row number to end with
            data (list) : The data set
            use_np (bool) : False if using the Pandas data fram, True if using a Numpy matrix.
            
            Returns:    
            --------------------
            cleaned_data_set (list) : The cleaned up data set
        '''
        cleaned_data_set = []
        for i in range(start, end, 1):
            time, row = self.get_processed_row_of_data(i, data, use_np)
            cleaned_data_set.append([time, row])
        return cleaned_data_set
        
    def get_processed_row_of_data(self, row_number, data_set, use_np=False):
        '''
            Processes a specific row in the data set.

            Parameters:
            --------------------
            row_number (int) : The row to get from the data set
            data_set (list) : The data set
            use_np (bool) : False if using the Pandas data fram, True if using a Numpy matrix.

            Returns:
            --------------------
            processed_row (list) : The cleaned and processed row

        '''
        row = self.get_row(data_set, row_number, use_np)
        clean = self.clean_data_row(row)
        filter = self.smooth_data(clean[1])
        #processed_row = [clean[0], clean[1]]
        processed_row = [clean[0], filter]
        return processed_row
    
    def get_row(self, data, start_row, use_np=False):
        '''
        Get a specific row from data set

        Parameters: 
        --------------------
        data (list) : the data set
        start_row (int) : Row to get
                
        Returns:
        --------------------
        row (list) : The row
        '''
        stop = start_row + 1

        row = []
        if use_np:
            for i in range(start_row, stop ):
                for j in range(2000):  
                    row.append(data[i][j])
        else:
            for i in range(start_row, stop ):
                for j in range(2000):  
                    row.append(data[j][i])
        return row
    
    def clean_data_row(self, data):
        '''
            Cleans a row from faulty data.

            Parameters:
            --------------------
            data (list): The row to clean
            
            Returns:
            --------------------    
            clean_data (list): The cleaned data
        '''
        clean_data = [] 
        for i in range(2):
            clean_data.append([])
        
        clean_data[0] = data[0]
        for j in range(1,len(data)): 
            if not math.isnan(data[j]):
                clean_data[1].append(int(data[j]))
        return clean_data

    def smooth_data(self, data):
        '''
            Smooths the data by a simple averaging filter.

            --------------------------------------------------------
            For x < 3 and x > n-3: 
                1/3 * (x_1 + x_2 + x_3)

            Else
                1/7 * (x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7)
            --------------------------------------------------------

            Parameters:
            --------------------
            data (list) : The data to smooth

            Returns:
            --------------------
            smooth_data (list) : The smoothened data
        '''
        x_1 = x_2 = x_3 = x_4 = x_5 = x_6 = x_7 = 0
        smooth_data = []
        
        for i in range(len(data)):
            smooth_data.append(0)

        for j in range(len(data)):
            if j < 3:
                x_1 = data[j]
                x_2 = data[j+1]
                x_3 = data[j+2]
                smooth_data[j] = round( ( (1 / 3) * (x_1 + x_2 + x_3) ), 2)
            elif j == len(data)-2 or j == len(data)-1 or j == len(data):
                x_1 = data[j]
                x_2 = data[j-1]
                x_3 = data[j-2]
                smooth_data[j] = round( ( (1 / 3) * (x_1 + x_2 + x_3) ), 2)
            else:
                x_1 = data[j-3]
                x_2 = data[j-2]
                x_3 = data[j-1]
                x_4 = data[j]
                x_5 = data[j+1]
                x_6 = data[j+2]
                x_7 = data[j+2]
                smooth_data[j] = round( ( (1 / 7) * (x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7) ), 2 )  
        
        return smooth_data  

    def get_peaks(self, data):
        '''
            Get the column nr for where the peak is in the CSV file. Also gets the value of the peak.

            The data in the CSV file is reversed, and must therefore first be reversed before looking
            for the peak.

            Parameters:
            --------------------
            data (2d list) : The data to find the peaks in

            Returns:
            --------------------
            peaks (2d list) : The list of peaks and corresponding values.
        '''
        peaks = []

        for i in range(len(data)):
            column_nr = 0
            value = 0

            reversed = data[i][1].copy()
            reversed.reverse()
            timestamp = int(data[i][0] / 1000)

            for j in range(len(reversed)):
    
                if j == 0:
                    column_nr = j
                
                if reversed[j] > value:
                    column_nr = j
                    value = reversed[column_nr]

            peaks.append([timestamp, column_nr, value])
            #print(peaks)

        return peaks
    
    def map_reflection_strength_to_depth(self, depth_data, reflection_data):
        '''
            Maps data from the batymetric  CSV to data from the sonar CSV, based on timestamp.

            Parameters:
            --------------------
            depth_data (list) : The depth data
            reflection_data (list) : The reflection data

            Returns:
            --------------------
            mapped (list) : list of the mapped data
        '''
        mapped = []

        for i in range(len(depth_data)):
            tmp = depth_data[i]
            for j in range(len(reflection_data)):
                if reflection_data[j][0] == int(tmp[0] / 1000):
                    tstamp = reflection_data[j][0]
                    tmp_depth = tmp[1]
                    tmp_ref = reflection_data[j][2]
                    mapped.append([tstamp, tmp_depth, tmp_ref])
        
        return mapped


    def plot_reflection_strength_against_depth(self, d, r):
        '''
            By using the returned list from map_reflection_strength_to_depth.

            Use matplotlib to plot reflection strength against depth.

            Parameters:
            --------------------
            data (list) : List containging timestamp, depth and reflection strength

            Returns:
            --------------------
            None
        '''
        d_2 = np.array(d)
        r_2 = np.array(r)

        m, b = np.polyfit(d_2, r_2, 1)
        m_2, b_2 = np.polyfit(np.log(d_2), r_2, 1)

        plt.plot(d_2, r_2, "o", label="Depth against assumed reflection intesity")
        plt.plot(d_2, m*d_2+b, linewidth=3, label="Linear regression fit")
        plt.plot(d_2, m_2*np.log(d_2)+b_2, label="Logaritmic regression fit")
        plt.xlabel("Depth in meters", fontsize=20)
        plt.ylabel("Reflection intensity", fontsize=20)
        plt.legend()
        plt.show()

    def plot_refletion_strength(self, data, save_plot=False, path=None):
        '''
            Plots a histogram of the reflection intesity at a given timestamp

            Parameters:
            --------------------
            data (list) : The data to plot
            save_plot (bool) : Option to save plot, False by standard.
            path (string) : The path to save the plot.

            Returns:
            --------------------
            None
        '''
        x_2 = np.arange(len(data[1]))
        plt.barh(x_2, data[1])
        plt.ylabel("Columns from csv", fontsize=20)
        plt.xlabel("Recieved reflection intensity", fontsize=20)
        ax = plt.gca()
        ax.invert_yaxis()
        plt.show() 

        if save_plot and path != None:
            plt.savefig(path)


class udp_analysis:   

    def __init__(self):
        pass

    def get_data(self, path):
        '''
            Get data from the CSV.

            Parameters:
            --------------------
            path (string) : The path to the CSV file

            Returns:
            --------------------
            clean (list) : The cleaned data set
        '''
        df = pd.read_csv(path, delimiter=",")
        data = df[["time", "depth", "latitude", "longitude"]]
        clean = self.clean_row(data, "latitude")
        return clean

    def clean_row(self, data, key):
        '''
            Cleans and structures the dataset in the proper way.

            Parameters:
            --------------------
            data (list) : The data set to clean
            key (string) : The key to clean on

            Returns:
            --------------------
            cleaned_data (list) : The cleaned data set
        '''
        cleaned_data = []
        idx = 0
        for row in data[key]:
            if not math.isnan(row):
                cleaned_data.append( [data["time"][idx], data["longitude"][idx], row, data["depth"][idx]] )
            idx = idx+1
        return cleaned_data

    