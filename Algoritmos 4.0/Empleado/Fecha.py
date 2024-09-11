__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co"

class Fecha:
    # Aqui inicia mi clase

   '''#-------------------------------------------------
   # Atributos
   -----------------------------------------------------#'''

   dia = 0
   mes = 0
   anio = 0

   '''#--------------------------------------------------
   # Metodos
   ------------------------------------------------------#''' 
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
       return self. dia+'/'+self. mes+'/'+self.anio
   
   _method_='DarDia'
   _params_='Ninguno'
   _returns_='Dia de la clase'
   _descriptions_='Devuelve el dia de la clase'
   
   def DarDia(self):
       return self.dia
   

   _method_='DarMes'
   _params_='Ninguno'
   _returns_='Mes de la clase'
   _descriptions_='Devuelve el mes de la clase'
   
   def DarMes(self):
       return self.mes
   

   _method_='DarAnio'
   _params_='Ninguno'
   _returns_='Año de la clase'
   _descriptions_='Devuelve el año de la clase'
   
   def DarAño(self):
       return self.anio
   
       