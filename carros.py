print("=== CADASTRO DE CARROS ===")

nome = input("Digite o nome do carro: ")
marca = input("Digite a marca do carro: ")
ano = int(input("Digite o ano do carro: "))

print("\n=== DADOS DO CARRO ===")
print("Nome:", nome)
print("Marca:", marca)
print("Ano:", ano)

if ano >= 2024:
    print("Classificação: Carro novo")
else:
    print("Classificação: Carro usado")