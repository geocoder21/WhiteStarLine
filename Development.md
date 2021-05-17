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
Since the functions for reading data in and writing out could be reused in a future program these were written in a separate file from the main code, named 'data_io.py'.  The functions were therefore written so that web addresses could be updated in the main program as required.

The radar and lidar data for this task were supplied as separate raster files, covering a 300m by 300m area of sea.  The files were laid out in comma separated value (csv) format, with one line per image line and reading from top left of the grid to bottom right.

It was decided to use the pandas data manipulation library to read in this data, as this provided  more efficient code than the alternative of Python requests and csv reader modules.  Source documentation and other guides were used to develop code to read data into a pandas DataFrame and then extract this to a 2D list.  The two sites used to develop the read_data function were https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table and https://datatofish.com/convert-pandas-dataframe-to-list/ 

The web addresses for the raster data were entered within program parameters and the 'read_data' function called within the main programe for both radar and lidar daa.  Once read in the data was printed and displayed on a test plot, using matplotlib; once checked the plot code was removed.

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
It was then possible to calculate the volume and mass of the whole iceberg ('total_volume' and 'total_mass' variables within the program).  

Since this information would be required to be displayed on a GUI and written out to a file, these were defined as statements.


#### 4. Assess whether the iceberg could be pulled
```
iceberg mass > 36 million kg cannot be pulled
```
An 'ice_pull' function was developed to return a boolean value (True or False), depending on the total mass of the iceberg.  This included a 'max_tow' variable so that the value could be updated in program parameters if needed (e.g. if a more powerful iceberg-towing tug were available).

#### 5. Display plots and information on a GUI


#### 6. Write information out to a file
- 'naive' date included
- could also 


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

Tidy code by removing tests where possible

## References

https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table
https://datatofish.com/convert-pandas-dataframe-to-list/
