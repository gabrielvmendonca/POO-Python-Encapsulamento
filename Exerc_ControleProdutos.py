class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.__preco = float(preco)

    @property
    def preco(self):
        return self.__preco 
    
    @preco.setter
    def preco(self,valor):
        if valor > 0:
            self.__preco = float(valor)
        else:
            print("Precisa de um Preço.")

    def aplicar_desconto(self,percentual):
        if percentual > 0:
           self.__preco -= (self.__preco * (percentual / 100))
           print(f"Desconto de {percentual}% aplicado com sucesso.")
        else:
            print("Percentual inválido para desconto.")

    def aumentar_preco(self,percentual):
       if percentual > 0:
            self.__preco += (self.__preco * (percentual / 100))
            print(f"Aumento de {percentual}% aplicado com sucesso.")
       else:
            print(f"Preço mantido em: R$ {self.preco:.2f}")

goiabinha = Produto("Goiabinha", 3.50)

goiabinha.aplicar_desconto(10)
print(f"Preço após desconto: R$ {goiabinha.preco:.2f}")

goiabinha.aumentar_preco(15)
print(f"Preço após aumento: R$ {goiabinha.preco:.2f}")