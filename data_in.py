 # IMPORTS
import requests
import csv
# from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt


# FUNCTIONS

# read in radar data (single iceberg)
def create_radar():
    # Init variables
    radar_lst = []
    # Set URL of csv file
    url = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar'
  

    ############################################################## DOESN'T WORK
    # # Old code
    # radar_single = []
    
    # radar1 = requests.get(url, stream=True)
    # if radar1.status_code == 200:  
    #     for row in radar1.iter_lines():                     # A list of rows
    #     rowlist = []
    #     for value in row:				    # A list of value
    #         rowlist.append(value)           # Append values to rowlist
    #         # print(value) 				    # Prints floats
    #     radar_single.append(rowlist)     # Append rowlist to environment

    # print(radar_single)
    # return (radar_single)
    ##############################################################

    # ############################################################# WORKS: Method 1 using csv library
    # # Get data via URL request
    # radar_rawdata = requests.get(url).text.splitlines()
    
    # # read in data and convert numer strings to floats
    # radar_data = csv.reader(radar_rawdata, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

    # # So to convert to a 2D integer list (radar_data_lst), we will need to iterate over each value in radar_data and convert
    # for row in radar_data:
    #     row_lst = []
    #     # Convert floats to int
    #     for value in row:
    #         row_lst.append(int(value))
    #     # add newly converted row to radar_lst 
    #     radar_lst.append(row_list)
    # #############################################################
    
    # ********************************************************************************
    # Get data using pandas library
    # used instead of requests module + csv reader as more efficient code
    
    # Get data via URL request into a pandas DataFrame
    radar_data=pandas.read_csv(url)
    # Extract data from DataFrame and convert to 2D list
    radar_lst=radar_data.values.tolist()
    # #############################################################

    # Now we can return our radar data as a list of lists with integer values
    return(radar_lst)

# # read in lidar data (single iceberg)
# def create_lidar():
#     lidar_single = []

#     lidar1 = requests.get('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar')
#     content = lidar1.text

#     for row in content:                     # A list of rows
#         rowlist = []
#         for value in row:				    # A list of value
#             rowlist.append(value)           # Append values to rowlist
#             # print(value) 				    # Prints floats
#         lidar_single.append(rowlist)     # Append rowlist to environment

#     return (lidar_single)

new_radar = create_radar()
print(new_radar)
plt.imshow(new_radar)
plt.show()