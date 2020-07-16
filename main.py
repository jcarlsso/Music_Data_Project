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
            if data['master_metadata_album_artist_name'] is not None:
                combined_json_files.append(data)
    for data in jdata1:
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            if data['master_metadata_album_artist_name'] is not None:
                combined_json_files.append(data)
    for data in jdata2:
        if dt.datetime.strptime(data['ts'], '%Y-%m-%dT%H:%M:%SZ') < dt.datetime(2018,12,27,0,0,0,):
            if data['master_metadata_album_artist_name'] is not None:
                combined_json_files.append(data) 

before2018()

print(len(combined_json_files))

test_list = []

for data in combined_json_files:
    if data['master_metadata_album_artist_name'] != 'Mac Miller':
        if data['master_metadata_album_artist_name'] != 'Drake':
            if data['master_metadata_album_artist_name'] != 'Kendrick Lamar':
                if data['master_metadata_album_artist_name'] != 'Logic':
                    test_list.append(data)

print(len(test_list))






# TDF = 0
# Track_1 = 0
# Track_2 = 0
# Track_3 = 0
# Track_4 = 0
# Track_5 = 0
# Track_6 = 0
# Track_7 = 0
# Track_8 = 0
# Track_9 = 0
# Track_10 = 0
# Track_11 = 0
# Track_12 = 0
# Track_13 = 0
# Track_14 = 0
# Track_15 = 0
# Track_16 = 0
# Track_17 = 0
# Track_18= 0
# Track_19 = 0

# for data in combined_json_files:
#     if data['master_metadata_album_album_name'] == 'The Divine Feminine':
#         TDF += 1
#         # print(data["master_metadata_track_name"])
#         if data['master_metadata_track_name'] == 'Congratulations (feat. Bilal)':
#             Track_1 += 1
#         if data['master_metadata_track_name'] == 'Dang! (feat. Anderson .Paak)':
#             Track_2 += 1
#         if data['master_metadata_track_name'] == "Stay":
#             Track_3 += 1
#         if data['master_metadata_track_name'] == 'Skin':
#             Track_4 += 1
#         if data['master_metadata_track_name'] == 'Cinderella (feat. Ty Dolla $ign)':
#             Track_5 += 1
#         if data['master_metadata_track_name'] == 'Planet God Damn (feat. Njomza)':
#             Track_6 += 1
#         if data['master_metadata_track_name'] == "Soulmate":
#             Track_7 += 1
#         if data['master_metadata_track_name'] == 'We (feat. CeeLo Green)':
#             Track_8 += 1
#         if data['master_metadata_track_name'] == 'My Favorite Part':
#             Track_9 += 1
#         if data['master_metadata_track_name'] == 'God Is Fair, Sexy Nasty (feat. Kendrick Lamar)':
#             Track_10 += 1
#         if data['master_metadata_track_name'] == 'Watching Movies':
#             Track_11 += 1
#         if data['master_metadata_track_name'] == 'Suplexes Inside of Complexes and Duplexes':
#             Track_12 += 1
#         if data['master_metadata_track_name'] == 'Remember':
#             Track_13 += 1
#         if data['master_metadata_track_name'] == 'Someone Like You':
#             Track_14 += 1
#         if data['master_metadata_track_name'] == 'Aquarium':
#             Track_15 += 1
#         if data['master_metadata_track_name'] == 'Youforia':
#             Track_16 += 1
#         if data['master_metadata_track_name'] == 'Goosebumpz (Bonus Track)':
#             Track_17 += 1
#         if data['master_metadata_track_name'] == 'O.K. (feat. Tyler, The Creator) [Bonus Track]':
#             Track_18 += 1
#         if data['master_metadata_track_name'] == 'Claymation (feat. Vinny Radio) [Bonus Track]':
#             Track_19 += 1


# print("Total GO:OD AM Plays: ", TDF)
# print("Track 1: ", Track_1)
# print("Track 2: ", Track_2)
# print("Track 3: ", Track_3)
# print("Track 4: ", Track_4)
# print("Track 5: ", Track_5)
# print("Track 6: ", Track_6)
# print("Track 7: ", Track_7)
# print("Track 8: ", Track_8)
# print("Track 9: ", Track_9)
# print("Track 10: ", Track_10)
# print("Track 11: ", Track_11)
# print("Track 12: ", Track_12)
# print("Track 13: ", Track_13)
# print("Track 14: ", Track_14)
# print("Track 15: ", Track_15)
# print("Track 16: ", Track_16)
# print("Track 17: ", Track_17)
# print("Track 18: ", Track_18)
# print("Track 19: ", Track_19)




