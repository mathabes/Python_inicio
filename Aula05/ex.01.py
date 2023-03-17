# IMPOSTO DE RENDA
sal = float(input("Qual o seu salário?: R$ "))
if sal <= 1903.98:
    ir = 0
elif sal <= 2826.65:
    ir = (sal * 0.075) - 142.80
elif sal <= 3751.05:
    ir = (sal * 0.15) - 354.80
elif sal <= 4664.68:
    ir = (sal * 0.225) - 636.13
else:
    ir = (sal * 0.275) - 869.36

sal_liq = sal - ir

print(f"""
    Salário.................: R${sal:9.2f}
    Imposto de Renda........: R${ir:9.2f}
    Salário Líquido.........: R${sal_liq:9.2f}
""")
