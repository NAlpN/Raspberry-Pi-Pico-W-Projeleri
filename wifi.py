import utime
import network
import socket
import machine
import time

ssid = 'Wi-Fi adı'
password = 'Wi-Fi şifresi'

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

wait_counter = 0
while ap.active() == False:
    print("bekleniyor " + str(wait_counter))
    time.sleep(0.5)
    pass

print('WiFi aktif')
status = ap.ifconfig()
pico_ip = status[0]
print('ip = ' + status[0])

addr = (pico_ip, 80)
s = socket.socket()
s.bind(addr)
s.listen(1)
print('dinleniyor', addr)

led = machine.Pin("LED", machine.Pin.OUT)
led.off()
led_state = False


while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    sicaklik = round(27 - (reading - 0.706)/0.001721,2)
    
    client, client_addr = s.accept()
    raw_request = client.recv(1024)
    raw_request = raw_request.decode("utf-8")
    print(raw_request)

    request_parts = raw_request.split()
    http_method = request_parts[0]
    request_url = request_parts[1]

    if request_url.find("/ledon") != -1:
        led_state = True
        led.on()
    elif request_url.find("/ledoff") != -1:
        led_state = False
        led.off()
    else:
        pass

    led_state_text = "KAPALI"
    if led_state:
        led_state_text = "ACIK"

    file = open("led.html")
    html = file.read()
    file.close()

    html = html.replace('**ledState**', led_state_text)
    html = html.replace('**sicaklik**', str(sicaklik))
    client.send(html)
    client.close()