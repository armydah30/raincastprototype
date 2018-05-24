from flask import Flask, render_template, request, g, flash, redirect, url_for, session, logging
from functools import wraps
import os
import requests
import json
import time
import datetime

app = Flask(__name__)
app.debug = False

#Index
@app.route('/')
def index():
    return render_template('home.html')


#Meteodata
@app.route('/weatherdata')
def weatherdata():

    return render_template('weatherdata.html')


@app.route('/vxml')
def vxml():
    return render_template('test.xml')

@app.route('/vxml2')
def vxml2():
    return render_template('testFrench.xml')

@app.route('/tamale')
def tamale():
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        result = requests.get(url).json()
        result2 = requests.get(url2).json()
        text = result2['list'][0]['weather'][0]['description']

        #Day1
        dayUnix = result2['list'][0]['dt']
        ts = time.gmtime(dayUnix)
        day1_t1 = time.strftime("%A", ts)

     #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][0]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11m = int(x)
        tday12m = int(y)

      #WeatherCondition
        wCDay_1t1 = result2['list'][0]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][0]['dt']
        ts = time.gmtime(day_1Unix)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day1_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod1 = 'noon'
        else:
            day1_tod1 = 'even'
        print(day1_tod1)

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][2]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11n = int(x)
        tday12n = int(y)

      #WeatherCondition
        wCDay_1t2 = result2['list'][2]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][2]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod2 = 'noon'
        else:
            day1_tod2 = 'even'

   #time 3
        t3 = result2['list'][4]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11e = int(x)
        tday12e = int(y)

      #WeatherCondition
        wCDay_1t3 = result2['list'][4]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][4]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod3 = 'noon'
        else:
            day1_tod3 = 'even'


        #Day2
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][8]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21m = int(x)
        tday22m = int(y)

      #WeatherCondition
        wCDay_2t1 = result2['list'][8]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][8]['dt']
        ts = time.gmtime(dayUnix)
        day2_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day2_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod1 = 'noon'
        else:
            day2_tod1 = 'even'
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][10]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21n = int(x)
        tday22n = int(y)

      #WeatherCondition
        wCDay_2t2 = result2['list'][10]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][10]['dt']
        ts = time.gmtime(dayUnix)
        day2_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod2 = 'noon'
        else:
            day2_tod2 = 'even'

       #time 3
        t3 = result2['list'][12]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21e = int(x)
        tday22e = int(y)

      #WeatherCondition
        wCDay_2t3 = result2['list'][12]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][12]['dt']
        ts = time.gmtime(dayUnix)
        day2_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day2_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod3 = 'noon'
        else:
            day2_tod3 = 'even'


    #Day3
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][16]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31m = int(x)
        tday32m = int(y)

      #WeatherCondition
        wCDay_3t1 = result2['list'][16]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][16]['dt']
        ts = time.gmtime(dayUnix)
        day3_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod1 = 'noon'
        else:
            day3_tod1 = 'even'

      #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][18]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31n = int(x)
        tday32n = int(y)

      #WeatherCondition
        wCDay_3t2 = result2['list'][18]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][18]['dt']
        ts = time.gmtime(dayUnix)
        day3_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod2 = 'noon'
        else:
            day3_tod2 = 'even'

       #time 3
        t3 = result2['list'][20]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31e = int(x)
        tday32e = int(y)

      #WeatherCondition
        wCDay_3t3 = result2['list'][20]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][20]['dt']
        ts = time.gmtime(dayUnix)
        day3_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod3 = 'noon'
        else:
            day3_tod3 = 'even'

        #day4
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][24]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41m = int(x)
        tday42m = int(y)

      #WeatherCondition
        wCDay_4t1 = result2['list'][24]['weather'][0]['id']
        print(wCDay_4t1)

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][24]['dt']
        ts = time.gmtime(dayUnix)
        day4_t1 = time.strftime("%A", ts)
        print(day4_t1)
        tod = time.strftime("%H", ts)
        print(tod)
        if int(tod) < 12:
            day4_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod1 = 'noon'
        else:
            day4_tod1 = 'even'
        print(day4_tod1)
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][26]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41n = int(x)
        tday42n = int(y)

      #WeatherCondition
        wCDay_4t2 = result2['list'][26]['weather'][0]['id']
        print(wCDay_4t2)

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][26]['dt']
        ts = time.gmtime(dayUnix)
        day4_t2 = time.strftime("%A", ts)
        print(day4_t2)
        tod = time.strftime("%H", ts)
        print(tod)
        if int(tod) < 12:
            day4_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod2 = 'noon'
        else:
            day4_tod2 = 'even'
        print(day4_tod2)

       #time 3
        t3 = result2['list'][28]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41e = int(x)
        tday42e = int(y)

      #WeatherCondition
        wCDay_4t3 = result2['list'][28]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][28]['dt']
        ts = time.gmtime(dayUnix)
        day4_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod3 = 'noon'
        else:
            day4_tod3 = 'even'

        #day5
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][32]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51m = int(x)
        tday52m = int(y)

      #WeatherCondition
        wCDay_5t1 = result2['list'][32]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][32]['dt']
        ts = time.gmtime(dayUnix)
        day5_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod1 = 'noon'
        else:
            day5_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][34]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51n = int(x)
        tday52n = int(y)

      #WeatherCondition
        wCDay_5t2 = result2['list'][34]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][34]['dt']
        ts = time.gmtime(dayUnix)
        day5_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod2 = 'noon'
        else:
            day5_tod2 = 'even'

       #Time 3
        t3 = result2['list'][36]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51e = int(x)
        tday52e = int(y)

      #WeatherCondition
        wCDay_5t3 = result2['list'][36]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][36]['dt']
        ts = time.gmtime(dayUnix)
        day5_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod3 = 'noon'
        else:
            day5_tod3 = 'even'
        print(day5_tod3)


        #Currenttemperature
        temp = round(result['main']['temp'])
        temperature = str(temp)
        x = float(temperature[0])
        y= float(temperature[1])
        firstdigit = int(x)
        seconddigit = int(y)

        #Return All Data - Current anf Future Forecasts
        city_weather = {
           #Currentweather
           'city':  result['name'],
           'skye': result['weather'][0]['description'],
           'id': result['weather'][0]['id'],
           'temp': temperature,
           'fdigit': firstdigit,
           'sdigit': seconddigit,

           #Day1 Forecast Data
           'day1_time1': day1_t1,
           'day1_time2': day1_t2,
           'day1_time3': day1_t3,
           'day1_temp1_Morn': tday11m,
           'day1_temp2_Morn': tday12m,
           'day1_temp1_Noon': tday11n,
           'day1_temp2_Noon': tday12n,
           'day1_temp1_Even': tday11e,
           'day1_temp2_Even': tday12e,
           'weather_Condition_Day_1t1': wCDay_1t1,
           'weather_Condition_Day_1t2': wCDay_1t2,
           'weather_Condition_Day_1t3': wCDay_1t3,
           'day1_time_of_day1': day1_tod1,
           'day1_time_of_day2': day1_tod2,
           'day1_time_of_day3': day1_tod3,

           #Day2 Forecast Data
           'day2_time1': day2_t1,
           'day2_time2': day2_t2,
           'day2_time3': day2_t3,
           'day2_temp1_Morn': tday21m,
           'day2_temp2_Morn': tday22m,
           'day2_temp1_Noon': tday21n,
           'day2_temp2_Noon': tday22n,
           'day2_temp1_Even': tday21e,
           'day2_temp2_Even': tday22e,
           'weather_Condition_Day_2t1': wCDay_2t1,
           'weather_Condition_Day_2t2': wCDay_2t2,
           'weather_Condition_Day_2t3': wCDay_2t3,
           'day2_time_of_day1': day2_tod1,
           'day2_time_of_day2': day2_tod2,
           'day2_time_of_day3': day2_tod3,

           #Day3 Forecast Data
           'day3_time1': day3_t1,
           'day3_time2': day3_t2,
           'day3_time3': day3_t3,
           'day3_temp1_Morn': tday31m,
           'day3_temp2_Morn': tday32m,
           'day3_temp1_Noon': tday31n,
           'day3_temp2_Noon': tday32n,
           'day3_temp1_Even': tday31e,
           'day3_temp2_Even': tday32e,
           'weather_Condition_Day_3t1': wCDay_3t1,
           'weather_Condition_Day_3t2': wCDay_3t2,
           'weather_Condition_Day_3t3': wCDay_3t3,
           'day3_time_of_day1': day3_tod1,
           'day3_time_of_day2': day3_tod2,
           'day3_time_of_day3': day3_tod3,

           #Day4 Forecast Data
           'day4_time1': day4_t1,
           'day4_time2': day4_t2,
           'day4_time3': day4_t3,
           'day4_temp1_Morn': tday41m,
           'day4_temp2_Morn': tday42m,
           'day4_temp1_Noon': tday41n,
           'day4_temp2_Noon': tday42n,
           'day4_temp1_Even': tday41e,
           'day4_temp2_Even': tday42e,
           'weather_Condition_Day_4t1': wCDay_4t1,
           'weather_Condition_Day_4t2': wCDay_4t2,
           'weather_Condition_Day_4t3': wCDay_4t3,
           'day4_time_of_day1': day4_tod1,
           'day4_time_of_day2': day4_tod2,
           'day4_time_of_day3': day4_tod3,

           #Day5 Forecast Data
           'day5_time1': day5_t1,
           'day5_time2': day5_t2,
           'day5_time3': day5_t3,
           'day5_temp1_Morn': tday51m,
           'day5_temp2_Morn': tday52m,
           'day5_temp1_Noon': tday51n,
           'day5_temp2_Noon': tday52n,
           'day5_temp1_Even': tday51e,
           'day5_temp2_Even': tday52e,
           'weather_Condition_Day_5t1': wCDay_5t1,
           'weather_Condition_Day_5t2': wCDay_5t2,
           'weather_Condition_Day_5t3': wCDay_5t3,
           'day5_time_of_day1': day5_tod1,
           'day5_time_of_day2': day5_tod2,
           'day5_time_of_day3': day5_tod3,
        }
        print(city_weather)
        context = {'city_weather': city_weather}
        return render_template('tamale.xml', context=context)

