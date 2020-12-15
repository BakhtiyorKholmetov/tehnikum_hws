names = []
numbs = []
ages = []
new_name = input('Введите свое имя ').upper()
names.append(new_name)
print(new_name + ' вас приветствует аля Makhmood oka :)!')
age = int(input('Пожалуста введите год рождения '))
age = 2020 - age
ages.append(age)
print('Вы знаете что такое программирование?')
ans1 = input('Y или N ')
while ans1 == 'n' or ans1 == 'N':
    print('Вы знаете что такое программирование?')
    ans1 = input('Y или N ')
print('Я предполлагаю что вы уже знаете про языке программирования.')
print('Вы слышали про Tehnikium.'
      '\nTehnikum - школа актуалных профессий в Узбекистане')
ans2 = input('Y или N ')
if ans2 == 'y' or ans2 == 'Y':
    print('Тогда я предлагаю вам оставить свой номер телефона для обратной связи')
    print('Прошу ввести номер в формате +998-33-333-33-33')
    numb = input()
    print('Для обработки ваших данных мне нужно ваше согласие')
    ans = input('Y или N ')
    while ans == 'n' or ans == 'N':
        print('Без вашего согласия '
              '\nМы не сможем с вами связаться')
        ans = input('Y или N ')
numbs.append(numb)
print('Прошу подтвердить ваши данные')
print('Имя', names[0])
print('Номер', numbs[0])
print('возраст', ages[0] + 'лет')
ans3 = input('Y или N ')

if ans3 == 'n' or ans3 == 'N':
    print('Без вашего подтверждения '
          '\nМы не сможем с вами связаться')
    ans = input('Y или N ')
    print('Хорошего дня')
