# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollBar

from .main_ui import Ui_JsonDiff


class Main(QtWidgets.QMainWindow, Ui_JsonDiff):
    def __init__(self, app):
        super(Main, self).__init__()
        self.app = app
        self.setupUi(self)
        self.setWindowTitle("JsonDiff")
        self._init_set()
        self._init_connect()

    def _init_set(self):
        self.scroll_bar_left = QScrollBar()
        self.scroll_bar_right = QScrollBar()
        self.text_edit_left.setVerticalScrollBar(self.scroll_bar_left)
        self.text_edit_right.setVerticalScrollBar(self.scroll_bar_right)

    def _init_connect(self):
        self.file_button_left.clicked.connect(lambda _: self.open_file_dialog(self.path_edit_left, self.text_edit_left))
        self.file_button_right.clicked.connect(lambda _: self.open_file_dialog(self.path_edit_right, self.text_edit_right))

        # scrollbar sync
        self.scroll_bar_left.valueChanged.connect(lambda _: self._set_scroll_value(self.scroll_bar_right, self.scroll_bar_left.value()))
        self.scroll_bar_right.valueChanged.connect(lambda _: self._set_scroll_value(self.scroll_bar_left, self.scroll_bar_right.value()))

    @staticmethod
    def _set_scroll_value(scroll_bar, value):
        scroll_bar.setValue(value)

    def open_file_dialog(self, path_edit, text_edit):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'select json', filter="json (*.json)")
        path_edit.setText(filename)
        with open(filename) as file:
            text_edit.setPlainText(file.read())


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = Main(app)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()