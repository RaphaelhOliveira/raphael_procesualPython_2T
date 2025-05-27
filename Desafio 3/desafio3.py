nomes = ["Arthur", "Beatriz", "Caio", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Júlia",
"Kauã", "Larissa", "Miguel", "Natália", "Otávio", "Olivia", "Pedro", "Patrícia", "Rafael", "Rafaela",
"Samuel", "Sabrina", "Thiago", "Tainá", "Victor", "Úrsula", "William", "Valentina", "André", "Yasmin",
"Bruno", "Zuleika", "Diego", "Clara", "Enzo", "Cecília", "Guilherme", "Elisa", "Heitor", "Lívia",
"Isaac", "Mariana", "Jorge", "Sofia", "Lucas", "Ana", "Benjamin", "Camila", "Daniel", "Eduarda",
"Felipe", "Gabriela", "Henrique", "Isabela", "João", "Karina", "Leonardo", "Luana", "Nicolas", "Maria",
"Alex", "Ariel", "Charlie", "Dani", "Dominique", "Emerson", "Francis", "Gabi", "Harley", "Indigo",
"Jaime", "Kai", "Logan", "Morgan", "Noel", "Orion", "Phoenix", "Quinn", "Riley", "Sam",
"Taylor", "Zion", "Avery", "Blair", "Casey", "Devon", "Eden", "Finley", "Gray", "Hunter",
"Jordan", "Kendall", "Leslie", "Milan", "Nico", "Ocean", "Robin", "Sky", "Terry", "Winter"]
contador = 0

for nomes in nomes:
    if nomes == "Úrsula":
        print("Bônus")
    contador+= 1
    teste = contador % 15
    if teste == 0:
        print("teste")
    if contador == 85:
        print("Fim")
        break
    print(nomes)
