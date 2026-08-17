# Python GTFS Realtime for Central Florida
This repository makes [GTFS Realtime](https://gtfs.org/documentation/realtime) Protocol Buffer binaries to be used by services such as [OneBusAway](https://github.com/OneBusAway). It requests information from various REST APIs and forms binaries based on merged information from each included agency.

## Agencies

| Agency Name | Region| Status | Realtime API Link
| --- | --- | --- | ---
| [LYNX](https://www.golynx.com) | Greater Orlando | Not Started | Unknown
| [Sunrail](https://sunrail.com) | Central Florida | Not Started | https://sunrail.com/wp-json/sunrail/v1
| [Votran](https://www.votran.org) | Volusia Country | Complete | https://realtimevotran.availtec.com/InfoPoint/rest
| [Citrus Connect](http://www.ridecitrus.com) | Polk County | Complete | https://www.ccbusinfo.com/InfoPoint/rest
| [Suntran](https://www.ocalafl.gov/government/city-departments-i-z/suntran) | City of Ocala | Complete | https://realtimesuntran.availtec.com/InfoPoint/rest
| [LakeXPress](https://www.ridelakexpress.com) | Lake County | Not Started | Unknown

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
The Python script performs get requests to various REST APIs for different agencies and compiles the data into a single Protocol Buffer binary. Then it sleeps for 25 seconds and repeats.
