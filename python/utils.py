import gtfs_realtime_pb2 as gtfs_rt

def formatdate(date: str):
    return int(date.split('Date(')[1].split('-')[0])//1000

def transtr(s):
    transtr        = gtfs_rt.TranslatedString()
    translate      = gtfs_rt.TranslatedString.Translation()
    translate.text = str(s)
    transtr.translation.add().CopyFrom(translate)
    return(transtr)
