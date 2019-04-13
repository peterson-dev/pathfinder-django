# Pathfinder

## Description

This small web app allows you to upload any text file (i.e. `.txt`, `.asc`) containing topographic (land elevation) data, which generates an elevation map as a `.png` file, and charts every optimal path from left to right. These lines are drawn in purple. The green line highlights the path with the 'least' amount of elevation change. The idea for this project originated from a lab I did in school called [Mountain Paths](MountainPaths.pdf), which was adapted from [this project](http://nifty.stanford.edu/2016/franke-mountain-paths/). The concepts utilize a "greedy" algorithm that follows the problem solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum, i.e. the green line.  

## Built With
- [Django](https://www.djangoproject.com/) - The web framework
- Python and Javascript
- [Pillow](https://pillow.readthedocs.io/en/3.0.x/index.html) - A Python library to create images

## Test it out
- Navigate to the [website](https://greedy-pathfinder.herokuapp.com/)
- Download the test data in the project directory `/sample-data/rocky-mountain-south.asc`
- "Choose" file in the UI and select the sample file
- Click "Generate map" 
- Behold the algorithmic glory

To try out other data sets, you can go to [the NOAA Grid Extract tool](http://maps.ngdc.noaa.gov/viewers/wcs-client/) and follow these steps to select any region on the globe.

- Select an area using the box selector button.
- Download the data in "ArcGIS ASCII Grid" format.
- Remove the metadata at the top of the file, leaving just the numbers.
- Upload the file in the same way as above.  

## Acknowledgements
* [Fan Huang](https://github.com/fanh33)
* [Clinton Dreisbach](https://github.com/cndreisbach)
