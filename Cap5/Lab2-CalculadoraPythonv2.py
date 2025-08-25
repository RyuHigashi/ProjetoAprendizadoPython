from typing import Callable, Tuple

def ler_float(msg: str) -> float:

    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Entrada Invalida.")


def lerNums() -> Tuple[float, float]:
    a = ler_float("Digite o 1º Numero: ")
    b = ler_float("Digite o 2º Numero: ")

    return a, b

def soma(a: float, b: float ) -> float:
    return a+b

def subt(a: float, b: float ) -> float:
    return a-b

def mult(a: float, b: float ) -> float:
    return a*b

def div(a: float, b: float ) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero!")
    return a/b

OPERACOES: dict[str, tuple[str, Callable[[float, float], float]]] = {
    "1": ("Soma", soma),
    "2": ("Subtração", subt),
    "3": ("Multiplicação", mult),
    "4": ("Divisão", div),
}

MENU = """
************************ Calculadora em Python ************************


Selecione o numero da operação desejada:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair
""" 




def main() -> None:
    print(MENU)
    while True:
        opc = input("Digite sua opção (0/1/2/3/4): ").strip()


        if opc == "0":
            print("Encerrando até mais!")
            break

        if opc not in OPERACOES:
            print("Opção invalida")


        nome, func = OPERACOES[opc]

        a, b = lerNums()


        try:
            resultado = func(a,b)
            print(f"{nome}: {a} e {b} -> Resultado = {resultado}")
        except ZeroDivisionError as e:
            print(f"Erro {e}")


        cont = input("Deseja realizar outra operação (s/n): ").strip().lower()

        if cont != "s":
            print("Encerrando. Até mais!")
            break


        print()
        print (MENU)

if __name__ == "__main__":
    main()