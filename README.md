# Raspberry-Pi-Dashboard
Local web based dashboard for the raspberry pi.
# Raspberry Pi Dashboard

This project is a web-based local dashboard for monitoring Raspberry Pi system metrics like CPU temperature, RAM usage, and uptime. It also includes useful buttons like activating the reboot function.

## Requirements
"""
This script requires the following Python packages:
- Flask
- psutil

Install them using:
pip install Flask psutil
"""
To use:
'''git clone https://github.com/exie1122/Raspberry-Pi-Dashboard.git
cd Raspberry-Pi-Dashboard
'''
then,
'''python3 tempWatch.py '''

to run on boot:
'''sudo nano /etc/systemd/system/tempwatch.service'''
then, add this to the file:
'''[Unit]
Description=Flask App for Raspberry Pi Status Dashboard
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/Raspberry-Pi-Dashboard/tempWatch.py
WorkingDirectory=/home/pi/Raspberry-Pi-Dashboard
Restart=always
User=pi
Environment=FLASK_ENV=production

[Install]
WantedBy=multi-user.target
'''


finally, making sure it works:
'''sudo systemctl daemon-reload
   sudo systemctl enable tempwatch.service
   sudo systemctl start tempwatch.service
'''

