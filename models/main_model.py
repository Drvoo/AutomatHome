import threading
import time
import random
from InputOutput import HWInterface

class MainModel:
    def __init__(self, controller):
        self.controller = controller
        self.worker_thread = None
        self.working = False
        self.dict_rb_buttons = {
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
        self.hw_interface = None
        try:
            self.hw_interface = HWInterface.HWInterface()
        except Exception as e:
            print("Could not instantiate HWInterface: " + str(e))

    def start_work(self):
        self.working = True
        self.worker_thread = threading.Thread(target=self.work)
        self.worker_thread.start()

    def work(self):
        while self.working:
            if self.hw_interface is not None:
                print("checking...")
                self.hw_interface.update_device_status()
                self.dict_rb_buttons = self.hw_interface.dictDeviceStatus
                self.controller.update_signals(self.dict_rb_buttons)
            time.sleep(0.2)
        pass

    def stop_work(self):
        self.working = False
        pass
