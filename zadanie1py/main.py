def main():
    print("Wybierz opcję:")
    print("1. Kalkulator")
    print("2. Konwersja temperatury")
    print("3. Obliczanie średniej ocen")
    choice = input("> ")
    if choice == "1":
        calculate()
    elif choice == "2":
        convert_temperature()
    elif choice == "3":
        calculate_average_grade()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: Podaj poprawną liczbę.")

def calculate_average_grade():
    while True:
        try:
            num_grades = int(input("Podaj, ile ocen chcesz wprowadzić: "))
            if num_grades > 0:
                break
            print("Błąd: Podaj liczbę większą od zera.")
        except ValueError:
            print("Błąd: Podaj liczbę całkowitą.")
    average = 0
    for i in range(num_grades):
        while True:
            try:
                grade = int(input(f"Podaj ocenę {i + 1} (1-6): "))
                if 1 <= grade <= 6:
                    average += grade
                    break
                print("Błąd: Ocena musi być w zakresie 1-6.")
            except ValueError:
                print("Błąd: Podaj liczbę całkowitą.")
    average /= num_grades
    print(f"Średnia ocen: {average}")
    if average >= 3:
        print("Uczeń zdał")
    else:
        print("Uczeń nie zdał")
        

def convert_temperature():
    unit = input("Wpisz c, jeśli chcesz zamienić stopnie Celsjusza na Fahrenheita lub f, jeśli chcesz zamienić stopnie Fahrenheita na Celsjusza: ")
    temp = get_number("Wpisz temperaturę: ")
    result = None
    if unit == "c":
        result = temp * 1.8 + 32
    elif unit == "f":
        result = (temp - 32) / 1.8
    else:
        print("Nieprawidłowy wybór jednostki. Użyj 'c' lub 'f'.")
        return
    print(f"Wynik: {result}")
        

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
