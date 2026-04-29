class Bicileta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Trim trim ...")
    
    def parar(self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vruuummm ...")
    
    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
    
    # Com esse código abaixo, tudo o que for instanciado na classe aparecerá quando ele for chamado. Diferente do código acima, que teríamos que adicionar na mão qualquer instância nova adicionada.
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicileta("vermelha", "caloi", 2022, 600)

b1 = Bicileta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicileta("Verde", "Monark", 2000, 189)
Bicileta.buzinar(b2)
