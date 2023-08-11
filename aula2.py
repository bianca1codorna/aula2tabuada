while True:
    print("""

Menu
----

1 - Divisão
2 - Multiplicação
3 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 3:
        break
    elif opção >= 1 and opção < 3:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:

            if opção == 1:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif opção == 2:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")
