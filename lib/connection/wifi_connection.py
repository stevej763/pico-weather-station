import network
from time import sleep
import machine


class WifiConnection:

    def __init__(self, ssid, password, statusLight):
        self.statusLight = statusLight
        self.ssid = ssid
        self.password = password

    def connect(self):
        try:
            self.statusLight.off()
            ip = self.__join_network()
            self.statusLight.on()
            return ip
        except KeyboardInterrupt:
            machine.reset()

    def __join_network(self):
        print(f'joining network: {self.ssid}')
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while not wlan.isconnected():
            self.statusLight.toggle()
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip

