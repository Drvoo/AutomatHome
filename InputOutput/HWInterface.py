# imports
import os
import RPi.GPIO as GPIO

print("OS Name: " + os.name)


class HWInterface:

    def __init__(self):
        if os.name is not "posix":
            print("Can't import module RPi.GPIO.\n" +
                  "Is this a Raspberry Pi? If yes, install the module.")
            raise Exception("HWInterface can only run on posix operating system")
        self.GPIOs4BitAddress = [2, 3, 4, 17]
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
            GPIO.setup(self.GPIODataInput, GPIO.IN)
        except Exception as e:
            print("Exception during GPIO.setup data input")
            raise e

    def update_device_status(self):
        for address, Device in enumerate(self.dictDeviceStatus):
            binaddress = [int(x) for x in list('{0:0b}'.format(address+16))][1:]
            for i in range(len(self.GPIOs4BitAddress)):
                GPIO.output(self.GPIOs4BitAddress[i], bool(binaddress[i]))

            self.dictDeviceStatus[Device] = GPIO.input(self.GPIODataInput) == GPIO.HIGH
