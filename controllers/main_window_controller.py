from models.main_model import MainModel
import time
import threading


class MainWindowController:
    def __init__(self, view):
        self.view = view
        self.model = MainModel(self)
        self.working = True
        worker_thread = threading.Thread(target=MainWindowController.__worker_thread, args=[self])
        worker_thread.start()



    def connect_signals(self):
        pass

    def __worker_thread(self) -> None:
        while False:
            time.sleep(2)
            self.view.rb_attic_door.toggle()
            self.view.rb_celler_door.toggle()
            self.view.rb_large_garage.toggle()


    def __stop_worker_thread(self):
        self.working = False