@app.route('/bolgatanga')
def bolgatanga():
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=10.7833&lon=-0.8500&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=10.7833&lon=-0.8500&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        result = requests.get(url).json()
        result2 = requests.get(url2).json()
        text = result2['list'][0]['weather'][0]['description']

        #Day1
        dayUnix = result2['list'][0]['dt']
        ts = time.gmtime(dayUnix)
        day1_t1 = time.strftime("%A", ts)

     #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][0]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11m = int(x)
        tday12m = int(y)

      #WeatherCondition
        wCDay_1t1 = result2['list'][0]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][0]['dt']
        ts = time.gmtime(day_1Unix)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day1_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod1 = 'noon'
        else:
            day1_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][2]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11n = int(x)
        tday12n = int(y)

      #WeatherCondition
        wCDay_1t2 = result2['list'][2]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][2]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod2 = 'noon'
        else:
            day1_tod2 = 'even'

   #time 3
        t3 = result2['list'][4]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11e = int(x)
        tday12e = int(y)

      #WeatherCondition
        wCDay_1t3 = result2['list'][4]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][4]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod3 = 'noon'
        else:
            day1_tod3 = 'even'

        #Day2
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][8]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21m = int(x)
        tday22m = int(y)

      #WeatherCondition
        wCDay_2t1 = result2['list'][8]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][8]['dt']
        ts = time.gmtime(dayUnix)
        day2_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod1 = 'noon'
        else:
            day2_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][10]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21n = int(x)
        tday22n = int(y)

      #WeatherCondition
        wCDay_2t2 = result2['list'][10]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][10]['dt']
        ts = time.gmtime(dayUnix)
        day2_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod2 = 'noon'
        else:
            day2_tod2 = 'even'

       #time 3
        t3 = result2['list'][12]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21e = int(x)
        tday22e = int(y)

      #WeatherCondition
        wCDay_2t3 = result2['list'][12]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][12]['dt']
        ts = time.gmtime(dayUnix)
        day2_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod3 = 'noon'
        else:
            day2_tod3 = 'even'

    #Day3
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][16]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31m = int(x)
        tday32m = int(y)

      #WeatherCondition
        wCDay_3t1 = result2['list'][16]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][16]['dt']
        ts = time.gmtime(dayUnix)
        day3_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod1 = 'noon'
        else:
            day3_tod1 = 'even'

      #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][18]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31n = int(x)
        tday32n = int(y)

      #WeatherCondition
        wCDay_3t2 = result2['list'][18]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][18]['dt']
        ts = time.gmtime(dayUnix)
        day3_t2 = time.strftime("%A", ts)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day3_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod2 = 'noon'
        else:
            day3_tod2 = 'even'


       #time 3
        t3 = result2['list'][20]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31e = int(x)
        tday32e = int(y)

      #WeatherCondition
        wCDay_3t3 = result2['list'][20]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][20]['dt']
        ts = time.gmtime(dayUnix)
        day3_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod3 = 'noon'
        else:
            day3_tod3 = 'even'

        #day4
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][24]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41m = int(x)
        tday42m = int(y)

      #WeatherCondition
        wCDay_4t1 = result2['list'][24]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][24]['dt']
        ts = time.gmtime(dayUnix)
        day4_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod1 = 'noon'
        else:
            day4_tod1 = 'even'
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][26]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41n = int(x)
        tday42n = int(y)

      #WeatherCondition
        wCDay_4t2 = result2['list'][26]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][26]['dt']
        ts = time.gmtime(dayUnix)
        day4_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day4_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod2 = 'noon'
        else:
            day4_tod2 = 'even'

       #time 3
        t3 = result2['list'][28]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41e = int(x)
        tday42e = int(y)

      #WeatherCondition
        wCDay_4t3 = result2['list'][28]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][28]['dt']
        ts = time.gmtime(dayUnix)
        day4_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod3 = 'noon'
        else:
            day4_tod3 = 'even'

        #day5
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][32]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51m = int(x)
        tday52m = int(y)

      #WeatherCondition
        wCDay_5t1 = result2['list'][32]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][32]['dt']
        ts = time.gmtime(dayUnix)
        day5_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod1 = 'noon'
        else:
            day5_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][34]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51n = int(x)
        tday52n = int(y)

      #WeatherCondition
        wCDay_5t2 = result2['list'][34]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][34]['dt']
        ts = time.gmtime(dayUnix)
        day5_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod2 = 'noon'
        else:
            day5_tod2 = 'even'

       #Time 3
        t3 = result2['list'][36]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51e = int(x)
        tday52e = int(y)

      #WeatherCondition
        wCDay_5t3 = result2['list'][36]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][36]['dt']
        ts = time.gmtime(dayUnix)
        day5_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod3 = 'noon'
        else:
            day5_tod3 = 'even'
        print(day5_tod3)


        #Currenttemperature
        temp = round(result['main']['temp'])
        temperature = str(temp)
        x = float(temperature[0])
        y= float(temperature[1])
        firstdigit = int(x)
        seconddigit = int(y)

        #Return All Data - Current anf Future Forecasts
        city_weather = {
           #Currentweather
           'city':  result['name'],
           'skye': result['weather'][0]['description'],
           'id': result['weather'][0]['id'],
           'temp': temperature,
           'fdigit': firstdigit,
           'sdigit': seconddigit,

           #Day1 Forecast Data
           'day1_time1': day1_t1,
           'day1_time2': day1_t2,
           'day1_time3': day1_t3,
           'day1_temp1_Morn': tday11m,
           'day1_temp2_Morn': tday12m,
           'day1_temp1_Noon': tday11n,
           'day1_temp2_Noon': tday12n,
           'day1_temp1_Even': tday11e,
           'day1_temp2_Even': tday12e,
           'weather_Condition_Day_1t1': wCDay_1t1,
           'weather_Condition_Day_1t2': wCDay_1t2,
           'weather_Condition_Day_1t3': wCDay_1t3,
           'day1_time_of_day1': day1_tod1,
           'day1_time_of_day2': day1_tod2,
           'day1_time_of_day3': day1_tod3,

           #Day2 Forecast Data
           'day2_time1': day2_t1,
           'day2_time2': day2_t2,
           'day2_time3': day2_t3,
           'day2_temp1_Morn': tday21m,
           'day2_temp2_Morn': tday22m,
           'day2_temp1_Noon': tday21n,
           'day2_temp2_Noon': tday22n,
           'day2_temp1_Even': tday21e,
           'day2_temp2_Even': tday22e,
           'weather_Condition_Day_2t1': wCDay_2t1,
           'weather_Condition_Day_2t2': wCDay_2t2,
           'weather_Condition_Day_2t3': wCDay_2t3,
           'day2_time_of_day1': day2_tod1,
           'day2_time_of_day2': day2_tod2,
           'day2_time_of_day3': day2_tod3,

           #Day3 Forecast Data
           'day3_time1': day3_t1,
           'day3_time2': day3_t2,
           'day3_time3': day3_t3,
           'day3_temp1_Morn': tday31m,
           'day3_temp2_Morn': tday32m,
           'day3_temp1_Noon': tday31n,
           'day3_temp2_Noon': tday32n,
           'day3_temp1_Even': tday31e,
           'day3_temp2_Even': tday32e,
           'weather_Condition_Day_3t1': wCDay_3t1,
           'weather_Condition_Day_3t2': wCDay_3t2,
           'weather_Condition_Day_3t3': wCDay_3t3,
           'day3_time_of_day1': day3_tod1,
           'day3_time_of_day2': day3_tod2,
           'day3_time_of_day3': day3_tod3,

           #Day4 Forecast Data
           'day4_time1': day4_t1,
           'day4_time2': day4_t2,
           'day4_time3': day4_t3,
           'day4_temp1_Morn': tday41m,
           'day4_temp2_Morn': tday42m,
           'day4_temp1_Noon': tday41n,
           'day4_temp2_Noon': tday42n,
           'day4_temp1_Even': tday41e,
           'day4_temp2_Even': tday42e,
           'weather_Condition_Day_4t1': wCDay_4t1,
           'weather_Condition_Day_4t2': wCDay_4t2,
           'weather_Condition_Day_4t3': wCDay_4t3,
           'day4_time_of_day1': day4_tod1,
           'day4_time_of_day2': day4_tod2,
           'day4_time_of_day3': day4_tod3,

           #Day5 Forecast Data
           'day5_time1': day5_t1,
           'day5_time2': day5_t2,
           'day5_time3': day5_t3,
           'day5_temp1_Morn': tday51m,
           'day5_temp2_Morn': tday52m,
           'day5_temp1_Noon': tday51n,
           'day5_temp2_Noon': tday52n,
           'day5_temp1_Even': tday51e,
           'day5_temp2_Even': tday52e,
           'weather_Condition_Day_5t1': wCDay_5t1,
           'weather_Condition_Day_5t2': wCDay_5t2,
           'weather_Condition_Day_5t3': wCDay_5t3,
           'day5_time_of_day1': day5_tod1,
           'day5_time_of_day2': day5_tod2,
           'day5_time_of_day3': day5_tod3,
        }
        print(city_weather)
        context = {'city_weather': city_weather}
        return render_template('bolgatanga.xml', context=context)

