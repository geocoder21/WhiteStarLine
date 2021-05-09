 # IMPORTS
import requests
import csv
# from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt


# FUNCTIONS

# read in radar data (single iceberg)
def create_radar():
    # Initiate variable
    radar_lst = []
    # Set URL of csv file
    url_rad = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar'
  
    # Get data using pandas library
    # used instead of requests module + csv reader as more efficient code

    # Get data via URL request into a pandas DataFrame
    radar_data=pandas.read_csv(url_rad)
    # Extract data from DataFrame and convert to 2D list
    radar_lst=radar_data.values.tolist()
    
    # return radar data as a list of lists with integer values
    return(radar_lst)


# # read in lidar data (single iceberg)
def create_lidar():
    # initiate variable
    lidar_lst = []
    # Set URL of csv file
    url_lid = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar'
    
   
    # Get data using pandas library
    
    # Get data via URL request into a pandas DataFrame
    lidar_data=pandas.read_csv(url_lid)
    # Extract data from DataFrame and convert to 2D list
    lidar_lst=lidar_data.values.tolist()
    # #############################################################

    # Now we can return our radar data as a list of lists with integer values
    return(lidar_lst)

new_radar = create_radar()
print(new_radar)
plt.imshow(new_radar)
plt.show()

new_lidar = create_lidar()
print(new_lidar)
plt.imshow(new_lidar)
plt.show()