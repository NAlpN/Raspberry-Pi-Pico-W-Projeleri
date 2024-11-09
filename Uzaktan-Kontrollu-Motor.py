from machine import UART, Pin, PWM
import utime
import time

uart = UART(1, baudrate = 9600, tx = Pin(4), rx = Pin(5))
green = Pin(14, Pin.OUT)
red = Pin(15, Pin.OUT)
buzzer = Pin(13, Pin.OUT)

IN1 = Pin(19, Pin.OUT)
IN2 = Pin(18, Pin.OUT)
IN3 = Pin(17, Pin.OUT)
IN4 = Pin(16, Pin.OUT)

half_step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]


def step_motor(steps, delay):
    for _ in range(steps):
        for step in half_step_sequence:
            IN1.value(step[0])
            IN2.value(step[1])
            IN3.value(step[2])
            IN4.value(step[3])
            utime.sleep_ms(delay)
            
def rotate_forward(steps, delay=2):
    print("İleri hareket")
    step_motor(steps, delay)

def rotate_backward(steps, delay=2):
    print("Geri hareket")
    step_motor(steps, delay)

while True:
    kod = uart.read(1)
    print(kod)
    if kod is not None:
        kod = kod.decode("utf-8")
        if kod == '1':
            green.on()
            red.off()
            rotate_forward(512, 1)
        elif kod == '2':
            red.on()
            buzzer.on()
            green.off()
            rotate_backward(512, 1)
            buzzer.off()
