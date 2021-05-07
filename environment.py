 # IMPORTS

import requests
import bs4


# create an iceberg environment
def create_lidar():
    lidar_single = []

    lidar1 = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = lidar1.text

    for row in lidar1:                     # A list of rows
        rowlist = []
        for value in row:				    # A list of value
            rowlist.append(value)           # Append values to rowlist
            # print(value) 				    # Prints floats
        lidar_single.append(rowlist)     # Append rowlist to environment

    file.close()
    return lidar_single
