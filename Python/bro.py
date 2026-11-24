listaDnumeros = []

while True:
    entrada = input("insira um número ou digite 'pare' para parar: ")
    
    if entrada.lower() == "pare":
        print("todos os números estão em ordem crescente!")
        break

    numero = int(entrada)
    if numero <= 0:
        print("Erro")
    elif listaDnumeros and numero <= listaDnumeros[-1]:
        print("A sequência não é crescente!")
        break
    else:
        listaDnumeros.append(numero)
        print(listaDnumeros)

print(f"Quantidade de números: {len(listaDnumeros)}")
print(f"Soma dos números: {sum(listaDnumeros)}")
