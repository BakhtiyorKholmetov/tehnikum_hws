print("Только не Ноль Плиз")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("x="))
        b = float(input("y="))
        if s == '+':
            print(a+b)
        elif s == '-':
            print(a-b)
        elif s == '*':
            print(a*b)
        elif s == '/':
            if b != 0:
                print(a/b)
            else:
                print("Деление на ноль!"
                      "\nНе надо так!")
    else:
        print("Прошу ввести еще раз!")
