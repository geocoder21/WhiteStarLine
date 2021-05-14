"""This model pulls in radar and lidar data from specified locations to
assess whether there is an iceberg within the specified 300m x 300m area.
The programme then uses dimensions to calculate total iceberg mass and
volume and whether it could be pulled by an iceberg-towing tug. This
information is displayed on a Graphical User Interface (GUI) and saved to a
text file.  The code is written in Python. The programme can be run with  the
data provided, but could also be used with alternative input data, output
filename and towing tolerances"""


# IMPORTS
import tkinter as tk            # GUI package
import matplotlib               # plotting package
import matplotlib.pyplot as plt
import datetime                 # package for including data and time
import timeit                   # timing package for testing
import doctest                  # code testing

import data_IO                  # functions for importing and exporting data


# MODEL PARAMETERS
density = 900           # density of ice in kg/m3
lidperm = 10            # lidar units per metre
max_tow = 36000000      # maximum towable mass in kg
url_rad = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar'
url_lid = 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar'
# addresses can be updated to pull in alternative data


# FUNCTIONS

# find total volume of ice
def find_volume(radar, lidar):
    # test conditions to check for when loop conditions are and are not met
    # test if radar value >=100 but lidar value is 0
    """
    >>> find_volume([[100]],[[100]])
    10.0
    >>> find_volume([[0]],[[100]])
    0.0
    >>> find_volume([[150]],[[0]])
    0.0
    """
   # radar value >=100 is ice
    # 10 lidar units = 1m
    # each pixel has area 1x1
    # so volume  = (lidar value/10) 
    volume = 0
    for y in range(len(radar)):
        for x in range(len(radar[y])):
            if radar[y][x] >= 100:
                volume += (lidar[y][x]/lidperm)
    return(float(volume))


# assess whether the iceberg can be towed
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
# can be updated to different web sources by updating addresses in parameters

new_radar = data_IO.create_radar(url_rad)
# print(new_radar)                          # Test
# print()

new_lidar = data_IO.create_lidar(url_lid)
# print(new_lidar)                          # Test


# ASSESS WHICH AREAS ARE ICE AND CALCULATE MASS ABOVE SEA LEVEL

# print(find_volume([[0,100,200,300]], [[0,150,200,300]]))    # Test: expecting 65
# print(find_volume(new_radar, new_lidar))                    # Test: expecting 14,415.5
mass_above = (find_volume(new_radar, new_lidar))*density
# print(mass_above)                                            # Test: expecting 12,973,950


# CALCULATE TOTAL ICEBERG MASS

# 10% of mass is above water, 90% below
# so total iceberg mass = mass above sea * 10
total_mass = mass_above*10
# print(total_mass)            # Test: expecting 129,739,500 and match with GUI


# DEFINE STATEMENTS FOR OUTPUTS
# defined here as used both in GUI and output file

mass_statement = "Total iceberg mass = " + str(total_mass) + " kg"
volume_statement = "Total iceberg volume = " + str(total_mass/density) + " m3"
if ice_pull(total_mass) == True:
    pull_statement = "Iceberg can be towed"
else:
    pull_statement = "Iceberg is too large to be towed"


# DISPLAY

# set up GUI with root and title
root = tk.Tk()
root.wm_title("Iceberg tow model")

# create new figure with subplots
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
# runs once 'quit'button clicked on GUI

date = str(datetime.datetime.now())
end_data = [date, mass_statement, volume_statement, pull_statement]
data_IO.write_out('iceberg_analysis.txt', end_data)


# TESTING AND TIMING

# 1. test timing for find_volume function
if __name__ == "__main__":
    print("Timing for find_volume:")
    x = timeit.timeit("find_volume(new_radar, new_lidar)",
    setup="from __main__ import find_volume,""new_radar, new_lidar", number=1)
    print("{:15.15f}".format(x))                # Test: approx 0.013-0.015 secs

# 2. test timing for ice_pull function
    print("Timing for ice_pull:")
    y = timeit.timeit("ice_pull(total_mass)", 
    setup="from __main__ import ice_pull,""total_mass", number=1)
    print("{:15.15f}".format(y))                # Test: approx 0.000003 secs

# 3. doctest for functions (above)
# test by typing 'python model_single.py -v' in command prompt
if __name__ == "__main__":
    doctest.testmod()