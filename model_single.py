# IMPORTS
import matplotlib 
import matplotlib.pyplot as plt
import tkinter 
# import icebergclass
import data_IO

# MODEL PARAMETERS
density = 900
ice = []

# FUNCTIONS

def find_volume(radar, lidar):
    # radar value >=100 is ice
    # 10 lidar units = 1m
    # each pixel has area 1x1
    # so volume  = (lidar value/10)
    volume = 0
    for y in range(len(radar)):
        for x in range(len(radar[y])):
            if radar[y][x] >= 100:
                ice = True
                volume += (lidar[y][x]/10) 
    return(volume)

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# 1. Pull in lidar and radar data files

new_radar = data_IO.create_radar()
# print("Radar values")
# print(new_radar)
# print()

new_lidar = data_IO.create_lidar()
# print("Lidar values")
# print(new_lidar)

#################################################
# Assess which areas are ice using radar data
# Assess total mass of ice above sea level

# print(find_volume([[0,100,200,300,0]], [[0,150,200,300,0]]))      # Test: expecting 65
print(find_volume(new_radar, new_lidar))
mass_above = (find_volume(new_radar, new_lidar))*density
# print(mass_above)

# Calculate total iceberg mass

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10
total_mass = mass_above*10
print("Total mass is {} kg".format(total_mass))

#################################################
# 4. Calculate whether iceberg can be pulled

# bergs with total mass < 36 million kg can be pulled

#################################################
# 5. Display total mass, total volume and whether iceberg can be pulled on GUI

# plt.ylim(0, 300)                        # y dimension limit
# plt.xlim(0, 300)                        # x dimension limit
# # plt.imshow(new_radar)
# plt.imshow(new_lidar)
# plt.show()


#################################################
# 6. Save information to a file
