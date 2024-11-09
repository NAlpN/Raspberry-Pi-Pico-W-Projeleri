from machine import Pin
import utime

IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
IN3 = Pin(18, Pin.OUT)
IN4 = Pin(19, Pin.OUT)

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

try:
    while True:
        rotate_forward(512, 2)
        utime.sleep(0.5)
        rotate_backward(512, 2)
        utime.sleep(0.5)

except KeyboardInterrupt:
    print("Program durduruldu.")