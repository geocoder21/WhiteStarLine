# Program Development
```
The README in the project file outlines the task, context, and project contents.  Please read it first.
```
## Design process

### Algorithm
1. read in radar and lidar data
2. identify ice from radar data and for cells containing ice, extract lidar height data
3. assess total volume and mass of iceberg
4. assess whether the iceberg could be pulled
5. display file data and information on a graphical user interface (GUI)
6. write information out to a file

#### 1. Read in data
A new Python file, named 'towing_model.py' was created to contain the program. Since the functions for reading data in and writing out could be reused in a future program these were created in a separate file, named 'data_io.py', to then be imported into the main model.  The functions were therefore written so that web addresses could be updated in the main program as required.

The radar and lidar data for this task were supplied as separate raster files, covering a 300m by 300m area of sea.  The files were laid out in comma separated value (csv) format, with one line per image line and reading from top left of the grid to bottom right.

It was decided to use the pandas data manipulation library (The pandas development team, Feb 2020) to read in this data as this provided  more efficient code than the alternative of Python requests and csv reader modules.  Source documentation and other guides were used to develop code to read data into a pandas DataFrame and then extract this to a 2D list.  Two sites were used to assist in development of the 'read_data' function: https://pandas.pydata.org/ and https://datatofish.com/.

The web addresses for the raster data were entered within program parameters and the 'read_data' function called within the main programe for both radar and lidar data.  Once read in the data was printed and displayed on a test plot, using matplotlib; once checked the plot code was removed.

#### 2. Identify ice and extract lidar height data
```
Radar value >= 100 is ice
1 lidar unit = 10cm
```
Given the parameters provided within task guidance (above) it was possible to identify raster pixels that contained ice and then extract the lidar value. It was decided to include both elements within a single function in order to increase efficiency, so the 'find_volume' function first identifies pixels containing ice, and then adds the lidar value in metres for that pixel to a 'volume' variable.  Since each pixel has an area of 1m by 1m, this returns a cumulative volume value for the ice above the water.

This function is called within the main program, using the radar and lidar data read in during the previous step.

#### 3. Assess volume and mass of iceberg
```
10% of iceberg mass is above sea level
ice density = 900kg/m3
```
Volume and mass of the whole iceberg could then be caluculated ('total_volume' and 'total_mass' variables within the program).  Since this information would be required to be displayed on a GUI and written out to a file, these were defined as statements ('mass_statement' and 'volume_statement').


#### 4. Assess whether the iceberg could be pulled
```
iceberg mass > 36 million kg cannot be pulled
```
An 'ice_pull' function was developed to return a True or False Boolean value, depending on the total mass of the iceberg.  This included a 'max_tow' variable so that the value could be updated in program parameters if needed (e.g. if a more powerful iceberg-towing tug were available).  This was run through the main program, with the output entered into the 'pull_statement'.

#### 5. Display plots and information on a GUI
The task required display of both radar and lidar data, along with total mass and volume for the iceberg, and whether it could be pulled.  The data display was created using the matplotlib library and tkinter package; these standard Python packages allow data to be plotted and visualised within a GUI (Van Rossum, 2020).  

Reference was made to the course notes to set up a GUI and creating a canvas (Evans, 2021).  Further reading then allowed additional elements to be added, namely;

**a)  Two subplots with axis labels,** allowing radar and lidar data to be displayed side-by-side. The code was developed with reference to matplotlib documentation (Hunter et al, 2021a).

**b)  A text widget** to display mass, volume and whether the iceberg could be pulled.  This was developed with reference to the https://www.geeksforgeeks.org/ website.

**c)  A 'quit' button** to allow the user to exit the GUI and the program to complete.  During early testing it became apparent that the program did not complete unless the GUI was closed.  A quit button allows the user to close the GUI and for the program to complete correctly.  This was developed with reference to https://www.delftstack.com/, using root.quit.

Finally the colours of plots, text and widgets were updated to improve the appearance of the GUI.  This was achieved using the matplotlib 'List of named colours' (Hunter et al, 2021b).

#### 6. Write information out to a file
- 'naive' date included
- could also 

### Finalising and documenting code


### Testing 

- within source code
- doctest tests
- timing tests

### Issues and solutions
- ice_pull True / False issue: identified through testing that would always have been False as Return statements omitted
- volume function returned int 0 if for loop condition not met.  Again, identified through testing.

### Unresolved issues
- only works for single iceberg
- no error codes, e.g. if radar data >100 but lidar data is missing

## Further development

- Tidy code by removing tests where possible

## References

DelftStack, Dec 2020, Close a TkinterWindow With a Button. [Online]. [Accessed 17 May 2020]. Availabel from https://www.delftstack.com/howto/python-tkinter/how-to-close-a-tkinter-window-with-a-button/ 

Evans, A., 2021. Graphical User Interfaces (GUIS), University of Leeds [Online]. [Accessed 17 May 2020]. Available from https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/part10/index.html 

Hunter, J., Dale, D., Firing, E., Droettboom, M. and the Matplotlib development team, May 2021a. matplotlib.axes. [Online]. [Accessed 17 May 2020]. Available from https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes 

Hunter, J., Dale, D., Firing, E., Droettboom, M. and the Matplotlib development team, May 2021b. List of named colors. [Online]. [Accessed 17 May 2020]. Available from https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes  https://matplotlib.org/stable/gallery/color/named_colors.html 

The pandas development team, Feb 2020, 'pandas-dev/pandas: Pandas, Zenodo, https://doi.org/10.5281/zenodo.3509134

Van Rossum, G., 2020. The Python Library Reference, release 3.8.2, Python Software Foundation.v

* pandas https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table
* datatofish https://datatofish.com/convert-pandas-dataframe-to-list/
* https://www.geeksforgeeks.org/python-tkinter-text-widget/