# GOOD_AM = 0
# Track_1 = 0
# Track_2 = 0
# Track_3 = 0
# Track_4 = 0
# Track_5 = 0
# Track_6 = 0
# Track_7 = 0
# Track_8 = 0
# Track_9 = 0
# Track_10 = 0
# Track_11 = 0
# Track_12 = 0
# Track_13 = 0
# Track_14 = 0
# Track_15 = 0
# Track_16 = 0
# Track_17 = 0

# for data in combined_json_files:
#     if data['master_metadata_album_album_name'] == 'GO:OD AM':
#         GOOD_AM += 1
#         if data['master_metadata_track_name'] == 'Doors':
#             Track_1 += 1
#         if data['master_metadata_track_name'] == 'Brand Name':
#             Track_2 += 1
#         if data['master_metadata_track_name'] == 'Rush Hour':
#             Track_3 += 1
#         if data['master_metadata_track_name'] == 'Two Matches (feat. Ab-Soul)':
#             Track_4 += 1
#         if data['master_metadata_track_name'] == '100 Grandkids':
#             Track_5 += 1
#         if data['master_metadata_track_name'] == 'Time Flies (feat. Lil B)':
#             Track_6 += 1
#         if data['master_metadata_track_name'] == 'Weekend (feat. Miguel)':
#             Track_7 += 1
#         if data['master_metadata_track_name'] == 'Clubhouse':
#             Track_8 += 1
#         if data['master_metadata_track_name'] == 'In the Bag':
#             Track_9 += 1
#         if data['master_metadata_track_name'] == 'Break the Law':
#             Track_10 += 1
#         if data['master_metadata_track_name'] == 'Perfect Circle / God Speed':
#             Track_11 += 1
#         if data['master_metadata_track_name'] == 'When in Rome':
#             Track_12 += 1
#         if data['master_metadata_track_name'] == 'ROS':
#             Track_13 += 1
#         if data['master_metadata_track_name'] == 'Cut the Check (feat. Chief Keef)':
#             Track_14 += 1
#         if data['master_metadata_track_name'] == 'Ascension':
#             Track_15 += 1
#         if data['master_metadata_track_name'] == 'Jump':
#             Track_16 += 1
#         if data['master_metadata_track_name'] == 'The Festival (feat. Little Dragon)':
#             Track_17 += 1
#     # cleaned_data_list = [data['ts'], data['master_metadata_album_artist_name'], data['master_metadata_album_album_name'], data['master_metadata_track_name']]

# print("Total GO:OD AM Plays: ", GOOD_AM)
# print("Track 1: ", Track_1)
# print("Track 2: ", Track_2)
# print("Track 3: ", Track_3)
# print("Track 4: ", Track_4)
# print("Track 5: ", Track_5)
# print("Track 6: ", Track_6)
# print("Track 7: ", Track_7)
# print("Track 8: ", Track_8)
# print("Track 9: ", Track_9)
# print("Track 10: ", Track_10)
# print("Track 11: ", Track_11)
# print("Track 12: ", Track_12)
# print("Track 13: ", Track_13)
# print("Track 14: ", Track_14)
# print("Track 15: ", Track_15)
# print("Track 16: ", Track_16)
# print("Track 17: ", Track_17)




# WMWTSO = 0
# Track_1 = 0
# Track_2 = 0
# Track_3 = 0
# Track_4 = 0
# Track_5 = 0
# Track_6 = 0
# Track_7 = 0
# Track_8 = 0
# Track_9 = 0
# Track_10 = 0
# Track_11 = 0
# Track_12 = 0
# Track_13 = 0
# Track_14 = 0
# Track_15 = 0
# Track_16 = 0
# Track_17 = 0
# Track_18= 0
# Track_19 = 0

