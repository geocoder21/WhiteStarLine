# Program Development

> The README in the project file outlines the task, context, and project contents.  Please read it first.


## Design process

### Algorithm
The following algorithm was prepared to meet the task requirements:

1. read in radar and lidar data
2. identify ice from radar data and for cells containing ice, extract lidar height data
3. assess total volume and mass of iceberg
4. assess whether the iceberg could be pulled
5. display file data and information on a graphical user interface (GUI)
6. write information out to a file

#### 1. Read in data
A new Python file, named 'towing_model.py' was created to contain the program. Since the functions for reading data in and writing out could be reused in a future program these were created in a separate file, named 'data_io.py', to then be imported into the main model.  The functions were therefore written so that web addresses could be updated in the main program as required.

The radar and lidar data for this task were supplied as separate raster files, covering a 300m by 300m area of sea.  The files were laid out in comma separated value (csv) format, with one line per image line and reading from top left of the grid to bottom right.

It was decided to use the *pandas* data manipulation library (the pandas development team, Feb 2020) to read in this data as this provided  more efficient code than the alternative combination of Python *requests* and *csv reader* modules.  Source documentation and other guides were used to develop code to read data into a pandas DataFrame and then extract this to a 2D list.  Two sites were used to assist in development of the 'read_data' function: https://pandas.pydata.org/ and https://datatofish.com/.

The web addresses for the raster data were entered within program parameters and the 'read_data' function called within the main programe for both radar and lidar data.  Once read in the data was printed and displayed on a test plot, using matplotlib; once checked the plot code was removed.


#### 2. Identify ice and extract lidar height data
> Radar value >= 100 is ice
>
> 1 lidar unit = 10cm

Given the parameters provided within task guidance (above) it was possible to identify raster pixels that contained ice and then extract the lidar value. It was decided to include both elements within a single function in order to increase efficiency, so the 'find_volume' function first identifies pixels containing ice, and then adds the lidar value in metres for that pixel to a 'volume' variable.  Since each pixel has an area of 1m by 1m, this returns a cumulative volume value for the ice above the water.

This function is called within the main program, using the radar and lidar data read in during the previous step.


#### 3. Assess volume and mass of iceberg
> 10% of iceberg mass is above sea level
>
> ice density = 900kg/m3

Volume and mass of the whole iceberg could then be caluculated ('total_volume' and 'total_mass' variables within the program).  Since this information would be required to be displayed on a GUI and written out to a file, these were defined as statements ('mass_statement' and 'volume_statement').


#### 4. Assess whether the iceberg could be pulled
> iceberg mass > 36 million kg cannot be pulled

An 'ice_pull' function was developed to return a True or False Boolean value, dependent on the total mass of the iceberg.  This included a 'max_tow' variable so that the value could be updated in program parameters if needed (e.g. if a more powerful iceberg-towing tug were available).  This was run through the main program, with the output entered into the 'pull_statement'.


#### 5. Display plots and information on a GUI
The task required display of both radar and lidar data, along with total mass and volume for the iceberg, and whether it could be pulled.  The data display was created using *matplotlib* external library and *tkinter* standard library; these allow data to be plotted and visualised within a GUI (Van Rossum, 2020).  

A basic canvas was created with reference to the course notes (Evans, 2021).  Further reading then allowed additional elements to be added, namely;

**-  Two subplots with axis labels,** allowing radar and lidar data to be displayed side-by-side. The code was developed with reference to matplotlib documentation (Hunter et al, 2021a).

**-  A text widget** to display mass, volume and whether the iceberg could be pulled.  This was developed with reference to the https://www.geeksforgeeks.org/ website.

**-  A 'quit' button** to allow the user to exit the GUI and the program to complete.  During early testing it became apparent that the program did not complete unless the GUI was closed.  A quit button allows the user to close the GUI and for the program to complete correctly.  This was developed with reference to https://www.delftstack.com/, using 'root.quit'.

Finally the colours of plots, text and widgets were updated to improve the appearance of the GUI.  This was achieved with reference to the *matplotlib* 'List of named colours' (Hunter et al, 2021b).


