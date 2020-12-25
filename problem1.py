a = float(input('Введите число а '))

b = float(input('Введите число b '))

c = float(input('Введите число c '))

if a > b and a < c:

    print('a больше b и a меньше c')

else:

    if a < b and a > c:

        print('a меньше b и a больше c')

    else:

            if b > a and b < c:

                print('b больше a и меньше c')

            else:

                    if b < a and b > c:

                        print('b меньше a и больше c')

                    else:

                            print('c лежит посередине')
