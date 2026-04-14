curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

verficacao1 = curso is nome_curso
print(verficacao1)

verficacao2 = curso is not nome_curso
print(verficacao2)

verficacao3 = saldo is limite
print(verficacao3)
