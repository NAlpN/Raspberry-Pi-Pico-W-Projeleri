import network
import socket
import machine
import time
import json

ssid = 'Wi-Fi'
password = 'Şifre'

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

led = machine.Pin("LED", machine.Pin.OUT)
led.off()
led_state = False

trig = machine.Pin(15, machine.Pin.OUT)
echo = machine.Pin(14, machine.Pin.IN)

def mesafe_olc():
   trig.low()
   time.sleep_us(2)
   trig.high()
   time.sleep_us(10)
   trig.low()
   while echo.value() == 0:
       signaloff = time.ticks_us()
   while echo.value() == 1:
       signalon = time.ticks_us()
   sure = signalon - signaloff
   distance = (sure * 0.0343) / 2
   return distance 

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while not ap.active():
    pass

print('WiFi aktif')
print('IP adresi:', ap.ifconfig()[0])

addr = (ap.ifconfig()[0], 80)
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Sunucu başlatıldı:', addr)

while True:
    try:
        client, addr = s.accept()
        print('İstek alındı:', addr)
        request = client.recv(1024).decode()
        print('İstek içeriği:', request)

        if 'GET /ledon' in request:
            led.on()
            led_state = True
            client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
            client.send('<html><body><h1>LED Açıldı</h1></body></html>')
            client.close()

        elif 'GET /ledoff' in request:
            led.off()
            led_state = False
            client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
            client.send('<html><body><h1>LED Kapandı</h1></body></html>')
            client.close()

        elif 'GET /durum' in request:
            reading = sensor_temp.read_u16() * conversion_factor
            sicaklik = round(27 - (reading - 0.706) / 0.001721, 2)

            mesafe = mesafe_olc()

            led_durum = "ACIK" if led_state else "KAPALI"
            durum = {
                "ledDurum": led_durum,
                "sicaklik": sicaklik,
                "mesafeDurum": f"{mesafe} cm"
            }

            response = json.dumps(durum)
            client.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + response)
            client.close()

        elif 'GET / ' in request or 'GET /index.html' in request:
            try:
                with open("pi-web.html", "r") as file:
                    html = file.read()
                client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + html)
            except Exception as e:
                print("HTML dosyası bulunamadı veya açılamadı:", e)
                client.send('HTTP/1.1 404 Not Found\r\n\r\n')
            client.close()

    except Exception as e:
        print("Hata:", e)
        client.close()