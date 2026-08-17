import gtfs_realtime_pb2 as gtfs_rt

import time

def formatdate(date: str):
    return int(date.split('Date(')[1].split('-')[0])//1000

def transtr(s):
    transtr        = gtfs_rt.TranslatedString()
    translate      = gtfs_rt.TranslatedString.Translation()
    translate.text = str(s)
    transtr.translation.add().CopyFrom(translate)
    return(transtr)

def GetHeader():
    header = gtfs_rt.FeedHeader()
    header.gtfs_realtime_version = '2.0'
    header.incrementality = gtfs_rt.FeedHeader.Incrementality.FULL_DATASET
    header.timestamp = int(time.time())
    return header

VEHICLE_OCCUPANCIES = (
    gtfs_rt.VehiclePosition.OccupancyStatus.EMPTY,
    gtfs_rt.VehiclePosition.OccupancyStatus.MANY_SEATS_AVAILABLE,
    gtfs_rt.VehiclePosition.OccupancyStatus.FEW_SEATS_AVAILABLE,
    gtfs_rt.VehiclePosition.OccupancyStatus.STANDING_ROOM_ONLY,
    gtfs_rt.VehiclePosition.OccupancyStatus.CRUSHED_STANDING_ROOM_ONLY,
    gtfs_rt.VehiclePosition.OccupancyStatus.FULL,
    gtfs_rt.VehiclePosition.OccupancyStatus.NOT_ACCEPTING_PASSENGERS,
    gtfs_rt.VehiclePosition.OccupancyStatus.NO_DATA_AVAILABLE,
    gtfs_rt.VehiclePosition.OccupancyStatus.NOT_BOARDABLE,
)

ALERT_CAUSES = (
    gtfs_rt.Alert.Cause.UNKNOWN_CAUSE,
    gtfs_rt.Alert.Cause.OTHER_CAUSE,
    gtfs_rt.Alert.Cause.TECHNICAL_PROBLEM,
    gtfs_rt.Alert.Cause.STRIKE,
    gtfs_rt.Alert.Cause.DEMONSTRATION,
    gtfs_rt.Alert.Cause.ACCIDENT,
    gtfs_rt.Alert.Cause.HOLIDAY,
    gtfs_rt.Alert.Cause.WEATHER,
    gtfs_rt.Alert.Cause.MAINTENANCE,
    gtfs_rt.Alert.Cause.CONSTRUCTION,
    gtfs_rt.Alert.Cause.POLICE_ACTIVITY,
    gtfs_rt.Alert.Cause.MEDICAL_EMERGENCY,
    gtfs_rt.Alert.Cause.SPECIAL_EVENT,
)

ALERT_EFFECTS = (
    gtfs_rt.Alert.Effect.NO_SERVICE,
    gtfs_rt.Alert.Effect.REDUCED_SERVICE,
    gtfs_rt.Alert.Effect.SIGNIFICANT_DELAYS,
    gtfs_rt.Alert.Effect.DETOUR,
    gtfs_rt.Alert.Effect.ADDITIONAL_SERVICE,
    gtfs_rt.Alert.Effect.MODIFIED_SERVICE,
    gtfs_rt.Alert.Effect.OTHER_EFFECT,
    gtfs_rt.Alert.Effect.UNKNOWN_EFFECT,
    gtfs_rt.Alert.Effect.STOP_MOVED,
    gtfs_rt.Alert.Effect.NO_EFFECT,
    gtfs_rt.Alert.Effect.ACCESSIBILITY_ISSUE,
)
