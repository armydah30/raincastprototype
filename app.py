from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import os

app = Flask(__name__)
app.debug = False

#config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sha256user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mrmeteo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init mySQL
mysql = MySQL(app)




#Index
@app.route('/')
def index():
    return render_template('home.html')

#About
@app.route('/about')
def about():
    return render_template('home.html')


#Meteodata
@app.route('/weatherdata')
def weatherdata():
    return render_template('weatherdata.html')


@app.route('/vxml')
def vxml():
    return render_template('test.xml')



if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='0.0.0.0', port=port)#Start listening
