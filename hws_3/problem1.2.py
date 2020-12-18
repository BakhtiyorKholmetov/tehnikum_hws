m = []
print("Только не Ноль Плиз")
while True:
    s = int(input("Введите число n = "))
    m.append(s)
    if s == 0:
        break

print(sum(m))
