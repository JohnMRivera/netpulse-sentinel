from core.database import DBConnection

class Device:

    def __init__(self, device_id, device_ip, device_mac, device_status):
        self.device_id = device_id
        self.device_ip = device_ip
        self.device_mac = device_mac
        self.device_status = device_status

    # @property
    # def deviceIp(self):
    #     return self.device_ip
    
    # @deviceIp.setter
    # def deviceIp(self, device_ip):
    #     self.device_ip = device_ip