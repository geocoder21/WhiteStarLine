"""
This model pulls in raster radar and lidar (Light Detection and Ranging) data
from given online locations to assess whether there is an iceberg within the
specified 300m x 300m area.

The programme uses dimensions to calculate total iceberg mass and
volume and whether it could be pulled by an iceberg-towing tug. This
information is displayed on a Graphical User Interface (GUI) and saved to a
text file.

The code is written in Python. It can be run through an operating system
command-line, an IDE, or a system file manager.

The programme can be run with the data provided,
but could also be used with alternative input data, output
filename and towing tolerances."""


# IMPORTS

import tkinter as tk            # GUI library
import matplotlib               # plotting library
import matplotlib.pyplot as plt
import datetime                 # to include data and time in code
import timeit                   # timing for testing
import doctest                  # code testing

import data_io                  # functions for importing and writing out data


# MODEL PARAMETERS

# included here so can be updated if required
max_tow = 36000000      # maximum towable mass in kg
url_rad = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar'
url_lid = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar'


# FUNCTIONS

"""
find_volume

Returns total volume of ice above sea level within the area by identifying
which squares contain ice (radar value > 100) and then extracting height
data from lidar readings for that pixel square.

10 lidar units per m, and each square is 1m x 1m, so volume = lidar height
value /10. Returns cumulative volume of ice above water level.

Tests to check for when loop conditions are and are not met, or
if radar value >=100 but lidar value = 0 (NB would indicate incorrect
data).


ice_pull

Calculates whether total iceberg mass exceeds max towable mass (36,000,000kg).
Returns True or False.

Tests for values >, = and < max mass
"""


def find_volume(radar, lidar):
    """
    >>> find_volume([[100]],[[210]])
    21.0
    >>> find_volume([[99]],[[100]])
    0.0
    >>> find_volume([[0]],[[100]])
    0.0
    >>> find_volume([[150]],[[0]])
    0.0
    """
    volume = 0
    for y in range(len(radar)):
        for x in range(len(radar[y])):
            if radar[y][x] >= 100:
                volume += (lidar[y][x] / 10)    # 10 lidar units per m
    return(float(volume))


def ice_pull(mass):
    """
    >>> ice_pull(1000)
    True
    >>> ice_pull(36000000)
    False
    >>> ice_pull(36000001)
    False
    """
    if mass < max_tow:
        return True
    else:
        return False


# **************************************************************************************
# MAIN PROGRAMME
# **************************************************************************************

# set up backend correctly before fig is created
matplotlib.use('TkAgg')


# IMPORT RADAR AND LIDAR DATA
# using functions from imported data_io

new_radar = data_io.read_data(url_rad)

new_lidar = data_io.read_data(url_lid)

# Tests
# print(new_radar)
# print(new_lidar)
# print(find_volume([[0,100,200,300]], [[0,150,200,300]]))  # expecting 65
# print(find_volume(new_radar, new_lidar))              # expecting 14,415.5


# ASSESS WHICH AREAS ARE ICE AND CALCULATE MASS ABOVE SEA LEVEL

volume_above = (find_volume(new_radar, new_lidar))
# print(volume_above)           # Test: expecting 12,973,950


# CALCULATE TOTAL ICEBERG MASS

# 10% of mass is above water, 90% below
total_volume = volume_above * 10
# print(total_mass)            # Test: expecting 144155 and match with GUI

total_mass = total_volume * 900     # density = 900 kg/m3
# print(total_mass)            # Test: expecting 129,739,500 and match with GUI


# DEFINE STATEMENTS FOR OUTPUTS
# defined here for ease of use in both GUI and output file

mass_statement = "Total iceberg mass = " + str(total_mass) + " kg"
volume_statement = "Total iceberg volume = " + str(total_volume) + " m3"
if ice_pull(total_mass) is True:
    pull_statement = "Iceberg can be towed"
else:
    pull_statement = "Iceberg is too large to be towed"


# DISPLAY

# set up GUI with root and title
root = tk.Tk()
root.wm_title("Iceberg tow model")

# create new figure with two subplots
fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(9, 4))
# ax = fig.add_axes([0, 0, 1, 1])

# make a canvas
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# add text widget to display data
text = tk.Text(root, height=4, width=45, fg='navy')
text.pack()
text.insert(tk.END, mass_statement)
text.insert(tk.END, '\n')
text.insert(tk.END, volume_statement)
text.insert(tk.END, '\n')
text.insert(tk.END, '\n')
text.insert(tk.END, pull_statement)

# add quit button
button = tk.Button(height=2, text='Quit', command=root.quit, bg='navy',
    fg='white')
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
# runs once 'quit' button clicked on GUI

date = str(datetime.datetime.now())
end_data = [date, mass_statement, volume_statement, pull_statement]
data_io.write_data('iceberg_analysis.txt', end_data)


# **************************************************************************************
# TESTING AND TIMING
# **************************************************************************************

if __name__ == "__main__":

    # 1. test timing for find_volume function

    print("Timing for find_volume:")
    x = timeit.timeit("find_volume(new_radar, new_lidar)",
        setup="from __main__ import find_volume,""new_radar, new_lidar",
        number=1)
    print("{:15.15f}".format(x))     # approx 0.013-0.015 secs

    # 2. test timing for ice_pull function

    print("Timing for ice_pull:")
    y = timeit.timeit("ice_pull(total_mass)",
        setup="from __main__ import ice_pull,""total_mass", number=1)
    print("{:15.15f}".format(y))                # approx 0.000003 secs

    # 3. doctest for functions (above)

    # test by typing 'python model_single.py -v' in command prompt
    # should run 7 tests correctly, as set under functions
    doctest.testmod()
