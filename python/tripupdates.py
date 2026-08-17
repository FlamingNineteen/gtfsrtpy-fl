import gtfs_realtime_pb2 as gtfs_rt
from utils import *

import json
import requests
import time

def GetTripUpdates():
    gtfsrt = gtfs_rt.FeedMessage()
        
    header = gtfs_rt.FeedHeader()
    header.gtfs_realtime_version = '2.0'
    header.incrementality = gtfs_rt.FeedHeader.Incrementality.FULL_DATASET
    header.timestamp = int(time.time())
    gtfsrt.header.CopyFrom(header)

    uniqueid = 0

    # Availtec API
    for url in (
        'realtimevotran.availtec.com',
        'realtimesuntran.availtec.com',
        'www.ccbusinfo.com',
    ):
        print(url)
        
        get = requests.get(f'https://{url}/InfoPoint/rest/Routes/GetVisibleRoutes').text
        son = json.loads(get)

        for route in son:
            for busdict in route.get('Vehicles'):
                entity    = gtfs_rt.FeedEntity()
                entity.id = str(uniqueid)
                uniqueid += 1

                update = gtfs_rt.TripUpdate()

                trip         = gtfs_rt.TripDescriptor()
                trip.trip_id = str(busdict.get('TripId'))
                update.trip.CopyFrom(trip)

                desc       = gtfs_rt.VehicleDescriptor()
                desc.id    = str(busdict.get('VehicleId'))
                desc.label = busdict.get('Name')
                update.vehicle.CopyFrom(desc)

                update.timestamp = formatdate(busdict.get('LastUpdated'))
                update.delay     = busdict.get('Deviation')

                entity.trip_update.CopyFrom(update)

                gtfsrt.entity.add().CopyFrom(entity)

    return gtfsrt

if __name__ == '__main__':
    result = GetTripUpdates()

    with open('tripupdates.pb', 'wb') as file:
        file.write(result.SerializeToString())

    with open('tripupdates.txt', 'w') as file:
        file.write(str(result))
