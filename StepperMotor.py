from machine import Pin
import time

l1=Pin(5,Pin.OUT)
l2=Pin(14,Pin.OUT)
l3=Pin(15,Pin.OUT)
l4=Pin(19,Pin.OUT)

a=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
b=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for j in range(500):
        for i in a:
            l1.value(i[0])
            l2.value(i[1])
            l3.value(i[2])
            l4.value(i[3])
            time.sleep_ms(5)
    for k in range(500):
        for i in b:
            l1.value(i[0])
            l2.value(i[1])
            l3.value(i[2])
            l4.value(i[3])
            time.sleep_ms(5)

