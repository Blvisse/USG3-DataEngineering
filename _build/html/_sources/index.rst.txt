.. USG3 documentation master file, created by
   sphinx-quickstart on Sat Aug 21 23:27:30 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to USG3's documentation!
*********************************

The USGS 3DEP project (United States Geological Survey 3D Elevation Program) aims at responding to growing needs for high-quality topographic data and a wide range of 3D data representation of the county’s features. 

The data is stored in a repository on an amazon server. The server contains geospatial data on over 1000 geographical regions. The data stored is in a .ept JSON file format. Entwine Point Tile format (ept)is a simple way to store data. It achieves this by a simple tree-based format. To enable processing ept has crucial keys that enable smooth processing. The dataset is however very complicated to understand

Hence this project aims to create a package to interact with the data and process it into a less complex file, example of code interaction can be found in the notebook labeled scriptdemeonstration.ipynb

All package dependencies can be found in the requirements.txt file 

.. versionadded:: 1.0

   1. Fetching of data from USGS 3DEP amazon data source
   
   2. Visualization of boundaries 
   
   3. Calculation of Topographic Wetness Index 
   
   4. Transformation of boundary points 
   

.. warning:: 
   *** This is an API in very early stages of development that may include some bugs or not support some systems *** 

How to Interact with the API
================================
.. note:: 
   1. Run:: 
   
     ``pip install USG3``

     to install the API and all dependencies 
   2. To import the API and all dependencies::
      
       import USG3 

      to your IDE/script 
   3. If you require specific functions from the package you can access them via::  

          from USG3 import <function name>  

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   

   tutorial 
   requirements
   
   

Setup Snippets 
================================
.. automodule:: setup 
   :members: 
Get Data API 
================================ 

.. automodule:: USG3.generate 
  :members: 



Visualization Script 
================================ 

.. automodule:: USG3.visualize 
   :members:  


Indices and tables
================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
