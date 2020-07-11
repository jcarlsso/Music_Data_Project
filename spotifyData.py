import json

with open("MyData/endsong_0.json", "r", encoding="utf8") as file1:
    jdata1 = json.load(file1)

#print(json.dumps(jdata_1, indent=2))
jdata1_cleaned_list = []

for data in jdata1:
    #if data['ts'] == '2016-*'
    jdata1_cleaned = data['ts'], data['master_metadata_album_artist_name'], data['master_metadata_album_album_name'], data['master_metadata_track_name']
    jdata1_cleaned_list.append(jdata1_cleaned)

print(jdata1_cleaned_list)

    # for key, value in data.items():

        # if key == "master_metadata_album_album_name" and value == "DAMN.":
        #     print(key,":", value)




# for line in jdata_1:
#     if ts == "2019-01-25T18:44:47Z":
#         print(data)
