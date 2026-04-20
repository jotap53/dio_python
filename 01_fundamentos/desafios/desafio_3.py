'''
Descrição
Neste desafio, implemente uma solução para completar a função conta_vogais que conta o número de vogais em uma string fornecida como entrada. Vogais são caracteres específicos sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas (aeiouAEIOU).

Para resolver este desafio, siga os passos abaixo:
    1. DEFINA UM CONJUNTO DE VOGAIS: Primeiramente, crie um conjunto contendo todas as vogais sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas.
    2. INICIALIZE UM CONTADOR: Em seguida, crie uma variável para contar o número de vogais encontradas na string, começando com zero.
    3. ITERE PELOS CARACTERES DA STRING: Aqui percorremos cada caractere na string de entrada para verificar se é uma vogal.
    4. VERIFIFIQUE SE O CARACTERE É UMA VOGAL: Para cada caractere, verifique se ele está presente no conjunto de vogais definido no passo 1. Se o caractere for uma vogal, incremente o contador em 1.
    5. RETORNE UM CONTADOR: Após percorrer todos os caracteres da string, retorne o valor do contador, que representa o número total de vogais na string.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements

Entrada
A função recebe como entrada uma única string contendo letras/palavras.

Saída
A função deve retornar um número inteiro que representa o total de vogais encontradas na string de entrada.
 
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada         |   Saída
Python          |   O número de vogais na string 'Python' é: 1
Programação     |   O número de vogais na string 'Programação' é: 4
Função          |   O número de vogais na string 'Função' é: 2

ATENÇÃO
As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.
'''

def conta_vogais(texto):

    texto = texto.lower()
    vogais = "aeiou"
    resultado = 0

    for letra in texto:
        if letra in vogais:
            resultado += 1

    return resultado

texto = input()

resultado = conta_vogais(texto)

print(f"O número de vogais na string '{texto}' é: {resultado}")
