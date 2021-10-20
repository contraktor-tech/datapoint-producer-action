import os
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ["INFLUX_TOKEN"]
measurement = os.environ.get("INFLUX_MEASUREMENT", "deploy")
influxdb_url = os.environ["INFLUX_URL"]
app_name = os.environ["APP"]
org = os.environ.get("INFLUX_ORG", "Contraktor")
bucket = 'deployment'

influxdb = InfluxDBClient(url=influxdb_url, token=token)

point = Point(measurement)
point.field(app_name, 1)
point.time(datetime.utcnow(), WritePrecision.NS)

write_api = influxdb.write_api(write_options=SYNCHRONOUS)
write_api.write(bucket, org, point)
