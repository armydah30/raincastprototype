from flask import Flask, render_template, request, g, flash, redirect, url_for, session, logging
from functools import wraps
import os

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

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':

	port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='0.0.0.0', port=port)#Start listening
