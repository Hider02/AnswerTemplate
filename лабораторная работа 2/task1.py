money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
incr_spend = spend
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0:
    count += 1
    if count >= 1:
        incr_spend = incr_spend + incr_spend * increase
        money_capital = money_capital + salary - incr_spend
    else:
        money_capital = money_capital + salary - incr_spend
print("Количество месяцев, которое можно протянуть без долгов:", count)
