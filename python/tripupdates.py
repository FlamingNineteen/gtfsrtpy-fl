import gtfs_realtime_pb2 as gtfs_rt

import json
import requests
import time

gtfsrt = gtfs_rt.FeedMessage()

with open('tripupdates.pb', 'rb') as file:
    gtfsrt.ParseFromString(file.read())

with open('tripupdates copy.txt', 'w') as file:
    file.write(str(gtfsrt))
