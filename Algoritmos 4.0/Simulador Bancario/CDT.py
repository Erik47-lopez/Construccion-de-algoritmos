__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co"

class CDT:
    # Aqui inicia mi clase

   '''#-------------------------------------------------
   # Atributos
   -----------------------------------------------------#'''

   Interes= 0
   Inversion = 0
   Fecha = 0
   
   '''#--------------------------------------------------
    # Metodos
   ------------------------------------------------------#''' 
   
   _method_='CambiarInteres'
   _params_='nuevoInteres'
   _returns_='Nada'
   _descriptions_='Este metodo cambia el valor del interes'
   
   def CambiarIntereses(self, nuevoInteres):
       #aqui inicia mi metodo
       self.Interes = self, nuevoInteres


   _method_='DarInteres'
   _params_='Ninguno'
   _returns_='Nuevo interes'
   _descriptions_='permite ver el interes de la cuenta de ahorros del usuario'


   def CambiarInteres(self):
       #aqui inicia mi metodo
       return self.Interes 
   
   
   _method_='CambiarFecha'
   _params_='nuevaFecha'
   _returns_='Ninguno'
   _descriptions_='Este método permite cambiar la fecha por una nueva'
   
  
   def CambiarFecha(self, nuevaFecha):
       #aqui empieza mi metodo
       self.fecha = nuevaFecha 

   _method_='DarFecha'
   _params_='Ninguno'
   _returns_='Fecha Actual'
   _descriptions_='Dar la fecha cambiada'
   
   
   def DarFecha(self):
       # Aqui inicia mi método
       return self. fecha 
