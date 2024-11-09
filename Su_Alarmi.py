from machine import ADC, Pin
from time import sleep

water_sensor = ADC(Pin(26))
buzzer = Pin(15, Pin.OUT)
led = Pin(14, Pin.OUT)

while True:
    value = water_sensor.read_u16()
    voltage = value * (3.3 / 65535)

    print("Su sensörü değeri:", value)
    print("Voltaj (V):", voltage)
    
    if value > 30000:
        print("Su seviyesi algılandı!")
        buzzer.on()
        led.on()
        sleep(0.25)
        led.off()
        sleep(0.25)
    else:
        print("Su seviyesi düşük veya yok.")
        buzzer.off()
        led.off()
        
    sleep(1)