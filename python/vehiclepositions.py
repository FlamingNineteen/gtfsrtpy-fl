import gtfs_realtime_pb2 as gtfs_rt
from utils import *

import json
import requests
import time

def GetVehiclePositions(gtfsrt: gtfs_rt.FeedMessage, uniqueid: int = 0):
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

                vehicle = gtfs_rt.VehiclePosition()

                trip          = gtfs_rt.TripDescriptor()
                trip.trip_id  = str(busdict.get('TripId'))
                trip.route_id = str(busdict.get('RouteId'))
                vehicle.trip.CopyFrom(trip)

                desc       = gtfs_rt.VehicleDescriptor()
                desc.id    = str(busdict.get('VehicleId'))
                desc.label = busdict.get('Name')
                vehicle.vehicle.CopyFrom(desc)

                position           = gtfs_rt.Position()
                position.latitude  = busdict.get('Latitude')
                position.longitude = busdict.get('Longitude')
                position.speed     = busdict.get('Speed')
                vehicle.position.CopyFrom(position)

                vehicle.stop_id          = str(busdict.get('StopId'))
                vehicle.timestamp        = formatdate(busdict.get('LastUpdated'))
                vehicle.occupancy_status = VEHICLE_OCCUPANCIES[busdict.get('OccupancyStatus')]

                if ('OnBoard' in busdict and 'TotalCapacity' in busdict):
                    if (busdict.get('OnBoard') != None and busdict.get('TotalCapacity') != None):
                        vehicle.occupancy_percentage = busdict.get('OnBoard')*100 // busdict.get('TotalCapacity')

                entity.vehicle.CopyFrom(vehicle)

                gtfsrt.entity.add().CopyFrom(entity)

    return gtfsrt

if __name__ == '__main__':
    result = gtfs_rt.FeedMessage()
    result.header.CopyFrom(GetHeader())
    result = GetVehiclePositions(result)

    with open("vehiclepositions.pb", "wb") as f:
        f.write(result.SerializeToString())
    
    with open('vehiclepositions.txt', 'w') as f:
        f.write(str(result))
