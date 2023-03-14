nome = "Matheus"
idade = 17
salario = 1000.5555

#\n serve para descer a linha
print("Nome:", nome, "\nIdade:", idade, "\nSalário:",salario)

#print(f"") serve para colocar quaisquer variáveis (entre chaves) no print
print(f"Nome: {nome} \nIdade: {idade} \nSalário: {salario}")

# :d serve para determinar bits utilizados e .f para casas decimais
print(f"Nome: {nome} \nIdade: {idade:6d} \nSalário: {salario:.2f}")

#número antes do .f também definem bits utilizados
print(f"Salário: {salario:10.3f}")

#outra maneira de usar o print
print(f"""
      Dados:
      Nome: {nome:15}
      Idade: {idade:12}
      Salário: {salario:10.2f}
""")