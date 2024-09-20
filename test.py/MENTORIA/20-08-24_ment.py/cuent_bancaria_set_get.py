class CtaBancaria():
    def __init__(self, titular, numero_cuenta, saldo):
self.titular = titular
self.__numero_cuenta = numero_cuenta
self.__saldoCta = saldo

def ingresar_dinero(self, monto):
self.__saldoCta = self.__saldoCta + monto

# setter
def retirar_dinero(self, monto):
if (monto > self.__saldoCta):
print("El monto a retirar supera al saldo de la cuenta")
return False
self.__saldoCta = self.__saldoCta - monto
return True

# getter
def ver_saldo(self, numero_cta):
if (numero_cta == self.__numero_cuenta):
return self.__saldoCta
else:
return "No es su cuenta."


cuenta1 = CtaBancaria("Rafael", 5555, 200000)
print(cuenta1.ver_saldo(5555))

cuenta1.__saldoCta = -50000
print(cuenta1.ver_saldo(5554))

na
Nancy Debárbora
15:58
gracias!

Enviar mensaje a Chat público

#

class CtaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldoCta = saldo

    def ingresar_dinero(self, monto):
        self.__saldoCta += monto

    def retirar_dinero(self, monto):
        if monto > self.__saldoCta:
            print("El monto a retirar supera al saldo de la cuenta")
            return False
        self.__saldoCta -= monto
        return True

    def ver_saldo(self, numero_cta):
        if numero_cta == self.__numero_cuenta:
            return self.__saldoCta
        else:
            return "No es su cuenta."

# Ejemplo de uso
cuenta1 = CtaBancaria("Rafael", 5555, 200000)
print(cuenta1.ver_saldo(5555))  # Debería imprimir 200000

# Intento de modificar el saldo directamente (no debería permitirse)
cuenta1.__saldoCta = -50000
print(cuenta1.ver_saldo(5554))  # Debería imprimir "No es su cuenta."
