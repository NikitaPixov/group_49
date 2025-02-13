from random import randint


def guess_the_number(capital, min_number, max_number, attempts):
    while attempts > 0:
        random_number = randint(min_number, max_number)
        if capital <= 0:
            print('вы проиграли у вас нету денег')
            break
        print(f'количество попыток: {attempts}')
        number = int(input(f"Выберите число от {min_number} до {max_number}: "))
        if number > max_number or number < min_number:
            print('неправильное число')
            continue
        user_capital = int(input(f"Выбирите ставку,у вас {capital}: "))


        if 0 < user_capital <= capital:
            if number == random_number:
                capital += user_capital * 2
                print(f'Поздровляю вы победили ваша ставка вышла в плюс и умножилась на 2\n Ваш капитал: {capital}')
            elif number != random_number:
                capital -= user_capital
                print((f'Сожелею но ваша ставка не сыграла и вы проиграли\n Ваш капитал: {capital}'))
            else:
                print('Ошибка!')
        else:
            print('НЕ ХВАТАЕТ ДЕНЕГ!')
            continue

        attempts -= 1
