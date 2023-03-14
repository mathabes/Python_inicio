linha = "="*49
print(f""" 
{linha}
       QUANTO VOCÊ JÁ GASTOU COM CIGARROS?
{linha}
""")
preco = float(input("QUAL O PREÇO DO MAÇO DE CIGARROS?: R$ "))
qnt_dia = int(input("QUANTOS MAÇOS VOCÊ FUMA POR DIA?: "))
tempo = int(input("HÁ QUANTOS ANOS VOCÊ FUMA?: "))
gasto = preco * qnt_dia * tempo*365
print(f"""
{linha}
 VOCÊ JÁ GASTOU R$ {gasto:.2f} COM CIGARROS NA VIDA.
{linha}
""")


