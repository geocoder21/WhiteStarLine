# Program Development
```
The README in the project file outlines the task, context, and project contents.  Please read it first.
```
## Design process

### Algorithm
- read in data
- identify ice from radar data and for cells containing ice, extract lidar height data
- assess total volume and mass of iceberg
- display file data and information on a graphical user interface (GUI)
- write information out to a file

#### Read in
- data_io separate as can be reused
- pandas used instead of requests module + csv reader as more efficient code

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
