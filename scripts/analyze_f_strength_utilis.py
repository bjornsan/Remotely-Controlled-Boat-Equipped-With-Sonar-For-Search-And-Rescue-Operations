import numpy as np
import pandas as pd
import math

def get_row(data, start_row, stop_row):
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

def create_bins(start, stop, step):
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

def clean_data_row(data):
    '''
        Cleans a row from faulty data.

        Parameters: data: row to clean
        
        Returns:    clean_data: The cleaned up data.
    '''
    clean_data = []
    for i in range(1,len(data)): 
        if not math.isnan(data[i]):
            clean_data.append(int(data[i]))
    return clean_data

def get_range_of_rows(r, data):
    '''
        Gets and cleans r rows from the data set.

        Parameters: r: number of rows to get.
                    data: The data set.
        
        returns:    The cleaned up dataset
    '''
    tmp_array = []
    for i in range(r):
        row = get_row(data, i, i+1)
        clean = clean_data_row(row)
        tmp_array.append(clean)
    return tmp_array

def print_sound_profile(data, length, path):
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