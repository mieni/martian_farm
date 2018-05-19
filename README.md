# Marsian garlic farm
Boriana Chtircova, Chavdar Ducov, Lubomir Petrov, Mihail Enimanev

A hackathon project for martian garlic farm with automatic watering ligths and the CO₂ exhaustion

![](https://github.com/mieni/martian_farm/blob/master/img/laika.jpg)
------------------------------------------------------------------------------------
## Used hardware
* [Raspberry pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Special red & blue LEDs used for plant growth](https://store.comet.bg/Catalogue/Product/49763/ "store link - blue")
* [Water pumps](https://www.olimex.com/Products/Components/Misc/MICRO-WATER-PUMP/ "store link")
* [Air Valve](https://www.olimex.com/Products/Components/Misc/AIR-E-VALVE-12V/ "store link")
* [Power supply -12VDC, 25W, 220VAC, 2A](https://vikiwat.com/zahranvasch-blok-ms35-12-12v-3a-36w.html "store link")
* [Soil humidity sensor](https://erelement.com/sensors/moisture-sensor?cPath=9_34&zenid=t0bn9dq5otka66lvfdsr4akte2 "bg store link")
* [temperature/pressure/humidity sensor](https://erelement.com/sensors/bme280?zenid=t0bn9dq5otka66lvfdsr4akte2 "bg store link")

------------------------------------------------------------------------------------
## Connecting the raspberry pi

This is a diagram of the conected pins of the raspberry pi

![](https://github.com/mieni/martian_farm/blob/master/img/pins.png)

------------------------------------------------------------------------------------
## Control of sensors and pumps 

The sensors that the farm uses are the [soil moisture sensor](https://www.itead.cc/wiki/Moisture_Sensor) and the [BME280](https://learn.adafruit.com/search?q=BME280&) sensor for temperature/pressure/humidity

The main features of the martian farm are

* Controlling the lights, simulating day and night.
* Controlling the CO₂ levels by using an air valve and [this](https://www.wikihow.com/Make-CO₂ "How to Make CO₂ at home") reaction.

 This is done by puting the ```day.py``` and ```night.py``` scripts in the crontab. That way we can simulate that 8 hour nights and 16 hour the days in wich the CO₂ is released.
 
* Controlling the moisture of the soil, giving it [55ml for 4 days](https://www.thompson-morgan.com/how-to-grow-garlic)

* For the BME280 sensor we have used the [Adafruit_Python_BME280](https://github.com/adafruit/Adafruit_Python_BME280) driver


The moisture of the soil are controled by the humidity sensor via the ```mousture.py``` script that is runned at systemd.

------------------------------------------------------------------------------------
## Transfering the data 

the data is transferred via the ```ui_publish.py``` script, using [MQTT protocol](http://mqtt.org)


------------------------------------------------------------------------------------

## User interface 

The user interface was made via [node.js](https://nodejs.org/en/ "node.js")  and with it you can control the watering, CO₂  exhaustion and lights. A [raspberry camera](https://www.raspberrypi.org/products/camera-module-v2/)  functionality  was later included and you can take photos of the plant via the UI.

![](https://github.com/mieni/martian_farm/blob/master/img/UI.png)

------------------------------------------------------------------------------------

## Final product

![](https://github.com/mieni/martian_farm/blob/master/img/final.jpg)




