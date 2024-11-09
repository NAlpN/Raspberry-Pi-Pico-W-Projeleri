from machine import UART, Pin, PWM
import utime

uart = UART(1, baudrate = 9600, tx = Pin(4), rx = Pin(5))
led = Pin(14, Pin.OUT)
                                                                                                    
while True:
    kod = uart.read(1)
    if kod is not None:
        kod = kod.decode("utf-8")
    
        if kod == '1':
            led.on()
        elif kod == '2':
            led.off()