#### 6. Write information out to a file
A 'write_data'function was created in the 'data_io.py'file, using the 'open' method to create a new file, and mode 'w'to write or overwrite to that location (Python Foundation, May 2021a).  

It was decided to include the current date in the file written out; this provides context for the data and also allows the user to check that the output file was updated correctly.  In order to achieve this the *datetime* module was imported and a date variable created.  This produced a 'naive' date - however the code could be updated to account for different time zones if required. The output file was named 'iceberg_analysis.txt', but again this could be renamed for future use.


### Testing 
Three principle types of testing were employed in development of the program: 

1. Firstly, tests were written within source code and performed as each section of the program was developed.  These either tested the program data or dummy data sets to check whether the code produced expected results.  The majority of these tests were then commented out so as to be available for future amendments. 

2. Timing tests were included for the 'find_volume' and 'ice_pull' functions, using the imported *timeit* module.  This tests the time taken to run a small segment of code within a program, in this case producing a result in seconds and milliseconds. The code was written with reference to the Python Library (Python Software Foundation, May 2021c) and https://www.guru99.com/.

3. Finally, the *doctest* module was imported and tests built into the functions within the main program.  This allowed for testing of a range of conditions. Further information on *doctest* is available through the Python Library (Python Software Foundation, May 2021d), and in addition Tagliaferri (2021) was referenced in order to formulate the tests.


### Finalising and documenting code
Docstrings were added to the code to increase usability for other users of the code, written in line with PEP 257 (Goodger, Jun 2001).  A linter was then used in the IDE to ensure that the code was compliant with PEP 8 wherever possible (Van Rossum et al, Aug 2013).  Additional in-line comments were included where clarification might be necessary, and the majority of tests commented out to reduce processing time.  Finally the Apache 2.0 license was selected and a README file created to facilitate sharing through GitHub.  The markdown documents were created with reference to Cone's (2021) guide to syntax.


## Issues and solutions
A number of issues were identified through development and testing of the code.  The most significant of these are outlined below.

### Resolved issues

- **ice_pull function output**. the function was initially written as follows:
```
def ice_pull(mass):
    if mass < max_tow:
        True
    else:
        False
```
When the program was run the function appeared to be working, as the large iceberg gained a False output.  However, the *bloctest* on this function showed that no value was being returned, so the function defaulted to False.  The function was updated to include `return True` and `return False` and then worked correctly.

- **volume function output**. The oringal code for this function was as follows:
```
def find_volume(radar, lidar):
    volume = 0
    for y in range(len(radar)):
        for x in range(len(radar[y])):
            if radar[y][x] >= 100:
                volume += (lidar[y][x] / 10)    
    return(volume)
```
Again, this appeared to work correctly during debugging, but an issue was highlighted through *doctest*.  It became apparent that if the 'for loop' condition was not met then an integer value of 0 was returned, but if the condition was met then a float was returned.  This was overcome by updating the final line to `return(float(volume))`

- **program not completing**: initially the program did not stop unless the user manually closed the GUI.  This issue was overcome by adding a 'quit' button to the GUI (also see above).


### Unresolved issues

- The program only works for a single iceberg, or to calculate the total mass of ice within a set area - however this would not allow the 'ice_pull' function to work correctly.  Work began on updating the model to work for multiple icebergs but could not be completed within time constraints (see 'Further development' below)
- During testing it was seen that the program did could not identify incorrect data, e.g. if the radar value for a pixel was greater than 100 but lidar value was 0.  It would be beneficial to build in error checks to overcome this problem.
- When radar and lidar data was first displayed on *matplotlib* spot values could be obtained by hovering the mouse over an area, however replotting within a *tkinter* GUI removed this functionality. A solution was not found within the required timescale to resolve this.


## Further development

#### Mulitple icebergs and colour coding

An extension task was to get the program to work where multiple icebergs were present within the study area, and colour them red or green on the display, depending on whether or not they could be pulled. As identified above, this could not be completed at this stage.  Initial working on this problem identified that the solution would need an iceberg class to be created, containing attributes such as 
    - maximum and minimum coordinates (for x and y)
    - area, mass and volume
    - whether it could be pulled

