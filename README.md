# White Star Line Iceberg Analysis
 
## Description
This project assesses whether an area of sea contains icebergs.  Where icebergs are found, it calculates volume and mass of ice. 
The aim is to identify icebergs that are small enough to be towed using a specialised iceberg-towing tug vessel.  

## Installation

## Usage
The project could be used to protect shipping and immovable objects at sea (such as wind farms and drilling platforms).  There have also been suggestions that icebergs be towed to areas short of drinking water: https://www.whoi.edu/news-insights/content/can-icebergs-be-towed-to-water-starved-cities/

Example data sources are included within the code.  These could be updated, but the programme would require the same parameters within the new data. 

The programme requires radar and lidar (Light Detection and Ranging) data for a 300m by 300m raster grid, with data measured for each 1m2 pixel.
- Radar values of 100 or greater indicate ice
- Lidar values represent height of ice, with 10 units per metre

## Development and testing
Further details of development processes and testing are given within this project.
```
development.md
```

## Roadmap
This programme currently assumes that there is only one iceberg within the area.  A future development would be to add an iceberg class and create a list of individual icebergs, identified using a recursive flood and fill algorithm.  This would allow each iceberg's mass, volume and 'towability' to be assessed separately.

## License
This project is available under the Apache 2.0 License.  See the LICENSE for further details.
