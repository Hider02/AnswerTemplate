salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_incr = spend
money_capital = 0
while months:
    months -= 1
    if months == 9:
        money_capital = total_incr - salary
    else:
        total_incr = total_incr + total_incr * increase
        money_capital += total_incr - salary
months = 10
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
