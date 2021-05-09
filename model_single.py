# IMPORTS
import matplotlib 
import matplotlib.pyplot as plt
import tkinter 
# import icebergclass
import data_IO

# MODEL PARAMETERS
volume = 0

# FUNCTIONS
def find_volume():
    for j in range(len(new_radar)):
        for i in range(len(new_radar[j])):
            if new_radar[j][i] >= 100:
                volume += (new_lidar[j][i]/10)
                

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# 1. Pull in lidar and radar data files and display them

new_radar = data_IO.create_radar()
# print("Radar values")
# print(new_radar)
# print()

new_lidar = data_IO.create_lidar()
print("Lidar values")
print(new_lidar)

plt.ylim(0, 300)                        # y dimension limit
plt.xlim(0, 300)                        # x dimension limit
# plt.imshow(new_radar)
plt.imshow(new_lidar)
plt.show()
# only displays radar data

#################################################
# 2. Assess which areas are ice using radar data
#    Assess total mass of ice above sea level

# radar value >=100 is ice
# 10 lidar units = 1m
# each pixel has area 1x1
# so volume for each pixel = (lidar value/10)
# then need to add all ice volume values together

find_volume()
print(volume)




#################################################
# 3. Calculate total iceberg mass

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10

#################################################
# 4. Calculate whether iceberg can be pulled

# bergs with total mass < 36 million kg can be pulled

#################################################
# 5. Display total mass, total volume and whether iceberg can be pulled on GUI

#################################################
# 6. Save information to a file
