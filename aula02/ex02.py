linha = "="*40
print(linha)
valor = int(input("QUAL O VALOR QUE DESEJA SACAR?: R$ "))
print(linha)

cd50 = valor // 50
r50 = int(valor % 50)
cd20 = r50 // 20
r20 = int(r50 % 20)
cd10 = r20 // 10

print(f"""
{linha}
||  FORAM RECEBIDAS:          ||
|| {cd50:3d} cédulas de 50 reais.   ||
|| {cd20:3d} cédulas de 20 reais.   ||
|| {cd10:3d} cédulas de 10 reais.   ||
{linha}
""")