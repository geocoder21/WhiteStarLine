# IMPORTS
import environment
import matplotlib 
import matplotlib.pyplot as plt
import tkinter 

# MODEL PARAMETERS


# FUNCTIONS

# ******************************************************************************************************************************
# MAIN PROGRAMME
# ******************************************************************************************************************************

# display radar data on plot
radar1 = environment.create_radar
plt.ylim(0, 300)                        # y dimension limit
plt.xlim(0, 300)                        # x dimension limit
plt.imshow(radar1)                      # radar plot
