from pywinusb import hid
import pyautogui
"""
Devices section, everything related to joysticks
"""

class Dispositives:
    def __init__(self):
        pass
    
    def list_dispositives(self):
        "Retrieves the names of the devices in the list"
        names_dispositives = []
        dispositives = hid.HidDeviceFilter().get_devices()
        for joystick in dispositives:
            names_dispositives.append(joystick.product_name)
        return names_dispositives
    
    def connect_dispositive(self,dispositive_name):
        "Connect the selected device"
        dispositives = hid.HidDeviceFilter().get_devices()
        for joystick in dispositives:
            if joystick.product_name == dispositive_name:
                joystick.open()
                joystick.set_raw_data_handler()
                return True
            return False
