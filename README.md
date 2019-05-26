# Pathfinder

## Description

Pathfinder allows you to upload a text file (i.e. `.txt`, `.asc`) containing topographic data, generate an elevation map as a `.png` file, and chart optimal paths across. Each optimal path will be drawn in purple. A green line is drawn highlighting the path with the 'least' amount of elevation change. This project is an extension to a lab assignement called [Mountain Paths](MountainPaths.pdf), which was adapted from [this project](http://nifty.stanford.edu/2016/franke-mountain-paths/). The concepts utilize a "greedy" algorithm that follows the problem solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum, i.e. the green line.  

## Built With
- [Django](https://www.djangoproject.com/) - Web framework
- Python and Javascript
- [Pillow](https://pillow.readthedocs.io/en/3.0.x/index.html) - Python imaging library

## Test it out
- Navigate to the [website](https://greedy-pathfinder.herokuapp.com/)
- Download the test data by clicking the link
- Click the "Choose File" button and select the test data file
- Click "Generate map" 
- Behold the algorithmic glory

To try out other data sets, you can go to [the NOAA Grid Extract tool](http://maps.ngdc.noaa.gov/viewers/wcs-client/) and follow these steps to select any region on the globe.

- Select an area using the box selector button.
- Download the data in "ArcGIS ASCII Grid" format.
- Remove the metadata at the top of the file, leaving just the numbers.
- Upload the file in the same way as above.  

## Acknowledgements
* [Fan](https://github.com/fanh33)
* [Clint](https://github.com/cndreisbach)
