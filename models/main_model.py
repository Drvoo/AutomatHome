import threading
import time
import random

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

    def start_work(self):
        self.working = True
        self.worker_thread = threading.Thread(target=self.work)
        self.worker_thread.start()

    def work(self):
        while self.working:
            for name, status in self.dict_rb_buttons.items():
                # TODO: Check signals of raspbarrypi
                self.dict_rb_buttons[name] = bool(random.randrange(0, 2))
            self.controller.update_signals(self.dict_rb_buttons)
            time.sleep(2)
        pass

    def stop_work(self):
        self.working = False
        pass
