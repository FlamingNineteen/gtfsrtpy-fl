import gtfs_realtime_pb2 as gtfs_rt
from utils import *

import json
import requests
import time

def GetAlerts():
    gtfsrt = gtfs_rt.FeedMessage()
    
    header = gtfs_rt.FeedHeader()
    header.gtfs_realtime_version = '2.0'
    header.incrementality = gtfs_rt.FeedHeader.Incrementality.FULL_DATASET
    header.timestamp = int(time.time())
    gtfsrt.header.CopyFrom(header)

    uniqueid = 0

    # Availtec API
    for agency_id, url in (
        ('127', 'realtimevotran.availtec.com'),
        ('40120', 'realtimesuntran.availtec.com'),
        ('1752', 'www.ccbusinfo.com'),
    ):
        print(url)
        
        get = requests.get(f'https://{url}/InfoPoint/rest/PublicMessages/GetCurrentMessages').text
        son = json.loads(get)

        for alertdict in son:
            entity    = gtfs_rt.FeedEntity()
            entity.id = str(uniqueid)
            uniqueid += 1

            alert = gtfs_rt.Alert()

            timerange       = gtfs_rt.TimeRange()
            timerange.start = formatdate(alertdict.get('FromTime'))
            timerange.end   = formatdate(alertdict.get('ToTime'))
            alert.active_period.add().CopyFrom(timerange)

            informed = gtfs_rt.EntitySelector()
            informed.agency_id = agency_id
            alert.informed_entity.add().CopyFrom(informed)

            alert.cause  = ALERT_CAUSES[alertdict.get('Cause')-1]
            alert.cause_detail.CopyFrom(transtr(alertdict.get('CauseReportLabel')))
            
            alert.effect = ALERT_EFFECTS[alertdict.get('Effect')-1]
            alert.effect_detail.CopyFrom(transtr(alertdict.get('CauseReportLabel')))

            alert.header_text.CopyFrom(transtr(alertdict.get('Header')))
            alert.description_text.CopyFrom(transtr(alertdict.get('Message')))

            entity.alert.CopyFrom(alert)
            
            gtfsrt.entity.add().CopyFrom(entity)

    return gtfsrt

if __name__ == '__main__':
    result = GetAlerts()

    with open("alerts.pb", "wb") as f:
        f.write(result.SerializeToString())
    
    with open('alerts.txt', 'w') as f:
        f.write(str(result))
