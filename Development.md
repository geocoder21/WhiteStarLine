# Program Development
```
The README in the project file outlines the task, context, and project contents.  Please read it first.
```
## Design process

### Algorithm
1. read in radar and lidar data
2. identify ice from radar data and for cells containing ice, extract lidar height data
3. assess total volume and mass of iceberg
4. display file data and information on a graphical user interface (GUI)
5. write information out to a file

#### Read in data
The radar and lidar data for this task were supplied as separate raster files, covering a 300m by 300m area of sea.  The files were laid out in comma separated value (csv) format, with one line per image line and reading from top left of the grid to bottom right.
It was decided to use the pandas data manipulation library to read in this data, as this provided  more efficient code than the alternative of Python requests and csv reader modules.  Since the functions for reading data in and writing out could be reused in a future program these were written in a separate file from the main code, named 'data_io.py'.


#### Identify ice and extract lidar height data

#### Assess volume and mass of iceberg


#### Display plots and information on a GUI


#### Write information out to a file
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
