from machine import ADC, Pin
from time import sleep

adc_pin = ADC(26)
buzzer = Pin(13, Pin.OUT)
led = Pin(12, Pin.OUT)

while True:
    ses_degeri = adc_pin.read_u16()
    print("Ses Seviyesi: ", ses_degeri)
    if ses_degeri > 5000:
        buzzer.on()
        led.on()
        sleep(0.25)
        led.off()
        sleep(0.25)
        led.on()
    else:
        buzzer.off()
        led.off()
    sleep(0.1)
