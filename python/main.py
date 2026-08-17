from alerts           import GetAlerts
from tripupdates      import GetTripUpdates
from vehiclepositions import GetVehiclePositions
from utils            import GetHeader

import gtfs_realtime_pb2 as gtfs_rt

import time

if __name__ == '__main__':
    i=0

    while True:
        i+=1
        print(f'Loop {i}')

        gtfsrt = gtfs_rt.FeedMessage()
        gtfsrt.header.CopyFrom(GetHeader())

        print('Getting vehicle positions')
        GetVehiclePositions(gtfsrt)

        print('Getting alerts')
        GetAlerts(gtfsrt)

        print('Getting trip updates')
        GetTripUpdates(gtfsrt)

        with open('realtime.pb', 'wb') as file:
            file.write(gtfsrt.SerializeToString())

        with open('realtime.txt', 'w') as file:
                file.write(str(gtfsrt))

        print('Done! Sleeping for 25 seconds...')
        time.sleep(25)

        print()
