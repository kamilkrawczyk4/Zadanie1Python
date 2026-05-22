def main():
    calculate()

def calculate():
    print("Wpisz pierwszą liczbę: ")
    a = int(input())
    print("Wpisz drugą liczbę: ")
    b = int(input())
    print("Wybierz operację: +, -, *, /")
    op = input()
    result = None
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        print("Nieznana operacja")
        return
    print("Wynik: ", result)


if __name__ == "__main__":
    main()
