def main():
    calculate()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: Podaj poprawną liczbę.")

def calculate():
    a = get_number("Wpisz pierwszą liczbę: ")
    b = get_number("Wpisz drugą liczbę: ")

    print("Wybierz operację: +, -, *, /")
    op = input("> ").strip()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Błąd: Nie można dzielić przez zero.")
            return
        result = a / b
    else:
        print(f"Błąd: Nieznana operacja '{op}'. Użyj: +, -, *, /")
        return

    print(f"Wynik: {a} {op} {b} = {result}")


if __name__ == "__main__":
    main()
