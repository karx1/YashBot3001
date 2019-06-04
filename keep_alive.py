#this is the flask code to keep the bot running 24/7
from flask import Flask
from threading import Thread
from flask import render_template

app = Flask('')

@app.route('/')
def home():
    return render_template('changelog.html')

@app.route('/invite')
def invite():
    return render_template('invite.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
