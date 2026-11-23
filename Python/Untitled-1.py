numero1 = int(input("Diga um número: "))
numero2 = int(input("Diga um segundo número: "))
numero3 = int(input("Diga um terceiro número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

if numero1 > numero3:
    numero1, numero3 = numero3, numero1

if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Menor:", numero1)
print("Meio:", numero2)
print("Maior:", numero3)