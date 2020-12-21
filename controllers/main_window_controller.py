from models.main_model import MainModel
import view.main_view
import time
import threading

class MainWindowController:
    def __init__(self, view: view.main_view.Ui_MainWindow):
        self.view = view
        self.model = MainModel(self)
        self.working = True
        self.dict_rb_buttons = {
            "large_garage": self.view.rb_large_garage,
            "celler_door": self.view.rb_celler_door,
            "attic_door": self.view.rb_attic_door,
            "garden_door": self.view.rb_garden_door,
            "garden_door_a": self.view.rb_garden_door_a,
            "garden_door_b": self.view.rb_garden_door_b,
            "light_garage": self.view.rb_light_garage,
            "lights_attic": self.view.rb_lights_attic,
            "motion_detector_1": self.view.rb_motion_detector_1,
            "motion_detector_2": self.view.rb_motion_detector_2,
            "motion_detector_3": self.view.rb_motion_detector_3,
            "small_garage": self.view.rb_small_garage
        }
        self.model.start_work()

    def connect_signals(self):
        pass

    # view to model

    # model to view
    def update_signals(self, status_rb_buttons: dict):
        for name, status in status_rb_buttons.items():
            time.sleep(0.05)
            self.dict_rb_buttons[name].setChecked(status)
        pass

