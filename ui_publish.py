import json
import os

import datetime

from Adafruit_BME280 import *
import paho.mqtt.client as paho
import time

from subprocess import call

broker = "127.0.0.1"
port = 1883
filename = datetime.datetime.now().isoformat() + ".log"
data = {}




def on_publish(client, userdata, result):  # create function for callback
    # print("data published \n")
    pass


def publish_sensor_data(client, sensor_data):
    client.publish("sensors/temperature", "%0.3f" % (sensor_data["temperature"]), retain=True)
    client.publish("sensors/pressure", "%0.3f" % sensor_data["pressure"])
    client.publish("sensors/humidity", "%0.3f" % sensor_data["humidity"])
    client.publish("sensors/dewpoint", "%0.3f" % sensor_data["dew_point"])


def init_mqtt_client():
    client = paho.Client("control1")  # create client object
    client.on_publish = on_publish  # assign function to callback
    client.connect(broker, port)  # establish connection
    return client



def append_data(d):
    if os.path.exists(filename):
        with open(filename, "rb") as data_file:
            data_list = pickle.load(data_file)
            data_list.append(d)
        with open(filename, "wb") as data_file:
            pickle.dump(data_list, data_file)
    else:
        with open(filename, "wb") as data_file:
            pickle.dump([], data_file)



def get_sensor_data(sensor):
    data["datetime"] = datetime.datetime.now()
    data["temperature"] = round(sensor.read_temperature(), 2)
    data["pressure"] = round(sensor.read_pressure() / 100, 3)
    data["humidity"] = round(sensor.read_humidity(), 2)
    data["dew_point"] = round(sensor.read_dewpoint(), 2)
    return






def main_loop():
    client = init_mqtt_client()
    bme = BME280(p_mode=BME280_OSAMPLE_8, t_mode=BME280_OSAMPLE_2, h_mode=BME280_OSAMPLE_1, filter=BME280_FILTER_16)

    start_time = datetime.datetime.now()
    data_published_time = datetime.datetime.now()

    i = 0


    while True:
        i += 1

        get_sensor_data(sensor=bme)

        # Publish sensor data to MQTT server
        publish_sensor_data(client=client, sensor_data=data)
        print data
        # Push data file to server @krasi
        time.sleep(1)

main_loop()
