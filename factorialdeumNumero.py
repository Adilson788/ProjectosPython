def factorial(num):
    print(f'{num}!=', end=" ")
    f = 1
    for c in range (1, num + 1):
        if num > c:
            print(c,'x', end=" ")
        if num == c:
            print(c, '=', end=" ")
        f *= c
    print(f)

valor = int(input('Digite o numero para saber o factorial: '))
factorial(valor)
