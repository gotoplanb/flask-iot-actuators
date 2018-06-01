from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/fan')
def fan():
    speed = request.args.get('speed')
    if speed == 'high':
        # turn fan to high
        return f'Fan speed changed to {speed}'
    elif speed == 'low':
        # turn fan to low
        return f'Fan speed changed to {speed}'
    elif speed == 'off':
        # turn fan off
        return f'Fan speed changed to {speed}'
    else:
        return 'Unknown value. Nothing done.'