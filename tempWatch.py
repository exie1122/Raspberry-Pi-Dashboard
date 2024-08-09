import os
import psutil
from flask import Flask, render_template, jsonify
import time



app = Flask(__name__)

@app.route('/reboot', methods=['POST'])
def reboot():
   os.system('sudo reboot')
   return 'rebooting', 200
@app.route('/shutdown')
def shutdown():
   os.system('sudo shutdown now')
   return ('shutting down')

def get_uptime():
    uptime = os.popen("uptime -s").readline().strip()
    return uptime

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return res.replace("temp=", "").replace("'C\n", "")

def get_ram_usage():
    mem = psutil.virtual_memory()
    return mem.percent  # Returns the percentage of RAM used

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
@app.route('/status')
def status():
    temp = get_cpu_temperature()
    ram_usage = get_ram_usage()
    uptime = get_uptime()  
    cpu_usage = get_cpu_usage()
    return jsonify({
        'temperature': temp,
        'ram_usage': ram_usage,
        'uptime': uptime,
        'cpu_usage': cpu_usage 
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
