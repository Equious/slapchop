from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QStatusBar,
)

from slapchop import Widget


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app  # declare an app member
        central_widget = Widget()
        self.setWindowTitle("Slapchop")
        self.setCentralWidget(central_widget)

        # menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)

        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addAction("Window")
        menu_bar.addAction("Settings")
        menu_bar.addAction("Help")

        # Toolbars

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Adding actions to the toolbar

        toolbar.addAction(quit_action)

        toolbar.addSeparator()

        action1 = QAction("Hate Everything", self)
        action1.setStatusTip("Click to Hate Everything")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        toolbar.addSeparator()

        toolbar.addAction(save_action)

        toolbar.addSeparator()

        toolbar.addSeparator()

        # Set up Status Bar
        statusbar = self.setStatusBar(QStatusBar(self))

    # Functions
    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Custom Message", 3000)

    def dickbutt_mode_toggle(self, checked):
        if checked:
            self.setCentralWidget(self.buttonWidget)
        else:
            self.setCentralWidget(self.fileWidget)
