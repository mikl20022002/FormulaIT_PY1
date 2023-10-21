money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
mounth = 0
while True:
    if money_capital + salary - spend * (1 + increase * mounth) > 0:
        mounth += 1
        money_capital = money_capital + salary - spend * (1 + increase * mounth)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", mounth)
