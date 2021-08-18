# Background
The USGS 3DEP project (United States Geological Survey 3D Elevation Program) aims at responding to growing needs for high-quality topographic data and a wide range of 3D data representation of the county’s features. You can read about the full project here.
The data is stored in a repository on an amazon server. The server contains geospatial data on over 1000 geographical regions. The data stored is in a .ept JSON file format. Entwine Point Tile format (ept)is a simple way to store data. It achieves this by a simple tree-based format. To enable processing ept has crucial keys that enable smooth processing. The dataset is however very complicated to understand

Hence this project aims to create a package to interact with the data and process it into a less complex file

# Data

Download USGS 3DEP data from here

# Folders
jsons-folder contains all pipleines in form of .ept.json files

laz-stores processed laz files

tif-stores .tif files

notebooks- contains notebooks used


## notebooks

scripts- folder contains python scripts used int he project

## scripts
``` classification.py ``` allows user to define classification for pipeline processing

``` generate.py ``` base script to generate new tif and laz files

``` reprojection.py ``` this script reprojects the sh files into a standard format using geopandas



# Resources
https://www.usgs.gov/core-science-systems/ngp/3dep/what-is-3dep?qt-science_support_page_related_con=0#qt-science_support_page_related_con

https://entwine.io/entwine-point-tile.html
