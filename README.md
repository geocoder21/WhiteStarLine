# White Star Line Iceberg Analysis
 
## Description
This project assesses whether an area of sea contains icebergs.  Where icebergs are found, it calculates volume and mass of ice. 
The aim is to identify icebergs that are small enough to be towed using a specialised iceberg-towing tug vessel.

The information is presented on a Graphical User Interface (GUI) and is also written out to a text file.

## Project Contents
<pre>
- README.md                 <i> This document </i>
- development.md            <i> Project design, summary of testing, and ideas for further development</i>
- towing_model.py           <i> Model </i>
- data_io.py                <i> Code for reading in and writing out data </i>
- License                   <i> Apache 2.0 license </i>
</pre>


## Usage

### Context
The project could be used to protect shipping and immovable objects at sea (such as wind farms and drilling platforms).  There have also been suggestions that icebergs be towed to areas short of drinking water: https://www.whoi.edu/news-insights/content/can-icebergs-be-towed-to-water-starved-cities/

### Use with alternative data
Example data sources are included within the code.  These could be updated, but the programme would require the same parameters within the new data. 

The programme requires radar and lidar (Light Detection and Ranging) data for a 300m by 300m raster grid, with data measured for each 1m2 pixel.
- Radar values of 100 or greater indicate ice
- Lidar values represent height of ice, with 10 units per metre

### To run the programme:
The code is written in Python 3. Once downloaded it can be run through an operating system command-line.
```
$ python towing_model.py
```
Alternatively it can be run through the Integrated Development Environment (IDE) of your choice, or the system file manager.

## Development and testing
The software was developed to meet [a set of requirements](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/ice.html). Full details of development processes and testing are given elsewhere within this project.
```
development.md
```

### Roadmap for further development
This programme currently assumes that there is only one iceberg within the area.  A future development would be to add an iceberg class and create a list of individual icebergs, identified using a recursive flood and fill algorithm.  This would allow each iceberg's mass, volume and 'towability' to be assessed separately.

## License
This project is available under the Apache 2.0 License.  See the LICENSE for further details.
