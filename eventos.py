print("\nTipo de evento:")
print("1. Palestra")
print("2. Oficina")
print("3. Encontro")
tipo_evento = input("Escolha o tipo (1-3, ou deixe em branco): ")

print("\nPúblico:")
print("1. Pais")
print("2. Educadores")
print("3. Profissionais")
publico = input("Escolha o público (1-3, ou deixe em branco): ")

data = input("\nFiltro por data (DD/MM/AAAA): ")

local = input("\nCidade/Local: ")

print("\n=== FILTROS APLICADOS ===")

print(f"Tipo de evento: {['Palestra', 'Oficina', 'Encontro'][int(tipo_evento)-1] if tipo_evento else 'Qualquer'}")
print(f"Público: {['Pais', 'Educadores', 'Profissionais'][int(publico)-1] if publico else 'Qualquer'}")
print(f"Data: {data if data else 'Qualquer'}")
print(f"Local: {local if local else 'Qualquer'}")
