USG3 Module Tutorials
****************************

The package consists of a number of scripts that carry out different functions


Modules In  The package 
========================

Supported functions include the following:

1. classification
   
2. elevation_data
   
3. elevation
   
4. visualize
   
5. generate
   
6. reprojection


Generate
----------

.. function:: gather_input( )

    This is a script function meant to be run on the command line console 
    It is interactive and enables the user to input various parameters that the function wil use to produce a raster file,shape and geojson file 

    :rtype: bound,full_path,output_file_laz,output_file_tif,output_file_csv


.. function:: get_raster_terrain(bounds,full_path,output_file_laz,output_file_tif,output_file_csv,pipeline)

    This function generates necessary geospatial data files such as raster files and las files 

    :param:bounds: input the bounds of the region
    :param:full_path: input the full path of the region's ept file this is can be found by runining the gather input function 
    :param:output_file_laz: input the location to store the laz file
    :param:output_file_tif: input the location to store the raster image file this
    :param:output_file_csv: input the location to store the geopandas dataframe stored in csv format
    
    :rtype: None 

Elevation_data
----------

.. function:: get_elevation(laz_file,las_file,output_path,crs)

    This function extracts elevation of given geometrical points given the latitude and the longitude of the given point

    :param:laz_file: The given laz file that contains the detailed geographical data  of the location
    :param:las_file: The location to store the converted las file equivalent of the laz file
    :param:output_path: The output path fot the geopandas dataframe generated 
    :param:crs: The projection crs you desire to use 
    :rtype: geoPandasData frame , lasfile dataframe


classification
----------

.. function::get_raster_terrain(bounds,full_path,output_file_laz,output_file_tif,classification,pipeline)

    This function is similar to the get_raster_terrain found in the generated libraries the difference is that it allows the user to specify the classification of the raster file according to the ASRPS Standard LiDAR point Classification
    Below is the classification reference 



.. image:: ./lidarclass.png


Reprojection 
----------

This is a class script and hence must be initialized before using it
The class requires a geopandas dataframe for initialization.

``<instance name>=REPRO(geoapndasfile)`` 

.. function:: <instance name>.reprojet(): 

    :rtype: a set reprojection crs for the given geopandas dataframe

visualize
----------

This class comprises functions to visualize the data 

.. function:: visalize_3D(las_file,output_name, **kwargs):
    
    :param:las_file: the las file from which we get the information
    :output:output_name: the output name for the 3d renderer

    :rtype: a 3D plot stored in html format

    .. figure:: ./images/iowa3d.png
        :align: center
     
        3D visualization of IO_FULLSTATE 



.. function:: standardize_plot(geo_frame,setcrs,tiff_file,shp_output)

    :param:geo_frame: Geodata frame 
    :param:setc: set the reprojection of the geopandas dataframe
    :param:tiff_file: path to the raster image file
    :param:shp_output: path to store the correspodning shape file 








