from flask import Flask, render_template
from threading import Thread

app = Flask('YashBot3001')

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
