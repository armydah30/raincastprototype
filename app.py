from flask import Flask, render_template, request, g, flash, redirect, url_for, session, logging
from functools import wraps
import os
import requests
import json

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
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=10.7833&lon=-0.8500&units=metric&appid=454d3e3138f204980589ae958b2a9728'

        result = requests.get(url).json()
        print(result)
        temp = round(result['main']['temp'])
        city_weather = {
           'city':  result['name'],
           'country': result['sys']['country'],
           'icon': result['weather'][0]['icon'],
           'skye': result['weather'][0]['description'],
           'temp': temp,
        }
        context = {'city_weather': city_weather}
        return render_template('tamale.xml', context=context)

@app.route('/bolgatanga')
def bolgatanga():
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        #url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=9.3999984&lon=-0.8499966&units=metric&appid=454d3e3138f204980589ae958b2a9728'
        result = requests.get(url).json()
        #result2 = requests.get(url2).json()
        print(result)
        temp = round(result['main']['temp'])
        temperature = str(temp)
        x = float(temperature[0])
        y= float(temperature[1])
        firstdigit = int(x)
        seconddigit = int(y)
        print(firstdigit)
        print(seconddigit)
        city_weather = {
           'city':  result['name'],
           'skye': result['weather'][0]['description'],
           'id': result['weather'][0]['id'],
           'temp': temperature,
           'fdigit': firstdigit,
           'sdigit': seconddigit,
        }
        print(city_weather)
        context = {'city_weather': city_weather}
        return render_template('bolgatanga.xml', context=context)

@app.route('/tamale2')
def tamale2():
    return render_template('tamale2.xml')

@app.route('/bolgatanga2')
def bolgatanga2():
    return render_template('bolgatanga2.xml')


@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    #app.run()
	port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='0.0.0.0', port=port)#Start listening
