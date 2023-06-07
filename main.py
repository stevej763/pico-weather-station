from machine import Pin, I2C
from time import sleep
from lib.bme.bme280 import BME280
from lib.microdot.microdot import Microdot
from lib.connection.status_light import StatusLight
from lib.connection.wifi_connection import WifiConnection
from lib.connection.wifi_settings import ssid, password


import machine
import ubinascii

pico_id = ubinascii.hexlify(machine.unique_id()).decode()
 
i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=400000)
bme = BME280(i2c=i2c)

wifi = WifiConnection(ssid, password, StatusLight("LED"))
app = Microdot()

@app.route('/data')
def get_data():
    response_json = {
          "deviceId": pico_id,
          "temperature": bme.get_temperature(),
          "pressure": bme.get_pressure(),
          "humidity": bme.get_humidity()
        }
    return response_json

@app.route('/data/temperature')
def get_temperature():
    response_json = {
          "deviceId": pico_id,
          "temperature": bme.get_temperature()
        }
    return response_json

@app.route('/data/pressure')
def get_pressure():
    response_json = {
          "deviceId": pico_id,
          "pressure": bme.get_pressure(),
        }
    return response_json

@app.route('/data/humidity')
def get_humidity():
    response_json = {
          "deviceId": pico_id,
          "humidity": bme.get_humidity()
        }
    return response_json

wifi.connect()
app.run('0.0.0.0', 8080, True)
