# IMPORTS
import matplotlib 
import matplotlib.pyplot as plt
import tkinter 
# import icebergclass
import data_IO

# MODEL PARAMETERS


# FUNCTIONS

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# pull in lidar and radar data files and display them
new_radar = data_IO.create_radar()
print("Radar values")
print(new_radar)
print()

new_lidar = data_IO.create_lidar()
print("Lidar values")
print(new_lidar)

plt.ylim(0, 300)                        # y dimension limit
plt.xlim(0, 300)                        # x dimension limit
plt.imshow(new_radar)
plt.imshow(new_lidar)
plt.show()
# only displays radar data
