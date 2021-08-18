import pdal
import json

#### we intialize the dataset location present in aws
dataset_path='https://s3-us-west-2.amazonaws.com/usgs-lidar-public'
###we select iowa region to gather info from it
selected_region='IA_FullState'

bounds="([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"

full_path=dataset_path+selected_region+"ept.json"

output_file_laz="iowa.laz"
output_file_tif="iowa.tif"
pipeline="../jsons/user.json"

def get_raster_terrain(bounds,region,full_path,output_file_laz,output_file_tif,pipeline):

    with open(pipeline) as json_file:
        file_json=json.load(json_file)

    file_json['pipeline'][0]['bounds']=bounds
    file_json['pipeline'][0]['filename']=region
    file_json['pipeline'][5]['filename']=output_file_laz
    file_json['pipeline'][6]['filename']=output_file_tif

    pipeline=pdal.Pipeline(json.dumps(file_json))

    try:
        pipe_execute=pipeline.execute()
        metadata=pipeline.metadata
    except :
        pass


if (__name__== '__main__'):
    get_raster_terrain()




