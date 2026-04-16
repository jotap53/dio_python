def sacar(valor: float):
    saldo = 500
    
    if saldo > valor:
        print('Valor sacado.')
        print('Retire seu dinheiro no caixa.')
        
    print('Obrigado por ser nosso cliente!')
    
def depositar(valor):
    saldo = 500
    saldo += valor
        
sacar(1000)