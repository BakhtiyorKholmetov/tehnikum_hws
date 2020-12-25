a = int(input('Введите число а '))

b = int(input('Введите число b '))

c = int(input('Введите число c '))

if a > b:

    m = a

    if a > c:

        print(m)

    else:

        m = c

        if c > b:

            print(m)

        else:

            m = b

            print(m)

else:

    m = b

    if b > c:

        print(m)

    else:

        m = c

        print(m)
