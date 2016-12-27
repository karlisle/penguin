#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################
# Author: @HackerAzteca                #
# Licence: Creative Common             #
# Web: https://github.com/karlisle     #
# Share&Help                           #
########################################
import  sys, time
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


# Importar los modulos locales
import getSerial


class Options(QMainWindow):
    def __init__(self):
        # Inicial el objeto de QMainWindow
        QMainWindow.__init__(self)
        # Cargamos el archivo de interfaz grafica
        uic.loadUi('visor.ui', self)

        # Inicializamos un QTimer
        self.tempo = QTimer(self)
        self.sensor()

        # Instanciar las clases locales
        # Instanciamos la clase de getSerial, con ella obtendremos los datos del sensor

        # Cuando el botón salir sea activado
        self.exit.clicked.connect(self.salir)



        pass
    # Funcion para obtener el valor del sensor
    def sensor(self):
        self.distance.setText("Distancia: No conocida" )
        print("Ok....")
        getVal = getSerial.Distance()
        getVal.getValue()
        return
        pass

    def salir(self):

        self.close()
    pass
    # ------------------------------------------------------------------
    # Fin de la clase
    pass

App = QApplication(sys.argv)
_options = Options()
_options.show()
App.exec()