@app.route('/tamale2')
def tamale2():
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        result = requests.get(url).json()
        result2 = requests.get(url2).json()
        text = result2['list'][0]['weather'][0]['description']

        #Day1
        dayUnix = result2['list'][0]['dt']
        ts = time.gmtime(dayUnix)
        day1_t1 = time.strftime("%A", ts)

     #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][0]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11m = int(x)
        tday12m = int(y)

      #WeatherCondition
        wCDay_1t1 = result2['list'][0]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][0]['dt']
        ts = time.gmtime(day_1Unix)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day1_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod1 = 'noon'
        else:
            day1_tod1 = 'even'
        print(day1_tod1)

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][2]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11n = int(x)
        tday12n = int(y)

      #WeatherCondition
        wCDay_1t2 = result2['list'][2]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][2]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod2 = 'noon'
        else:
            day1_tod2 = 'even'

   #time 3
        t3 = result2['list'][4]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11e = int(x)
        tday12e = int(y)

      #WeatherCondition
        wCDay_1t3 = result2['list'][4]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][4]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod3 = 'noon'
        else:
            day1_tod3 = 'even'


        #Day2
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][8]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21m = int(x)
        tday22m = int(y)

      #WeatherCondition
        wCDay_2t1 = result2['list'][8]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][8]['dt']
        ts = time.gmtime(dayUnix)
        day2_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day2_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod1 = 'noon'
        else:
            day2_tod1 = 'even'
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][10]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21n = int(x)
        tday22n = int(y)

      #WeatherCondition
        wCDay_2t2 = result2['list'][10]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][10]['dt']
        ts = time.gmtime(dayUnix)
        day2_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod2 = 'noon'
        else:
            day2_tod2 = 'even'

       #time 3
        t3 = result2['list'][12]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21e = int(x)
        tday22e = int(y)

      #WeatherCondition
        wCDay_2t3 = result2['list'][12]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][12]['dt']
        ts = time.gmtime(dayUnix)
        day2_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day2_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod3 = 'noon'
        else:
            day2_tod3 = 'even'


    #Day3
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][16]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31m = int(x)
        tday32m = int(y)

      #WeatherCondition
        wCDay_3t1 = result2['list'][16]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][16]['dt']
        ts = time.gmtime(dayUnix)
        day3_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod1 = 'noon'
        else:
            day3_tod1 = 'even'

      #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][18]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31n = int(x)
        tday32n = int(y)

      #WeatherCondition
        wCDay_3t2 = result2['list'][18]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][18]['dt']
        ts = time.gmtime(dayUnix)
        day3_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod2 = 'noon'
        else:
            day3_tod2 = 'even'

       #time 3
        t3 = result2['list'][20]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31e = int(x)
        tday32e = int(y)

      #WeatherCondition
        wCDay_3t3 = result2['list'][20]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][20]['dt']
        ts = time.gmtime(dayUnix)
        day3_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod3 = 'noon'
        else:
            day3_tod3 = 'even'

        #day4
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][24]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41m = int(x)
        tday42m = int(y)

      #WeatherCondition
        wCDay_4t1 = result2['list'][24]['weather'][0]['id']
        print(wCDay_4t1)

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][24]['dt']
        ts = time.gmtime(dayUnix)
        day4_t1 = time.strftime("%A", ts)
        print(day4_t1)
        tod = time.strftime("%H", ts)
        print(tod)
        if int(tod) < 12:
            day4_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod1 = 'noon'
        else:
            day4_tod1 = 'even'
        print(day4_tod1)
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][26]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41n = int(x)
        tday42n = int(y)

      #WeatherCondition
        wCDay_4t2 = result2['list'][26]['weather'][0]['id']
        print(wCDay_4t2)

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][26]['dt']
        ts = time.gmtime(dayUnix)
        day4_t2 = time.strftime("%A", ts)
        print(day4_t2)
        tod = time.strftime("%H", ts)
        print(tod)
        if int(tod) < 12:
            day4_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod2 = 'noon'
        else:
            day4_tod2 = 'even'
        print(day4_tod2)

       #time 3
        t3 = result2['list'][28]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41e = int(x)
        tday42e = int(y)

      #WeatherCondition
        wCDay_4t3 = result2['list'][28]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][28]['dt']
        ts = time.gmtime(dayUnix)
        day4_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod3 = 'noon'
        else:
            day4_tod3 = 'even'

        #day5
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][32]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51m = int(x)
        tday52m = int(y)

      #WeatherCondition
        wCDay_5t1 = result2['list'][32]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][32]['dt']
        ts = time.gmtime(dayUnix)
        day5_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod1 = 'noon'
        else:
            day5_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][34]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51n = int(x)
        tday52n = int(y)

      #WeatherCondition
        wCDay_5t2 = result2['list'][34]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][34]['dt']
        ts = time.gmtime(dayUnix)
        day5_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod2 = 'noon'
        else:
            day5_tod2 = 'even'

       #Time 3
        t3 = result2['list'][36]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51e = int(x)
        tday52e = int(y)

      #WeatherCondition
        wCDay_5t3 = result2['list'][36]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][36]['dt']
        ts = time.gmtime(dayUnix)
        day5_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod3 = 'noon'
        else:
            day5_tod3 = 'even'
        print(day5_tod3)


        #Currenttemperature
        temp = round(result['main']['temp'])
        temperature = str(temp)
        x = float(temperature[0])
        y= float(temperature[1])
        firstdigit = int(x)
        seconddigit = int(y)

        #Return All Data - Current anf Future Forecasts
        city_weather = {
           #Currentweather
           'city':  result['name'],
           'skye': result['weather'][0]['description'],
           'id': result['weather'][0]['id'],
           'temp': temperature,
           'fdigit': firstdigit,
           'sdigit': seconddigit,

           #Day1 Forecast Data
           'day1_time1': day1_t1,
           'day1_time2': day1_t2,
           'day1_time3': day1_t3,
           'day1_temp1_Morn': tday11m,
           'day1_temp2_Morn': tday12m,
           'day1_temp1_Noon': tday11n,
           'day1_temp2_Noon': tday12n,
           'day1_temp1_Even': tday11e,
           'day1_temp2_Even': tday12e,
           'weather_Condition_Day_1t1': wCDay_1t1,
           'weather_Condition_Day_1t2': wCDay_1t2,
           'weather_Condition_Day_1t3': wCDay_1t3,
           'day1_time_of_day1': day1_tod1,
           'day1_time_of_day2': day1_tod2,
           'day1_time_of_day3': day1_tod3,

           #Day2 Forecast Data
           'day2_time1': day2_t1,
           'day2_time2': day2_t2,
           'day2_time3': day2_t3,
           'day2_temp1_Morn': tday21m,
           'day2_temp2_Morn': tday22m,
           'day2_temp1_Noon': tday21n,
           'day2_temp2_Noon': tday22n,
           'day2_temp1_Even': tday21e,
           'day2_temp2_Even': tday22e,
           'weather_Condition_Day_2t1': wCDay_2t1,
           'weather_Condition_Day_2t2': wCDay_2t2,
           'weather_Condition_Day_2t3': wCDay_2t3,
           'day2_time_of_day1': day2_tod1,
           'day2_time_of_day2': day2_tod2,
           'day2_time_of_day3': day2_tod3,

           #Day3 Forecast Data
           'day3_time1': day3_t1,
           'day3_time2': day3_t2,
           'day3_time3': day3_t3,
           'day3_temp1_Morn': tday31m,
           'day3_temp2_Morn': tday32m,
           'day3_temp1_Noon': tday31n,
           'day3_temp2_Noon': tday32n,
           'day3_temp1_Even': tday31e,
           'day3_temp2_Even': tday32e,
           'weather_Condition_Day_3t1': wCDay_3t1,
           'weather_Condition_Day_3t2': wCDay_3t2,
           'weather_Condition_Day_3t3': wCDay_3t3,
           'day3_time_of_day1': day3_tod1,
           'day3_time_of_day2': day3_tod2,
           'day3_time_of_day3': day3_tod3,

           #Day4 Forecast Data
           'day4_time1': day4_t1,
           'day4_time2': day4_t2,
           'day4_time3': day4_t3,
           'day4_temp1_Morn': tday41m,
           'day4_temp2_Morn': tday42m,
           'day4_temp1_Noon': tday41n,
           'day4_temp2_Noon': tday42n,
           'day4_temp1_Even': tday41e,
           'day4_temp2_Even': tday42e,
           'weather_Condition_Day_4t1': wCDay_4t1,
           'weather_Condition_Day_4t2': wCDay_4t2,
           'weather_Condition_Day_4t3': wCDay_4t3,
           'day4_time_of_day1': day4_tod1,
           'day4_time_of_day2': day4_tod2,
           'day4_time_of_day3': day4_tod3,

           #Day5 Forecast Data
           'day5_time1': day5_t1,
           'day5_time2': day5_t2,
           'day5_time3': day5_t3,
           'day5_temp1_Morn': tday51m,
           'day5_temp2_Morn': tday52m,
           'day5_temp1_Noon': tday51n,
           'day5_temp2_Noon': tday52n,
           'day5_temp1_Even': tday51e,
           'day5_temp2_Even': tday52e,
           'weather_Condition_Day_5t1': wCDay_5t1,
           'weather_Condition_Day_5t2': wCDay_5t2,
           'weather_Condition_Day_5t3': wCDay_5t3,
           'day5_time_of_day1': day5_tod1,
           'day5_time_of_day2': day5_tod2,
           'day5_time_of_day3': day5_tod3,
        }
        print(city_weather)
        context = {'city_weather': city_weather}
        return render_template('tamale2.xml', context=context)

