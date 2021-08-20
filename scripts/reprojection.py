import os 
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import earthpy as et 


class REPRO:
    def __init__(self,file):
        self.file=file
        
    def reproject(self):
        print()
        sh_file = gpd.read_file(self.file)  
        sh=sh_file.set_crs("EPSG:3857")
        print(sh.crs)
        
        return sh.crs

        
if (__name__== '__main__'):
    
    instance=REPRO('../shp/combi.shp')
    instance.reproject()
    
    

