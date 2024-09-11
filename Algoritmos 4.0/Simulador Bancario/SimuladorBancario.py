__author__ = "Erik Santiago Lopez Erazo"
__license__ = "GPL"
__version__ = "1.0.0"
__email____ = "erik.lopez@campusucc.edu.co" 

'''#----------------------------------------------------
# importacones
--------------------------------------------------------#'''
from Cuenta_Ahorros import Cuenta_Ahorros
from Cuenta_Corriente import Cuenta_Corriente
from CDT import CDT

class SimuladorBancario:
  
   '''#-------------------------------------------------
   # Atributos
   -----------------------------------------------------#'''

   __cedula = ''
   __nombre = ''
   
   __CuentaCorriente__ = Cuenta_Corriente()
   __CuentaAhorros__  =  Cuenta_Ahorros()
   __CDT__  =  CDT()

   __mesActual = 0 

   '''#-------------------------------------------------
   # Metodos
   -----------------------------------------------------#'''

   __method__='ConsignarCuentaCorriente'
   __params__='Monto'
   __returns__='Nada'
   __descriptions__='Este metodo consigna un monto a la cuenta corriente'
   
   def ConsignarCuentaCorriente(self, monto):
       #aqui inicia mi metodo
       #self.__CuentaCorriente.__Saldo = self__cuentaCorriente.saldo+monto #modo no recomendado
       self.__CuentaCorriente__. Consignarvalor(monto)

   __method__='CalcularSaldoTotal'
   __params__='ninguno'
   __returns__='Saldo total'
   __descriptions__='Este metodo suma el saldo de todas las cuentas'
   
   def CalcularSaldoTotal(self):
       #aqui inicia mi metodo
       #forma 1 
       total= self. __CuentaCorriente__. DarSaldo()+self.__CuentaAhorros__. DarSaldo()
       return total


   __method__='PasarAhorrosACorriente'
   __params__='ninguno'
   __returns__='ninguno'
   __descriptions__='Este metodo transfiere el saldo de ahorros a corriente'
   
   def PasarAhorrosACorriente(self):
       saldoTemporal = self.__CuentaAhorros__. DarSaldo()
       self.__CuentaAhorros__. RetirarValor(saldoTemporal)
       self.__CuentaCorriente__. ConsignarValor(saldoTemporal)


   __method__='Ahorrar'
   __params__='monto'
   __returns__='ninguno'
   __descriptions__='Este metodo permite pasar un monto de la cuenta corriente a la cuenta de ahorros'
   
   def Ahorrar(self,monto):
       self.__CuentaCorriente__. RetirarValor(monto)
       self.__CuentaAhorros__. ConsignarValor(monto)

   __method__="RetirarAhorro"
   __params__="Monto"
   __returns__="Nada"
   __descriptions__="Este metodo retira un monto dado de la cuenta de ahorros"   
    
   def RetirarAhorro (self, monto):
        self.__CuentaAhorros__.RetirarValor(monto)

   _method__="DarSaldoCorriente"
   __params__="Ninguno"
   __returns__="Saldo"
   __descriptions__="Este metodo retorna el saldo que hay en la cuenta corriente"   
    
   def DarSaldoCorriente (self):
        return self.__saldo
   

   __method__="RetirarTodo"
   __params__="Monto"
   __returns__="cantidad retirda"
   __descriptions__="Retira todo el dinero de la cuenta corriente"   
    
   def RetirarTodo (self, ):
        total = self. __CuentaCorriente__.DarSaldo() + self. __CuentaAhorros__. DarSaldo()
        self.__CuentaAhorros__. RetirarValor(self.__CuentaAhorros__.DarSaldo())
        self.__CuentaCorriente__.RetirarValor(self.__CuentaCorriente__.DarSaldo())
        return 'Usted acaba de retirar '+total
   

   __method__='DuplicarAhorro'
   __params__='Ninguno'
   __returns__='Ninguno'
   __descriptions__='Duplica la cantidad de dinero que hay en la cuenta e ahorros'
   
   def DuplicarAhorro(self):
       self. __CuentaAhorros__.ConsignarValor(self.__CuentaAhorros__.DarSaldo())
       