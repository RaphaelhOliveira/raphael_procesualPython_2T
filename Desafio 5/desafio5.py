print ("Adicione 10 nomes aqui:")
nome1 = input("Acicone o 1º nome:")
nome2 = input("Acicone o 2º nome:")
nome3 = input("Acicone o 3º nome:")
nome4 = input("Acicone o 4º nome:")
nome5 = input("Acicone o 5º nome:")
nome6 = input("Acicone o 6º nome:")
nome7 = input("Acicone o 7º nome:")
nome8 = input("Acicone o 8º nome:")
nome9 = input("Acicone o 9º nome:")
nome10 = input("Acicone o 10º nome:")

lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8, nome9, nome10]

for nome in lista:
    if not nome.isalpha():
        print(f"Erro: '{nome} 'Apenas letras podem ser adicionadas")
        exit()
        
lista.sort()

print("\nLista em ordem alfabética:")
for nome in lista:
    print(f"{nome}-{len(nome)} letras")
        
