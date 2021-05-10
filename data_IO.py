 # IMPORTS

import pandas

# *********************************************************************************************************************************************
# FUNCTIONS


# Read in radar data (single iceberg)

def create_radar(url_name):
    # Initiate variable
    radar_lst = []
    
    # Get data using pandas library
    # used instead of requests module + csv reader as more efficient code

    # Get data via URL request into a pandas DataFrame
    radar_data=pandas.read_csv(url_name)
    # Extract data from DataFrame and convert to 2D list
    radar_lst=radar_data.values.tolist()
        # return radar data as a list of lists with integer values
    return(radar_lst)


# Read in lidar data (single iceberg)

def create_lidar(url_name):
    # initiate variable
    lidar_lst = []
        
    # Get data via URL request into a pandas DataFrame
    lidar_data=pandas.read_csv(url_name)
        # Extract data from DataFrame and convert to 2D list
    lidar_lst=lidar_data.values.tolist()
    # return lidar data as a list of lists with integer values
    return(lidar_lst)


# Read out data to a file
# def write_out():           
# end_data=pandas.to_csv('Data_out.csv', newline=' ')            # TO BE DONE
