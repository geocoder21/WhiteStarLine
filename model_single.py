# IMPORTS
import tkinter 
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# import icebergclass
import data_IO

# MODEL PARAMETERS
density = 900
# ice = []

# FUNCTIONS

# find total volume of ice
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

# assess whether the iceberg can be towed
def ice_pull(mass):
    if mass < 36000000:
        True
    else:
        False

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# set up backend correctly before fig is created
matplotlib.use('TkAgg')


# IMPORT RADAR AND LIDAR DATA

new_radar = data_IO.create_radar()
# print(new_radar)                          # Test
# print()

new_lidar = data_IO.create_lidar()
# print(new_lidar)                          # Test


# ASSESS WHICH AREAS ARE ICE AND CALCULATE MASS ABOVE SEA LEVEL

# print(find_volume([[0,100,200,300,0]], [[0,150,200,300,0]]))      # Test data: expecting 65
# print(find_volume(new_radar, new_lidar))                          # Test: expecting 14,415.5
mass_above = (find_volume(new_radar, new_lidar))*density
# print(mass_above)                                                 # Test: expecting 12,973,950


# CALCULATE TOTAL ICEBERG MASS

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10
total_mass = mass_above*10
# print(total_mass)                          # Test: expecting 129,739,500 and match with GUI


# DISPLAY total mass, total volume and whether iceberg can be pulled on GUI

# GUI code
root = tkinter.Tk()
root.wm_title("Iceberg tow model")

# create new figures
fig, (plot1, plot2) = plt.subplots(1,2,figsize=(8, 4))
# ax = fig.add_axes([0, 0, 1, 1])
# # ax.set_autoscale_on(False)

# make a canvas
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# add text widget to display data
text = tkinter.Text(root, height=4, width=40, fg='navy')
text.pack()
text.insert(tkinter.END, "Total iceberg mass = " + str(total_mass) + " kg")
text.insert(tkinter.END, '\n')
text.insert(tkinter.END, "Total iceberg volume = " + str(total_mass/900) + " m3")
text.insert(tkinter.END, '\n')
text.insert(tkinter.END, '\n')
if ice_pull(total_mass) == True:
    text.insert(tkinter.END,"Iceberg can be towed")
else:
    text.insert(tkinter.END,"Iceberg is too large to be towed")

# plt.ylim(0, 300)                        # y dimension limit
# plt.xlim(0, 300)                        # x dimension limit

plot1.set_ylim(300, 0)                        # y dimension limit
plot1.set_xlim(0, 300)                        # x dimension limit
plot1.set_title("Radar data")
plot1.set_xlabel("X")
plot1.set_ylabel("Y")
plot1.imshow(new_radar, cmap="plasma")

plot2.set_ylim(300, 0)                        # y dimension limit
plot2.set_xlim(0, 300)                        # x dimension limit
plot2.set_title("Lidar data")
plot2.set_xlabel("X")
plot2.set_ylabel("Y")
plot2.imshow(new_lidar, cmap="plasma")

canvas.draw()

tkinter.mainloop()

# SAVE INFORMATION TO A FILE
