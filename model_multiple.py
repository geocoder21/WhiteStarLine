# IMPORTS
import tkinter as tk
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import timeit

import data_IO
# import icebergclass


# MODEL PARAMETERS
density = 900
lidperm = 10            # lidar units per metre
results = []
ice_radar = 0
url_rad2 = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white2.radar'
url_lid2 = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white2.lidar'


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
                volume += (lidar[y][x]/lidperm) 
    return(volume)

# define which areas are ice and add them on to a list
# *** DOESN'T YET WORK ***
def find_ice(radar):
    for y in range(1, len(radar), -1):
        for x in range(1, len(radar[y]), -1):
            ice= False
            if(radar[y-1][x-1]>=100): ice = True
            if(radar[y-1][x]>=100): ice = True
            if(radar[y-1][x+1]>=100): ice = True
            if(radar[y][x-1]>=100): ice = True
            if(radar[y][x]>=100): ice = True
            if(radar[y][x+1]>=100): ice = True
            if(radar[y+1][x-1]>=100): ice = True
            if(radar[y+1][x]>=100): ice = True
            if(radar[y+1][x+1]>=100): ice = True
            if(ice==True) and (radar[y][x]>0):
                ice_radar[y][x] +=1
    print(ice_radar)
    return(ice_radar)

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

new_radar = data_IO.create_radar(url_rad2)
# print(new_radar)                          # Test
# print()

new_lidar = data_IO.create_lidar(url_lid2)
# print(new_lidar)                          # Test

# find the ice
find_ice(new_radar)

# ASSESS WHICH AREAS ARE ICE AND CALCULATE MASS ABOVE SEA LEVEL

# print(find_volume([[0,100,200,300,0]], [[0,150,200,300,0]]))      # Test data: expecting 65
# print(find_volume(new_radar, new_lidar))                          # Test: expecting 14,415.5
mass_above = (find_volume(new_radar, new_lidar))*density
# print(mass_above)                                                 # Test: expecting 12,973,950


# CALCULATE TOTAL ICEBERG MASS

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10
total_mass = mass_above*10
# print(total_mass)                                     # Test: expecting 129,739,500 and match with GUI


# DISPLAY TOTAL MASS, VOLUME AND WHETHER ICEBERG CAN BE PULLED ON GUI


# set up GUI with root and title
root = tk.Tk()
root.wm_title("Iceberg tow model")

# create new figure with subplots
fig, (plot1, plot2) = plt.subplots(1,2,figsize=(9, 4))
# ax = fig.add_axes([0, 0, 1, 1])

# make a canvas
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# add text widget to display data
text = tk.Text(root, height=4, width=45, fg='navy')
text.pack()
text.insert(tk.END, "Total iceberg mass = " + str(total_mass) + " kg")
text.insert(tk.END, '\n')
text.insert(tk.END, "Total iceberg volume = " + str(total_mass/density) + " m3")
text.insert(tk.END, '\n')
text.insert(tk.END, '\n')
if ice_pull(total_mass) == True:
    text.insert(tk.END,"Iceberg can be towed")
else:
    text.insert(tk.END,"Iceberg is too large to be towed")

# add quit button
button = tk.Button(height=2, text='Quit', command=root.quit, bg='navy', fg='white')
button.pack()
button.place(x=770, y=415)

# plot radar data in subplot 1
plot1.set_ylim(300, 0)                        # y dimension limit
plot1.set_xlim(0, 300)                        # x dimension limit
plot1.set_title("Radar data")
plot1.set_xlabel("X")
plot1.set_ylabel("Y")
plot1.imshow(new_radar, cmap="plasma")

# plot lidar data in subplot 2
plot2.set_ylim(300, 0)                        # y dimension limit
plot2.set_xlim(0, 300)                        # x dimension limit
plot2.set_title("Lidar data")
plot2.set_xlabel("X")
plot2.set_ylabel("Y")
plot2.imshow(new_lidar, cmap="plasma")

canvas.draw()

tk.mainloop()

# SAVE INFORMATION TO A FILE


# TESTING AND TIMING 

if __name__ == "__main__":
    print("Timing for find_volume:")
    x = timeit.timeit("find_volume(new_radar, new_lidar)",
                    setup="from __main__ import find_volume,"
                    "new_radar, new_lidar",
                    number=1)
    print("{:15.15f}".format(x))                # Test: approx 0.013 seconds

    print("Timing for ice_pull:")
    y = timeit.timeit("ice_pull(total_mass)",
                    setup="from __main__ import ice_pull,"
                    "total_mass",
                    number=1)
    print("{:15.15f}".format(y))                # Test: approx 0.0000031 seconds
