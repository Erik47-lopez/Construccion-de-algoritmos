__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co"

class Cuenta_Ahorros:
    # Aqui inicia mi clase

   '''#-------------------------------------------------
   # Atributos
   -----------------------------------------------------#'''

   Interes= 0
   Saldo = 0
   
   '''#--------------------------------------------------
    # Metodos
   ------------------------------------------------------#''' 
   
   __method__='ConsignarValor'
   __params__='Monto'
   __returns__='Ninguno'
   __descriptions__='Este metodo consigna un monto a la cuenta'
   
   def ConsignarValor(self, monto):
       self,__saldo = self,__saldo+monto

   __method__='DarSaldo'
   __params__='Ninguno'
   __returns__='Saldo'
   __descriptions__='Este metodo retorna el saldo'
   
   def DarSaldo(self):
       return self.__saldo       
   
   __method__="RetirarValor"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo retira un monto de la cuenta"   
    
   def RetirarValor(self, monto):
        self._saldo = self._saldo-monto


   __method__="RetirarAhorro"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo retira un monto del ahorro de la cuenta"   
    
   def RetirarAhorro (self, monto):
        self._ahorro = self._ahorro-monto


   __method__="RetirarTodo"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo permite retirar todo el saldo de la cuenta de ahorros"   
    
   def RetirarTodo (self, total):
      self._saldo = self._saldo- total 


   __method__='DuplicarAhorro'
   __params__='Ninguno'
   __returns__='Ninguno'
   __descriptions__='Este metodo duplica el ahorro de la cuenta'
   def DuplicarAhorro(self):
      #Aqui inicia el metodo
      CuentaAhorros = self.DuplicarAhorro()
      return CuentaAhorros*2
