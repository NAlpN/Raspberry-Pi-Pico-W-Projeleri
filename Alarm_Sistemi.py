from machine import Pin
import utime
import math
import time

trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)
buzzer = Pin(13, Pin.OUT)
led = Pin(12, Pin.OUT)

def mesafe_olc():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(10)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   sure = signalon - signaloff
   distance = (sure * 0.0343) / 2
   return distance 

while True:  
   mesafe = mesafe_olc()
   print("Nesneye olan uzaklık ", mesafe, "cm")
   
   if mesafe < 10.0000:
       buzzer.on()
       led.on()
       time.sleep(0.25)
       led.off()
       time.sleep(0.25)
   else:
       buzzer.off()
       led.off()
   utime.sleep(0.5)