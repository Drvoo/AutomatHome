from PyQt5 import QtWidgets
from view.main_view import Ui_MainWindow
from controllers.main_window_controller import MainWindowController

if __name__ == "__main__":
    import sys
    # create main window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # create main controller

    main_controller = MainWindowController(ui)
    # start main window
    MainWindow.show()
    sys.exit(app.exec_())
