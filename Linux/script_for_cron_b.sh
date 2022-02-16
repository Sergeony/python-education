#!/bin/bash

curl "http://api.openweathermap.org/data/2.5/weather?lat=49.9923181&lon=36.2310146&appid=70a2ab1c2a009dbb267f11fe6c7350fe" >> weather_list.txt

#отступы между JSON объектами
echo >> weather_list.txt

# 0 12 * * * /home/serga/Documents/python-education/Linux/script_for_cron_b.sh

