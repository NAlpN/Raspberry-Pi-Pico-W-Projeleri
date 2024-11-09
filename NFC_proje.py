from machine import Pin
from mfrc522 import MFRC522
import utime
import time
       
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)
blue = Pin(12, Pin.OUT)
 
print("RFID kartını yaklaştırın...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == "RFID Numarası":
                print("Giriş Başarılı!")
                green.on()
                red.off()
                yellow.off()
                blue.off()
                time.sleep(1)
                green.off()
                red.off()
                yellow.off()
                blue.off()
            else:
                print("Card ID: "+ str(card)+" BİLİNMEYEN KART!")
                red.on()
                green.on()
                yellow.on()
                blue.on()
                time.sleep(0.25)
                red.off()
                green.off()
                yellow.off()
                blue.off()
                time.sleep(0.25)