A new 2D list would need to be set up, and icebergs identified as separate entities.  Use of a recursive flood and fill algorithm was investigated for this, but code was not yet forumalted.  Once icebergs were established as individual masses, their individual properties could be assessed through an updated program. 

#### 3D plot for lidar display

It would be interesting to add a 3D plot for the lidar data, to show contours above sea level.  Some investigation was carried out into this, using the *tkinter* wireframe, however the code was not developed sufficiently to be included.

#### More interactive GUI

It would be useful to have a more interactive GUI, for example adding a slider to alter the maximum mass that could be pulled.

#### Error checks

As identified under 'Unresolved issues' above, the program would benefit from additional code to produce error messages under certain circumstances.  The principle benefit would be to identify an error in the radar and lidar data, especially if sources were to be updated.

## References

Cone, M. 2021. *Markdown Guide: Basic Syntax*. [Online]. [Accessed 18 May 2021]. Available from https://www.markdownguide.org/basic-syntax/ 

Data to Fish website, July 2020. *How to Convert Pandas DataFrame into a List*. [Online]. [Accessed 17 May 2021]. Available from https://datatofish.com/convert-pandas-dataframe-to-list/

DelftStack, Dec 2020, *Close a Tkinter Window With a Button*. [Online]. [Accessed 17 May 2020]. Available from https://www.delftstack.com/howto/python-tkinter/how-to-close-a-tkinter-window-with-a-button/ 

Evans, A. 2021. *Graphical User Interfaces (GUIS)*, University of Leeds [Online]. [Accessed 17 May 2020]. Available from https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/part10/index.html 

GeeksforGeeks website, Mar 2020. *Python Tkinter - Text Widget*. [Online]. [Accessed 17 May 2021]. Available from https://www.geeksforgeeks.org/python-tkinter-text-widget/

Goodger, D. Jun 2001. *PEP 257 -- Docstring Conventions*, Python Software Foundation. [Online]. [Accessed 17 May 2021]. Available from https://www.python.org/dev/peps/pep-0257/

Guru99 website. *Python Timeit() with examples* [Online]. [Accessed 17 May 2021]. Available from https://www.guru99.com/timeit-python-examples.html

Hunter, J., Dale, D., Firing, E., Droettboom, M. and the Matplotlib development team. May 2021a. *matplotlib.axes*. [Online]. [Accessed 17 May 2020]. Available from https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes 

Hunter, J., Dale, D., Firing, E., Droettboom, M. and the Matplotlib development team. May 2021b. *List of named colors*. [Online]. [Accessed 17 May 2020]. Available from https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes  https://matplotlib.org/stable/gallery/color/named_colors.html 

The pandas development team, Feb 2020, 'pandas-dev/pandas: Pandas, Zenodo, Available from https://doi.org/10.5281/zenodo.3509134

The pandas development team, *IO tools* [Online]. [Accessed 17 May 2021]. Available from https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

Python Software Foundation, May 2021a. *Input and Output* [Online]. [Accessed 17 May 2021]. Available from https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files 

Python Software Foundation, May 2021b. *Reading and Writing Files* [Online]. [Accessed 17 May 2021]. Available from https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

Python Software Foundation, May 2021c. *timeit - Measure execution timeof small code snippets.* [Online]. [Accessed 17 May 2021]. Available from https://docs.python.org/3/library/timeit.html

Python Software Foundation, May 2021d. *doctest - Test interactive Python examples.* [Online]. [Accessed 17 May 2021]. Available from https://docs.python.org/3/library/timeit.html

Tagliaferri, L. Feb 2021. *How To Write Doctests in Python*. [Accessed 17 May 2021]. Available from https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python

Van Rossum, G., Warsaw, B., Coghlan, N. Aug 2013. *PEP 8 -- Style Guide for Python Code*, Python Software Foundation.  [Online]. [Accessed 17 May 2021]. Available fromhttps://www.python.org/dev/peps/pep-0008/

Van Rossum, G., 2020. *The Python Library Reference*, release 3.8.2, Python Software Foundation.v
