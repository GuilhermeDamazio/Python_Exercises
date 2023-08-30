print("Contando os números ímpares de 0 a 100: ")
for numero in range(100):
   
    if numero % 2 == 0:
        continue
    print(numero, end=" ")


print("\nContando os números pares de 0 a 100: ")
for numero in range(100):
    if numero % 2 == 1:
        continue
    print(numero, end= " ")
