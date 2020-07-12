import pandas as pd
import json
import datetime as dt

# Opening each json file and loading it to a global variable

with open("MyData/endsong_0.json", "r", encoding="utf8") as file0:
    jdata0 = json.load(file0)

with open("MyData/endsong_1.json", "r", encoding="utf8") as file1:
    jdata1 = json.load(file1)

with open("MyData/endsong_2.json", "r", encoding="utf8") as file2:
    jdata2 = json.load(file2)

# ['ts'],['master_metadata_album_artist_name'],['master_metadata_album_album_name'],['master_metadata_track_name']

# before2018() is a function to parse through the jdata lists and only pull out listening data prior to 12-27-2018.
# All of the listening data is than appended to a new global list called combined_json_files
combined_json_files = []
def before2018():
    for data in jdata0:
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            combined_json_files.append(data)
    for data in jdata1:
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            combined_json_files.append(data)
    for data in jdata2:
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            combined_json_files.append(data) 

before2018()



# for data in combined_json_files:
#     cleaned_data_list = [data['ts'], data['master_metadata_album_artist_name'], data['master_metadata_album_album_name'], data['master_metadata_track_name']]
#     print(cleaned_data_list)