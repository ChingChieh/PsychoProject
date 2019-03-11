#!/usr/bin/python
from stop_point import Ui_MainWindow as Ui_stop
from ui import Ui_MainWindow as Ui_play
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import time
import sys

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    #QtWidgets.QFrame.__init__(self, parent)
    #screen = QtWidgets.QDesktopWidget().screenGeometry()
    #self.setupUi(self)
    self.showFullScreen()
    self.dialogs = list()

  def stop(self):
    dialog = Ui_stop()
    dialog.setupUi(self)
    self.dialogs.append(dialog)
    self.show()

  def keyPressEvent(self, event):
    key = event.key()
    if key == QtCore.Qt.Key_Escape:
      self.showNormal()

def ui_setup():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  view = Ui_play()
  view.setupUi(window)
  view.src_1.setText("2")
  return app, window, view

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
  app, window, view = ui_setup()
  src = [
      ["7", "5" ,"4"],
      ["5", "5" ,"1"],
      ["7", "5" ,"4"],
      ["5", "5" ,"1"],
      ["7", "5" ,"4"],
      ["5", "5" ,"1"],
      ["1", "2" ,"3"]
      ]
  for l in src:
    time.sleep(1)
    set_src(app, view, 1, l)
  window.stop()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
