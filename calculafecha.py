# -*- coding: utf-8 -*- 
import sys
import time
import datetime
from PyQt4 import QtGui, QtCore

#usamos strftime para obtener dia, mes y anio, luego declaramos variables con cada dato recibido
fecha=(str(time.strftime("%d/%m/%Y"))).split('/')

dia=int(fecha[0])
mes=int(fecha[1])
anio=int(fecha[2])


class Mexico(QtGui.QWidget):
    
    def __init__(self):
        super(Mexico, self).__init__()
        
        self.btn= QtGui.QPushButton("Aprietame", self)        
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.calcula)
        self.btn.move(150, 100)            

        label= QtGui.QLabel(self)
        label.setText("Miguel Hidalgo y Costilla, José María Morelos y Pavón, Vicente Guerrero")
        label.move(20,10)
        
        self.setGeometry(500, 200, 400, 300)
        self.setWindowTitle("¡Viva México!")            
        self.show()

	#calcula el numero de dias para el 1 de septiembre del anio siguiente
    def calcula(self):
        if int(dia) <=15 and int(mes)<=9: #si aun no es 15 de septiembre en el anio actual
            faltan= datetime.date(anio, 9,15)- datetime.date.today()#usamos el date time en una resta, el dia de la independencia con el actual
            
            self.btn.setText("Faltan "+str(faltan.days)+" días para el 15 de septiembre del "+str(anio)+".")#usamos .days para obtener solo el dia
            self.btn.resize(self.btn.sizeHint())
            self.btn.move(90, 100)
            
        else:#si ya paso este anio
        	faltan= datetime.date(anio+1, 9,15) - datetime.date.today()
        	
        	self.btn.setText("Faltan "+str(faltan.days)+" días para el 15 de septiembre del "+str(anio+1)+".")#en el caso de que sea el proximo anio
        	self.btn.resize(self.btn.sizeHint())
        	self.btn.move(90, 100)
        	
        		

def main():    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("bandera.jpg")) #agregando el icono
    mx = Mexico()
    sys.exit(app.exec_()) #Para salir dentro de la aplicacion



if __name__ == '__main__':
    main()


