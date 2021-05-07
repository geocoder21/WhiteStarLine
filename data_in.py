 # IMPORTS
import requests

# FUNCTIONS

# read in radar data (single iceberg)
def create_radar():
    radar_single = []

    radar1 = requests.get('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar')
    type(radar1)
    content = radar1.text

    for row in content:                     # A list of rows
        rowlist = []
        for value in row:				    # A list of value
            rowlist.append(value)           # Append values to rowlist
            # print(value) 				    # Prints floats
        radar_single.append(rowlist)     # Append rowlist to environment

    print(radar_single)
    type(radar_single)
    return (radar_single)

# read in lidar data (single iceberg)
def create_lidar():
    lidar_single = []

    lidar1 = requests.get('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar')
    content = lidar1.text

    for row in content:                     # A list of rows
        rowlist = []
        for value in row:				    # A list of value
            rowlist.append(value)           # Append values to rowlist
            # print(value) 				    # Prints floats
        lidar_single.append(rowlist)     # Append rowlist to environment

    return (lidar_single)

create_radar