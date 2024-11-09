from machine import Pin
from mfrc522 import MFRC522
import utime
       
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
 
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
                print("Card ID: "+ str(card)+" ONAY: Yeşil Işık Yakıldı")
                red.off()
                green.on()
            else:
                print("Card ID: "+ str(card)+" BİLİNMEYEN KART! Kırmızı Işık Yakıldı")
                green.off()
                red.on()