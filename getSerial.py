#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################
# Author: @HackerAzteca                #
# Licence: Creative Common             #
# Web: https://github.com/karlisle     #
# Share&Help                           #
########################################

# Libreria serial para escuchar el puerto serial
import getSerial
import serial
import time, io

class Distance():
    # Inicializamos la clase...
    def __index__(self):
        pass

    ''' Esta función escucha las comunicaciones seriales y retorna
    la distancia que esta indicando el censor
    '''
    def getValue(self):

        try:
            # Inicializar puerto serial
            connection = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

            connection.setDTR(False)
            time.sleep(1)
            connection.flushInput()
            connection.setDTR(True)
            pass

        except:
            class FakeArduino(io.RawIOBase):
                def readline(self):
                    time.sleep(0.1)
                    return b'0\r\n'
                    pass
                pass
            connection = FakeArduino()
            pass

        with connection:
            while True:
                try:
                    # En python 3 devuelve un objeto bytes
                    line = connection.readline()
                    # Con errors='replace' se evitan problemas con bytes erroneos
                    # con end='' se evita el doble salto de linea
                    value = (line.decode('ascii', errors='replace')).rstrip('\n')

                    self.normalize(value)
                    pass
                except KeyboardInterrupt:
                    print("Saliendo")
                    exit()
                    pass
            pass
            pass
        pass

    def normalize(self, value):
        print(value)
        pass


    pass