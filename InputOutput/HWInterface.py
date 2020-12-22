# imports
import os

if os.name == "posix":
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
        GPIO.setmode(GPIO.BCM)
        # setting up the GPIOs, no need for pull up/downs since only CMOS drivers, inputs are employed
        for AddessBit in self.GPIOs4BitAddress:
            GPIO.setup(AddessBit, GPIO.OUT, pull_up_down=None, initial=GPIO.LOW)

        GPIO.setup(self.GPIODataInput, GPIO.IN, pull_up_down=None)

    def update_device_status(self):
        address = 0
        for Device in self.dictDeviceStatus:
            binaddress = [int(x) for x in list('{0:0b}'.format(address))]
            for i in range(0, len(self.GPIOs4BitAddress)):
                GPIO.output(self.GPIOs4BitAddress[i], bool(binaddress[i]))

            if GPIO.input(self.GPIODataInput) == GPIO.HIGH:
                self.dictDeviceStatus[Device] = True
            else:
                self.dictDeviceStatus[Device] = False

            address += 1
