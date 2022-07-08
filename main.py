from machine import Pin
import usocket as socket
import network
import time
import gc

# import uasyncio as asyncio

import urls

'''
Replace SSID and Password of your Wi-Fi
'''
# WIFI Informations
SSID = 'D-Link'
PASSWORD = '0555140236'
PORT = 80

# Init Station
station = network.WLAN(network.STA_IF)

# Enabling Station
station.active(True)

'''
You can use a static IP by uncommenting lines below and replace the IP Address that matches your network 
'''
# Setting up static IP
# station.ifconfig(('192.168.1.200', '255.255.255.0', '192.168.1.1', '8.8.8.8'))

# Connect to WI-FI
station.connect(SSID, PASSWORD)

'''
When Pin 14 turns off, this means that the ESP is connected to Wi-Fi, this can be used with an LED
'''
# Getting LED
led = Pin(14, Pin.OUT)

print(f'Trying to connect to {SSID}')
led.on()
# Connecting to Wifi
while not station.isconnected():
  time.sleep(5)
current_config = station.ifconfig()
print(f'Connected to {SSID}\n{current_config}')
led.off()

print('Starting Server...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.settimeout(10)
s.listen(5)
print(f'Server Started at {current_config[0]} on port {PORT}')

while True:
    try:
        # Freeing Memory
        gc.collect()
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        response = urls.router(request)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except Exception:
        continue
