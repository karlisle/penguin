#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################
# Author: @HackerAzteca                #
# Licence: Creative Common             #
# Web: https://github.com/karlisle     #
# Share&Help                           #
########################################
import  sys
import  serial
import time
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton



class Options(QMainWindow):
    def __init__(self):
        # Inicial el objeto de QMainWindow
        QMainWindow.__init__(self)
        # Cargamos el archivo de interfaz grafica
        uic.loadUi('visor.ui', self)

        self.exit.clicked.connect(self.salir)
        pass


    def salir(self):
        self.close()
    pass

App = QApplication(sys.argv)
_options = Options()
_options.show()
App.exec()





