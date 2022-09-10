
import pandas as pd
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("<your influx db token>")
org = "<your influx db org name>"
url = "<your influx db custom url>"
Bucket = "<your influx bucket name>"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

df = pd.read_csv('AirPassengers.csv')
for i in df.index:
    point = (
    Point("passengers")
    .tag("month", df.iloc[i,0])
    .field("passengers", df.iloc[i,1])
  )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1) # separate points by 1 second


