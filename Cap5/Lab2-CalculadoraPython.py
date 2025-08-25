# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capitulos até aqui no curso.

print("\n**************** Calculadora em Python ****************")

calc = int(input("\n Selecione o número da operação desejada:\n" \
"1 - Soma\n" \
"2 - Subtração\n" \
"3 - Multiplicação\n" \
"4 - Divisão\n" \
"\n" \
"Digite sua opção (1/2/3/4): "))

def numFloat():
    num1 = float(input("Digite 1º Numero: "))
    num2 = float(input("Digite 2º Numero: "))
    return num1, num2

def numSoma():
    n1, n2 = numFloat()
    print(f"A soma dos dois numeros é: {n1 + n2}")

def numSubt():
    n1, n2 = numFloat()
    print(f"A Subtração dos dois numeros é: {n1 - n2}")

def numMult():
    n1, n2 = numFloat()
    print(f"A Multiplicação dos dois numeros é: {n1 * n2}")

def numDivi():
    n1, n2 = numFloat()
    print(f"A Divisão dos dois numeros é: {n1 / n2}")

def calculator(calc):
    if calc == 1:
        numSoma()
    if calc == 2:
        numSubt()
    if calc == 3:
        numMult()
    if calc == 4:
        numDivi()

calculator(calc)