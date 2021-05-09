# IMPORTS
import matplotlib 
import matplotlib.pyplot as plt
import tkinter 
# import icebergclass
import data_IO

# MODEL PARAMETERS
density = 900
# ice = []

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
                # ice = True
                volume += (lidar[y][x]/10) 
    return(volume)


def ice_pull(mass):
    if mass < 36000000:
        True
    else:
        False

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# IMPORT RADAR AND LIDAR DATA

new_radar = data_IO.create_radar()
# print("Radar values")
# print(new_radar)
# print()

new_lidar = data_IO.create_lidar()
# print("Lidar values")
# print(new_lidar)


# ASSESS WHICH AREAS ARE ICE AND CALCULATE MASS ABOVE SEA LEVEL

# print(find_volume([[0,100,200,300,0]], [[0,150,200,300,0]]))      # Test: expecting 65
print(find_volume(new_radar, new_lidar))
mass_above = (find_volume(new_radar, new_lidar))*density
# print(mass_above)


# CALCULATE TOTAL ICEBERG MASS

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10
total_mass = mass_above*10
print("Total iceberg mass {} kg".format(total_mass))


# CALCULATE WHETHER ICEBERG CAN BE PULLED

# bergs with total mass < 36 million kg can be pulled
if ice_pull(total_mass) == True:
    print("Iceberg can be towed")
else:
    print("Iceberg is too large to be towed")

# 5. DISPLAY total mass, total volume and whether iceberg can be pulled on GUI

# plt.ylim(0, 300)                        # y dimension limit
# plt.xlim(0, 300)                        # x dimension limit
# plt.imshow(new_radar)
# plt.imshow(new_lidar)
# plt.show()



# SAVE INFORMATION TO A FILE
