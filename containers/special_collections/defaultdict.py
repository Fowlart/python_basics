from collections import defaultdict

if __name__ == "__main__":

    # створюємо defaultdict, вказуючи, що значення за замовчуванням мають бути Списками
    cities = defaultdict(list)

    # не потрібно перевіряти, чи існує ключ "Kyiv"! Він створюється автоматично
    cities["Kyiv"].append("Oleg")
    cities["Lviv"].append("Ira")
    cities["Kyiv"].append("Andriy")

    print(cities)

    # поверне порожній list
    print(cities['Odessa'])

    numbers = defaultdict(int)
    numbers['one'] = 1
    numbers['two'] = 2
    numbers['four'] = 4

    # поверне 0
    print(numbers['three'])

    strings = defaultdict(str)
    strings[1] = 'one'
    strings[2] = 'two'
    print(strings[1])
    print(f"[{strings[3]}] \--> of type {type(strings[3])}")

