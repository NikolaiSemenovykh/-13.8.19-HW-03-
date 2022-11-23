ticket = int(input('Введите количество билетов: '))
price = 0
for i in range(ticket):
    age = int(input(f'Введите возраст для {i+1} билета: '))
    if age < 18:
        print(f'Вход на конференцию для билета №{i+1} бесплатный')
        print(f'Промежуточная стоимость билета составляет {price} рублей\n')
    elif age <= 25:
        price += 990
        print(f'Промежуточная стоимость билета составляет {price} рублей\n')
    else:
        price += 1390
        print(f'Промежуточная стоимость билета составляет {price} рублей\n')

if ticket > 3:
    price -= price / 10

print (f'Общая стоимость билетов составляет {price} рублей')