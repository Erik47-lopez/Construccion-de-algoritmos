__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co"

'''#----------------------------------------------------
# importacones
--------------------------------------------------------#'''
from Fecha import Fecha

class Empleado:
   # Aqui inicia mi clase

   '''#-------------------------------------------------
   # Atributos
   -----------------------------------------------------#'''

   nombre = ''
   apellido = ''
   salario = 0

   '''#-------------------------------------------------
   # 1 Masculino y 2 Femenino 
   -----------------------------------------------------#'''

   sexo = 0 

   '''#--------------------------------------------------
   # Asociaciones
   -----------------------------------------------------#'''

   fechaNacimiento = Fecha()
   fechaIngreso  =  Fecha()
  
   '''#-------------------------------------------------
   # Metodos
   -----------------------------------------------------#'''

   _method_='CambiarSalario'
   _params_='NuevoSalario'
   _returns_='Nada'
   _descriptions_='Este método permite cambiar el salario del empleado por uno nuevo'
   
   def CambiarSalario(self, nuevoSalario):
        # Aqui inicia mi método 
        self.salario = nuevoSalario
   
   _method_='DarSalario'
   _params_='Ninguno'
   _returns_='Salario empleado'
   _descriptions_='Devuelve el salario de un empleado'
   
   def DarSalario(self):
      #aqui inicia el metodo
      return self.salario 
   
   _method_='AumentoSalarial'
   _params_='aumento'
   _returns_='Nimguno'
   _descriptions_='Permite aumentar el salario en un valor ingresado por el usuario'
   
   def AumentoSalarial(self, aumento):
       #aqui inicia mi metodo
       self.salario = self.salario+aumento

   _method_='CalcularSalarioAnual'
   _params_='Ninguno'
   _returns_='Salario anual'
   _descriptions_='permite calcular el salario anual del empleado'
   
   def CalcularSalarioAnual(self):
        return self.salario*12
   
   _method_='CalcularImpuestoSalarioAnual'
   _params_='Ninguno'
   _returns_='Impuesto del salario anual'
   _descriptions_='permite calcular el impuesto a el salario anual del empleado'

   def CalcularSalarioAnual(self):
       #Aqui inicia mi metodo
       salarioAnual = self.CalcularSalarioAnual
       return salarioAnual* 0.19 
   
   
   _method_='CalcularimpuestoSalario'
   _params_='Ninguno'
   _returns_='Impuestop del salario'
   _descriptions_='permite calcular el impuesto del salario  del empleado'
   
   def CalcularImpuestoSalario(self):
        #Aqui inicia mi metodo
        #forma 1
        #return self.salario 0.19
        #forma 2 
        return self.DarSalario()*0.19
   
   
   _method_='DarFechaIngreso'
   _params_='Ninguno'
   _returns_='FechaIngreso'
   _descriptions_='Muestra la fecha de ingreso del empleado'
   
   def DarFechaIngreso(self):
        #Aqui inicia mi metodo
        return self.fechaIngreso.DarFecha()
   

   _method_='DarFechaNacimiento'
   _params_='Ninguno'
   _returns_='FechaNacimiento'
   _descriptions_='Muestra la fecha de nacimiento del empleado'
   
   def DarFechaNacimiento(self):
        #Aqui inicia mi metodo
        return 'Tu fecha de nacimiento es: ' +self.fechaNacimiento.DarFecha()
   
  