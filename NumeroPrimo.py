num = int(input("digite numero: "))
cont = 0
print(f'O numero {num} é divisivel por:', end=" ")
for c in range(1, num + 1):
    if num % c ==0:
        print(c, end=" ")
        cont += 1
print()
if cont == 2:
    print(f"Portanto, \033[32m numero {num} é Primo\033[m, porque foi divisivel {cont} vezes, por 1 e ele mesmo.")
else:
    print(f"O numero {num} Não é Primo, porque foi divisivel {cont} vez(es).")
