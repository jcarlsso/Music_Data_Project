import pandas as pd
import json
import datetime as dt

# json_1 = pd.read_json(r'MyData/endsong_0.json')
# json_2 = pd.read_json(r'MyData/endsong_1.json')
# json_3 = pd.read_json(r'MyData/endsong_2.json')



# x = pd.Series(json_3['ts'])
# for line in x:
#     new = line.split("T")
#     if new[0] == "2019-12-05":
#         print(['master_metadata_album_album_name'])


with open("MyData/endsong_0.json", "r", encoding="utf8") as file1:
    jdata1 = json.load(file1)

# print(json.dumps(jdata1, indent=2))

def before2018():
    for data in jdata1:
        jdata1_cleaned = data['ts'], data['master_metadata_album_artist_name'], data['master_metadata_album_album_name'], data['master_metadata_track_name']
        # date_time = dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ')
        x = []
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            x.append(data)
            print(x)

before2018()

