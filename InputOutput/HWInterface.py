# imports
import os
import RPi.GPIO as GPIO
import time

print("OS Name: " + os.name)


class HWInterface:

    def __init__(self):
        if os.name is not "posix":
            print("Can't import module RPi.GPIO.\n" +
                  "Is this a Raspberry Pi? If yes, install the module.")
            raise Exception("HWInterface can only run on posix operating system")
        self.GPIOs4BitAddress = [17, 4, 3, 2]
        self.GPIODataInput = 22

        self.dictDeviceStatus = {
            "large_garage": False,
            "celler_door": False,
            "attic_door": False,
            "garden_door": False,
            "garden_door_a": False,
            "garden_door_b": False,
            "light_garage": False,
            "lights_attic": False,
            "motion_detector_1": False,
            "motion_detector_2": False,
            "motion_detector_3": False,
            "small_garage": False
        }

        # GPIO.setmode(GPIO.BOARD) using physical pin numbering e.g. pin 11 for GPIO 17
        # GPIO.setmode(GPIO.BCM) using GPIO numbering scheme eg. "pin 17" for GPIO 17
        print("GPIO: " + str(GPIO.BCM))
        GPIO.setmode(GPIO.BCM)
        # setting up the GPIOs, no need for pull up/downs since only CMOS drivers, inputs are employed
        try:
            for AddessBit in self.GPIOs4BitAddress:
                print("AddressBit: ")
                print("GPIO.OUT: " + str(GPIO.OUT))
                print("GPIO.LOW: " + str(GPIO.LOW))
                GPIO.setup(AddessBit, GPIO.OUT, initial=GPIO.LOW)
        except Exception as e:
            print("Exception during GPIO.setup address")
            raise e
        try:
            GPIO.setup(self.GPIODataInput, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        except Exception as e:
            print("Exception during GPIO.setup data input")
            raise e

    def update_device_status(self):
        for address, Device in enumerate(self.dictDeviceStatus):
            binaddress = [int(x) for x in list('{0:0b}'.format(address+16))][1:]
            for i in range(len(self.GPIOs4BitAddress)):
                GPIO.output(self.GPIOs4BitAddress[i], bool(binaddress[i]))
            time.sleep(0.02)
            self.dictDeviceStatus[Device] = GPIO.input(self.GPIODataInput) == GPIO.HIGH
            time.sleep(0.02)
            print(str(self.dictDeviceStatus[Device]))
            print(GPIO.input(self.GPIODataInput))
            dummy = 1

if __name__ == "__main__":
    hw_interface = HWInterface()
    while True:
        time.sleep(1)
        hw_interface.update_device_status()
    