# for data in combined_json_files:
#     if data['master_metadata_album_album_name'] == 'Watching Movies with the Sound Off (Deluxe Edition)':
#         WMWTSO += 1
#         # print(data["master_metadata_track_name"])
#         if data['master_metadata_track_name'] == 'The Star Room':
#             Track_1 += 1
#         if data['master_metadata_track_name'] == 'Avian':
#             Track_2 += 1
#         if data['master_metadata_track_name'] == "I'm Not Real (feat. Earl Sweatshirt)":
#             Track_3 += 1
#         if data['master_metadata_track_name'] == 'S.D.S.':
#             Track_4 += 1
#         if data['master_metadata_track_name'] == 'Bird Call':
#             Track_5 += 1
#         if data['master_metadata_track_name'] == 'Matches (feat. Ab-Soul)':
#             Track_6 += 1
#         if data['master_metadata_track_name'] == "I Am Who Am (Killin' Time) [feat. Niki Randa]":
#             Track_7 += 1
#         if data['master_metadata_track_name'] == 'Objects in the Mirror':
#             Track_8 += 1
#         if data['master_metadata_track_name'] == 'Red Dot Music (feat. Action Bronson)':
#             Track_9 += 1
#         if data['master_metadata_track_name'] == 'Gees (feat. Schoolboy Q)':
#             Track_10 += 1
#         if data['master_metadata_track_name'] == 'Watching Movies':
#             Track_11 += 1
#         if data['master_metadata_track_name'] == 'Suplexes Inside of Complexes and Duplexes':
#             Track_12 += 1
#         if data['master_metadata_track_name'] == 'Remember':
#             Track_13 += 1
#         if data['master_metadata_track_name'] == 'Someone Like You':
#             Track_14 += 1
#         if data['master_metadata_track_name'] == 'Aquarium':
#             Track_15 += 1
#         if data['master_metadata_track_name'] == 'Youforia':
#             Track_16 += 1
#         if data['master_metadata_track_name'] == 'Goosebumpz (Bonus Track)':
#             Track_17 += 1
#         if data['master_metadata_track_name'] == 'O.K. (feat. Tyler, The Creator) [Bonus Track]':
#             Track_18 += 1
#         if data['master_metadata_track_name'] == 'Claymation (feat. Vinny Radio) [Bonus Track]':
#             Track_19 += 1
#     # cleaned_data_list = [data['ts'], data['master_metadata_album_artist_name'], data['master_metadata_album_album_name'], data['master_metadata_track_name']]


# print("Total Watching Movies with the Sound Off Plays: ", WMWTSO)
# print("Track 1: ", Track_1)
# print("Track 2: ", Track_2)
# print("Track 3: ", Track_3)
# print("Track 4: ", Track_4)
# print("Track 5: ", Track_5)
# print("Track 6: ", Track_6)
# print("Track 7: ", Track_7)
# print("Track 8: ", Track_8)
# print("Track 9: ", Track_9)
# print("Track 10: ", Track_10)
# print("Track 11: ", Track_11)
# print("Track 12: ", Track_12)
# print("Track 13: ", Track_13)
# print("Track 14: ", Track_14)
# print("Track 15: ", Track_15)
# print("Track 16: ", Track_16)
# print("Track 17: ", Track_17)
# print("Track 18: ", Track_18)
# print("Track 19: ", Track_19)

# TDF = 0
# Track_1 = 0
# Track_2 = 0
# Track_3 = 0
# Track_4 = 0
# Track_5 = 0
# Track_6 = 0
# Track_7 = 0
# Track_8 = 0
# Track_9 = 0
# Track_10 = 0

# for data in combined_json_files:
#     if data['master_metadata_album_album_name'] == 'The Divine Feminine':
#         TDF += 1
#         # print(data["master_metadata_track_name"])
#         if data['master_metadata_track_name'] == 'Congratulations (feat. Bilal)':
#             Track_1 += 1
#         if data['master_metadata_track_name'] == 'Dang! (feat. Anderson .Paak)':
#             Track_2 += 1
#         if data['master_metadata_track_name'] == "Stay":
#             Track_3 += 1
#         if data['master_metadata_track_name'] == 'Skin':
#             Track_4 += 1
#         if data['master_metadata_track_name'] == 'Cinderella (feat. Ty Dolla $ign)':
#             Track_5 += 1
#         if data['master_metadata_track_name'] == 'Planet God Damn (feat. Njomza)':
#             Track_6 += 1
#         if data['master_metadata_track_name'] == "Soulmate":
#             Track_7 += 1
#         if data['master_metadata_track_name'] == 'We (feat. CeeLo Green)':
#             Track_8 += 1
#         if data['master_metadata_track_name'] == 'My Favorite Part':
#             Track_9 += 1
#         if data['master_metadata_track_name'] == 'God Is Fair, Sexy Nasty (feat. Kendrick Lamar)':
#             Track_10 += 1


# print("Total The Divine Feminine Plays: ", TDF)
# print("Track 1: ", Track_1)
# print("Track 2: ", Track_2)
# print("Track 3: ", Track_3)
# print("Track 4: ", Track_4)
# print("Track 5: ", Track_5)
# print("Track 6: ", Track_6)
# print("Track 7: ", Track_7)
# print("Track 8: ", Track_8)
# print("Track 9: ", Track_9)
# print("Track 10: ", Track_10)


