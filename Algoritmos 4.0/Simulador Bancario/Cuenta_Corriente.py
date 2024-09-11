__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co"

class Cuenta_Corriente:
    # Aqui inicia mi clase

   '''#-------------------------------------------------
   # Atributo
   -----------------------------------------------------#'''

   __saldo= 0
   
   '''#--------------------------------------------------
    # Metodos
   ------------------------------------------------------#''' 
   
   _method_='ConsignarValor'
   _params_='Monto'
   _returns_='Ninguno'
   _descriptions_='Este metodo consigna un monto a la cuenta'
   
   def ConsignarValor(self, monto):
       self,__saldo = self,__saldo+monto

   _method_='DarSaldo'
   _params_='Ninguno'
   _returns_='Saldo'
   _descriptions_='Este metodo retorna el saldo'
   
   def DarSaldo(self):
       return self.__saldo
   
    
   __method__="RetirarValor"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo retira un monto de la cuenta"   
    
   def RetirarValor (self, monto):
        self._saldo = self._saldo-monto

   __method__="Ahorrar"
   __params__="Monto"
   __returns__="Ninguno"
   __descriptions__="Este metodo permite pasar el ahorro de la cuenta corriente a la cuenta de ahorros"  

   def Ahorrar(self, monto):
        saldoTemporal = self.__cuentaAhorros.DarAhorro()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.consignarValor(saldoTemporal)

   __method__="DarSaldoCorriente"
   __params__="Ninguno"
   __returns__="Saldo"
   __descriptions__="Este metodo retorna el saldo que hay en la cuenta corriente"   
    
   def DarSaldoCorriente (self):
        return self.__saldo

   __method__="RetirarTodo"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo permite retirar todo el saldo de la cuenta corriente"   
    
   def RetirarTodo (self, total):
        self._saldo = self._saldo- total