@app.route('/bolgatanga2')
def bolgatanga2():
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=10.7833&lon=-0.8500&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=10.7833&lon=-0.8500&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        result = requests.get(url).json()
        result2 = requests.get(url2).json()
        text = result2['list'][0]['weather'][0]['description']

        #Day1
        dayUnix = result2['list'][0]['dt']
        ts = time.gmtime(dayUnix)
        day1_t1 = time.strftime("%A", ts)

     #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][0]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11m = int(x)
        tday12m = int(y)

      #WeatherCondition
        wCDay_1t1 = result2['list'][0]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][0]['dt']
        ts = time.gmtime(day_1Unix)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day1_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod1 = 'noon'
        else:
            day1_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][2]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11n = int(x)
        tday12n = int(y)

      #WeatherCondition
        wCDay_1t2 = result2['list'][2]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][2]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod2 = 'noon'
        else:
            day1_tod2 = 'even'

   #time 3
        t3 = result2['list'][4]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday11e = int(x)
        tday12e = int(y)

      #WeatherCondition
        wCDay_1t3 = result2['list'][4]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        day_1Unix = result2['list'][4]['dt']
        ts = time.gmtime(day_1Unix)
        day1_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day1_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day1_tod3 = 'noon'
        else:
            day1_tod3 = 'even'

        #Day2
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][8]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21m = int(x)
        tday22m = int(y)

      #WeatherCondition
        wCDay_2t1 = result2['list'][8]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][8]['dt']
        ts = time.gmtime(dayUnix)
        day2_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod1 = 'noon'
        else:
            day2_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][10]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21n = int(x)
        tday22n = int(y)

      #WeatherCondition
        wCDay_2t2 = result2['list'][10]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][10]['dt']
        ts = time.gmtime(dayUnix)
        day2_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod2 = 'noon'
        else:
            day2_tod2 = 'even'

       #time 3
        t3 = result2['list'][12]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday21e = int(x)
        tday22e = int(y)

      #WeatherCondition
        wCDay_2t3 = result2['list'][12]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][12]['dt']
        ts = time.gmtime(dayUnix)
        day2_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day2_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day2_tod3 = 'noon'
        else:
            day2_tod3 = 'even'

    #Day3
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][16]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31m = int(x)
        tday32m = int(y)

      #WeatherCondition
        wCDay_3t1 = result2['list'][16]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][16]['dt']
        ts = time.gmtime(dayUnix)
        day3_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod1 = 'noon'
        else:
            day3_tod1 = 'even'

      #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][18]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31n = int(x)
        tday32n = int(y)

      #WeatherCondition
        wCDay_3t2 = result2['list'][18]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][18]['dt']
        ts = time.gmtime(dayUnix)
        day3_t2 = time.strftime("%A", ts)
        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day3_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod2 = 'noon'
        else:
            day3_tod2 = 'even'


       #time 3
        t3 = result2['list'][20]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday31e = int(x)
        tday32e = int(y)

      #WeatherCondition
        wCDay_3t3 = result2['list'][20]['weather'][0]['id']


      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][20]['dt']
        ts = time.gmtime(dayUnix)
        day3_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day3_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day3_tod3 = 'noon'
        else:
            day3_tod3 = 'even'

        #day4
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][24]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41m = int(x)
        tday42m = int(y)

      #WeatherCondition
        wCDay_4t1 = result2['list'][24]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][24]['dt']
        ts = time.gmtime(dayUnix)
        day4_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod1 = 'noon'
        else:
            day4_tod1 = 'even'
    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][26]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41n = int(x)
        tday42n = int(y)

      #WeatherCondition
        wCDay_4t2 = result2['list'][26]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][26]['dt']
        ts = time.gmtime(dayUnix)
        day4_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)

        if int(tod) < 12:
            day4_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod2 = 'noon'
        else:
            day4_tod2 = 'even'

       #time 3
        t3 = result2['list'][28]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday41e = int(x)
        tday42e = int(y)

      #WeatherCondition
        wCDay_4t3 = result2['list'][28]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][28]['dt']
        ts = time.gmtime(dayUnix)
        day4_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day4_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day4_tod3 = 'noon'
        else:
            day4_tod3 = 'even'

        #day5
    #time 1:
      #Get temperature and split into two integers
        t1 = result2['list'][32]['main']['temp']
        temperature = str(t1)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51m = int(x)
        tday52m = int(y)

      #WeatherCondition
        wCDay_5t1 = result2['list'][32]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][32]['dt']
        ts = time.gmtime(dayUnix)
        day5_t1 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod1 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod1 = 'noon'
        else:
            day5_tod1 = 'even'

    #time 2
      #Get temperature and split into two integers
        t2 = result2['list'][34]['main']['temp']
        temperature = str(t2)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51n = int(x)
        tday52n = int(y)

      #WeatherCondition
        wCDay_5t2 = result2['list'][34]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][34]['dt']
        ts = time.gmtime(dayUnix)
        day5_t2 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod2 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod2 = 'noon'
        else:
            day5_tod2 = 'even'

       #Time 3
        t3 = result2['list'][36]['main']['temp']
        temperature = str(t3)
        x = float(temperature[0])
        y= float(temperature[1])
        tday51e = int(x)
        tday52e = int(y)

      #WeatherCondition
        wCDay_5t3 = result2['list'][36]['weather'][0]['id']

      #Get time of the day as noon, morning or evening
        dayUnix = result2['list'][36]['dt']
        ts = time.gmtime(dayUnix)
        day5_t3 = time.strftime("%A", ts)

        tod = time.strftime("%H", ts)
        if int(tod) < 12:
            day5_tod3 = 'morn'
        elif 12 <= int(tod) < 18:
            day5_tod3 = 'noon'
        else:
            day5_tod3 = 'even'
        print(day5_tod3)


        #Currenttemperature
        temp = round(result['main']['temp'])
        temperature = str(temp)
        x = float(temperature[0])
        y= float(temperature[1])
        firstdigit = int(x)
        seconddigit = int(y)

        #Return All Data - Current anf Future Forecasts
        city_weather = {
           #Currentweather
           'city':  result['name'],
           'skye': result['weather'][0]['description'],
           'id': result['weather'][0]['id'],
           'temp': temperature,
           'fdigit': firstdigit,
           'sdigit': seconddigit,

           #Day1 Forecast Data
           'day1_time1': day1_t1,
           'day1_time2': day1_t2,
           'day1_time3': day1_t3,
           'day1_temp1_Morn': tday11m,
           'day1_temp2_Morn': tday12m,
           'day1_temp1_Noon': tday11n,
           'day1_temp2_Noon': tday12n,
           'day1_temp1_Even': tday11e,
           'day1_temp2_Even': tday12e,
           'weather_Condition_Day_1t1': wCDay_1t1,
           'weather_Condition_Day_1t2': wCDay_1t2,
           'weather_Condition_Day_1t3': wCDay_1t3,
           'day1_time_of_day1': day1_tod1,
           'day1_time_of_day2': day1_tod2,
           'day1_time_of_day3': day1_tod3,

           #Day2 Forecast Data
           'day2_time1': day2_t1,
           'day2_time2': day2_t2,
           'day2_time3': day2_t3,
           'day2_temp1_Morn': tday21m,
           'day2_temp2_Morn': tday22m,
           'day2_temp1_Noon': tday21n,
           'day2_temp2_Noon': tday22n,
           'day2_temp1_Even': tday21e,
           'day2_temp2_Even': tday22e,
           'weather_Condition_Day_2t1': wCDay_2t1,
           'weather_Condition_Day_2t2': wCDay_2t2,
           'weather_Condition_Day_2t3': wCDay_2t3,
           'day2_time_of_day1': day2_tod1,
           'day2_time_of_day2': day2_tod2,
           'day2_time_of_day3': day2_tod3,

           #Day3 Forecast Data
           'day3_time1': day3_t1,
           'day3_time2': day3_t2,
           'day3_time3': day3_t3,
           'day3_temp1_Morn': tday31m,
           'day3_temp2_Morn': tday32m,
           'day3_temp1_Noon': tday31n,
           'day3_temp2_Noon': tday32n,
           'day3_temp1_Even': tday31e,
           'day3_temp2_Even': tday32e,
           'weather_Condition_Day_3t1': wCDay_3t1,
           'weather_Condition_Day_3t2': wCDay_3t2,
           'weather_Condition_Day_3t3': wCDay_3t3,
           'day3_time_of_day1': day3_tod1,
           'day3_time_of_day2': day3_tod2,
           'day3_time_of_day3': day3_tod3,

           #Day4 Forecast Data
           'day4_time1': day4_t1,
           'day4_time2': day4_t2,
           'day4_time3': day4_t3,
           'day4_temp1_Morn': tday41m,
           'day4_temp2_Morn': tday42m,
           'day4_temp1_Noon': tday41n,
           'day4_temp2_Noon': tday42n,
           'day4_temp1_Even': tday41e,
           'day4_temp2_Even': tday42e,
           'weather_Condition_Day_4t1': wCDay_4t1,
           'weather_Condition_Day_4t2': wCDay_4t2,
           'weather_Condition_Day_4t3': wCDay_4t3,
           'day4_time_of_day1': day4_tod1,
           'day4_time_of_day2': day4_tod2,
           'day4_time_of_day3': day4_tod3,

           #Day5 Forecast Data
           'day5_time1': day5_t1,
           'day5_time2': day5_t2,
           'day5_time3': day5_t3,
           'day5_temp1_Morn': tday51m,
           'day5_temp2_Morn': tday52m,
           'day5_temp1_Noon': tday51n,
           'day5_temp2_Noon': tday52n,
           'day5_temp1_Even': tday51e,
           'day5_temp2_Even': tday52e,
           'weather_Condition_Day_5t1': wCDay_5t1,
           'weather_Condition_Day_5t2': wCDay_5t2,
           'weather_Condition_Day_5t3': wCDay_5t3,
           'day5_time_of_day1': day5_tod1,
           'day5_time_of_day2': day5_tod2,
           'day5_time_of_day3': day5_tod3,
        }
        print(city_weather)
        context = {'city_weather': city_weather}
        return render_template('bolgatanga2.xml', context=context)



if __name__ == '__main__':
    #app.run()
	port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='0.0.0.0', port=port)#Start listening
