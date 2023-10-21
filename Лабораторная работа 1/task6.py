salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for month in range(10):
    money_capital += salary - spend * (1 + increase) ** month

# money_capital = salary * months - spend * months

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", abs(round(money_capital, 2)))
