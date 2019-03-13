#!/usr/bin/python
from stop_view import Ui_MainWindow as Ui_stop
from ui import Ui_MainWindow as Ui_play
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import sys

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.mode_dic = {'init': 1, 'start':2, 'stop':3, 'alloc':4, 'wait':5}
    self.mode = 1
    self.my_id = '2'
    self.other_id = '3'

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.set_stop_view)

    self.screen = QDesktopWidget().screenGeometry ()
    self.QtStack = QtWidgets.QStackedLayout()
    self.showFullScreen()
    self.Ui_setup()
    self.show()

  def Ui_setup(self):
    try:
      self.mode = self.mode_dic['init']
      self.start_view = Ui_play()
      self.start_view.setupUi(self)
      self.stop_view = Ui_stop()
      self.stop_view.setupUi(self)
      self.stop_view.label.setText("Press 5")
      #self.setCentralWidget(self.stop_view.centralwidget)
      self.start_view.centralwidget.resize(self.screen.width(),self.screen.height())
      self.stop_view.centralwidget.resize(self.screen.width(),self.screen.height())
      self.QtStack.addWidget(self.start_view.centralwidget)
      self.QtStack.addWidget(self.stop_view.centralwidget)
      self.QtStack.setCurrentIndex(1)

    except Exception as e:
       print(e)

  def set_start_view(self):
    self.mode = self.mode_dic['start']
    self.start_view.alloc_1.setText("")
    self.start_view.alloc_3.setText("")
    self.start_view.alloc_2.setText("")
    #self.setCentralWidget(self.start_view.centralwidget)
    self.QtStack.setCurrentIndex(0)

  def set_stop_view(self):
    self.mode = self.mode_dic['stop']
    self.stop_view.label.setText("+")
    self.QtStack.setCurrentIndex(1)
    #self.setCentralWidget(self.stop_view.centralwidget)

  def set_alloc_view(self):
    self.mode = self.mode_dic['alloc']
    self.start_view.alloc_1.setText("5")
    self.start_view.alloc_2.setText("1")
    self.start_view.alloc_3.setText("5")
    #self.setCentralWidget(self.start_view.centralwidget)
    self.QtStack.setCurrentIndex(0)

  def keyPressEvent(self, event):
    key = event.key()
    if key == QtCore.Qt.Key_Escape:
      self.showNormal()
    elif key == QtCore.Qt.Key_5 and self.mode == self.mode_dic['init']:
      self.set_start_view()
      test_src(self)
      self.timer.start(5000)
      self.set_alloc_view()

    elif key == QtCore.Qt.Key_1 and self.mode == self.mode_dic['alloc']:
      my_id = '2'
      other_id = '3'
      self.alloc_src(my_id, other_id, -1)
    elif key == QtCore.Qt.Key_2 and self.mode == self.mode_dic['alloc']:
      my_id = '2'
      other_id = '3'
      self.alloc_src(my_id, other_id, 1)

  def set_id(my_id):
    # my_id : string
    id = [1, 2 ,3]
    my_id = int(my_id) - 1
    self.start_view.pos_2.setText("ID : " + str(id[my_id]))
    self.start_view.pos_3.setText("ID : " + str(id[(my_id+1)%3]))
    self.start_view.pos_1.setText("ID : " + str(id[(my_id+2)%3]))
    QApplication.processEvents()

  def set_src(self, my_id, src_list):
    # my_id : string, src_list : string list
    my_id = int(my_id) - 1
    self.start_view.src_2.setText(src_list[my_id])
    self.start_view.src_3.setText(src_list[(my_id+1)%3])
    self.start_view.src_1.setText(src_list[(my_id+2)%3])
    QApplication.processEvents()

  def alloc_src(self, my_id, other_id, add_minus):
    my_id = int(my_id)
    other_id = int(other_id)
    my_src = int(self.start_view.alloc_3.text())
    self.start_view.alloc_3.setText(str(my_src+add_minus))
    if my_id%3+1 == other_id:
      other_src = int(self.start_view.alloc_2.text())
      self.start_view.alloc_2.setText(str(my_src-add_minus))
    else:
      other_src = int(self.start_view.alloc_1.text())
      self.start_view.alloc_3.setText(str(my_src-add_minus))

    self.setCentralWidget(self.start_view.centralwidget)
    #self.show()


#########

def ui_setup():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  return app, window

def test_src(window):
  src = [
      ["7", "1" ,"4"],
      ["5", "5" ,"1"],
      ["7", "6" ,"4"],
      ["5", "5" ,"1"],
      ["7", "7" ,"4"],
      ["5", "5" ,"1"],
      ["1", "2" ,"3"]
      ]
  for l in src:
    window.set_src(1, l)

def main():
  app, window = ui_setup()
  #window.stop()
  #sys.exit(app.exec_())
  app.exec_()

if __name__ == "__main__":
  main()
