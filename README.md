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
- iceberg_analysis.txt      <i> Data output file </i>
</pre>
These are also available via https://github.com/geocoder21/WhiteStarLine 

## Usage

### Context
The software was developed to meet [a set of requirements](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/ice.html) to prevent collisions between ships and icebergs, as outlined above. 

#### Other applications
1. The program could be used to protect immovable objects at sea (such as wind farms and drilling platforms).  
2. There have also been investigations into towing icebergs to areas short of drinking water: https://www.whoi.edu/news-insights/content/can-icebergs-be-towed-to-water-starved-cities/ The program could identify those icebergs small enough to be towed.
3. This program could be adapted to assess the mass and volume of any partially submerged object.

### To run the program:
The code is written in Python 3. Once downloaded it can be run through an operating system command-line.
```
$ python towing_model.py
```
Alternatively it can be run through the Integrated Development Environment (IDE) of your choice, or the system file manager.

#### Use with alternative data
Example data sources are included within the code.  These could be updated, but the program would require the same parameters within the new data. 

The program requires radar and lidar (Light Detection and Ranging) data for a 300m by 300m raster grid, with measurements for each 1m2 pixel.
- Radar values of 100 or greater indicate ice
- Lidar values represent height of ice, with 10 units per metre

## Roadmap for further development
1. This program currently assumes that there is only one iceberg within the area.  A future development would be to add an iceberg class and create a list of individual icebergs, identified using a recursive flood and fill algorithm.  This would allow each iceberg's mass, volume and 'towability' to be assessed separately.
2. To meet any future demand for towing icebergs to cities without drinking water, a minimum viable ice volume could also be incorporated.  Ideally this would include a calculation for loss through melting during the journey.

Full details of development processes and testing are given elsewhere within this project.
```
development.md
```

## License
This project is available under the Apache 2.0 License.  See the LICENSE for further details.
