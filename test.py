#!/usr/bin/python
from ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys
import time

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    QtWidgets.QFrame.__init__(self, parent)
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    self.setupUi(self)
    self.showFullScreen()

  def keyPressEvent(self, event):
    key = event.key()
    if key == QtCore.Qt.Key_Escape:
      self.showNormal()

def ui_setup():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.src_1.setText("2")
  window.show()
  return app, window

def set_id(app, window, my_id):
  # my_id : string
  id = [1, 2 ,3]
  my_id = int(my_id) - 1
  window.pos_2.setText("ID : " + str(id[my_id]))
  window.pos_3.setText("ID : " + str(id[(my_id+1)%3]))
  window.pos_1.setText("ID : " + str(id[(my_id+2)%3]))
  QApplication.processEvents()

def set_src(app, window, my_id, src_list):
  # my_id : string, src_list : string list
  my_id = int(my_id) - 1
  window.src_2.setText(src_list[my_id])
  window.src_3.setText(src_list[(my_id+1)%3])
  window.src_1.setText(src_list[(my_id+2)%3])
  QApplication.processEvents()

def main():
  app, window = ui_setup()
  src = [
      ["7", "5" ,"4"],
      ["5", "5" ,"1"],
      ["1", "2" ,"3"]
      ]
  for l in src:
    set_src(app, window, 1, l)
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
