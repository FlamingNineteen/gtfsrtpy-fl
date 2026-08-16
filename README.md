# Python GTFS Realtime for Central Florida
This repository makes [GTFS Realtime](https://gtfs.org/documentation/realtime) Protocol Buffer binaries to be used by services such as [OneBusAway](https://github.com/OneBusAway). It requests information from various REST APIs and forms three binaries based on merged information from each included agency.

## Agencies

| Agency Name | Region| Status | Website | Realtime API Link
| --- | --- | --- | --- | ---
| LYNX | Greater Orlando | Not Started | https://www.golynx.com | Unknown
| Sunrail | Central Florida | Not Started | https://sunrail.com | https://sunrail.com/wp-json/sunrail/v1
| Votran | Volusia Country | Partially Complete | https://www.votran.org | https://realtimevotran.availtec.com/InfoPoint/rest
| Citrus Connect | Polk County | Partially Complete | http://www.ridecitrus.com | https://www.ccbusinfo.com/InfoPoint/rest
| Suntran | City of Ocala | Partially Complete | https://www.ocalafl.gov/government/city-departments-i-z/suntran | https://realtimesuntran.availtec.com/InfoPoint/rest
| LakeXPress | Lake County | Not Started | https://www.ridelakexpress.com | Unknown

## Usage
1. Install the [Protocol Buffer Compiler](https://protobuf.dev/installation/)
2. Clone this repository
```bash
git clone https://github.com/FlamingNineteen/gtfsrtpy-fl.git
```
3. Generate `gtfs_realtime_pb2.py` using `protoc`:
```bash
cd gtfsrtpy-fl
protoc --proto_path=protobuf --python_out=python protobuf/gtfs-realtime.proto
```
4. Install the required Python libraries
```bash
pip install protobuf requests
```
5. Run `main.py`
```bash
python ./python/main.py
```
