from machine import Pin
from time import sleep


class StatusLight:
    def __init__(self, pin):
        self.light = Pin(pin, Pin.OUT)

    def toggle(self):
        self.on() if self.__isOff() else self.off()

    def flash(self, flashes, interval):
        loops = flashes * 2
        for x in range(loops):
            self.toggle()
            sleep(interval)
    def off(self):
        self.light(0)

    def on(self):
        self.light(1)

    def __isOff(self):
        return self.light.value() == 0
