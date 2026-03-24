class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.__saldo=saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,saldo):
       if saldo >= 0:
           self.__saldo = saldo
       else:
           print("Saldo não pode ser negativo.") 

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # Soma ao saldo atual
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor  # Subtrai do saldo atual
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saque não realizado. Saldo insuficiente ou valor inválido.")

conta = ContaBancaria("Gabriel" ,1000)
conta.depositar(500)
print(f"Saldo atual: R${conta.get_saldo()}")

conta.sacar(200)
print(f"Saldo após saque: R${conta.get_saldo()}")
