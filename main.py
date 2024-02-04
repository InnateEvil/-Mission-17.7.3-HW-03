per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую планируете положить под проценты: "))

deposit = [int(money * percent / 100) for percent in per_cent.values()]

max_deposit = max(deposit)

print("Максимальная сумма, которую вы можете заработать:")
for bank, amount in zip(per_cent.keys(), deposit):
    print(f"{bank}: {amount}")

print(f"\nМаксимальный депозит: {max_deposit}")
