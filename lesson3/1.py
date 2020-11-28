money = int(input("введите сумму выигрыша:"))
percent1 = int(input("сколько хочет взять первый человек:"))
percent2 = int(input("сколько хочет взять второй человек:"))
percent3 = int(input("сколько хочет взять третий человек:"))
money1 = (money * percent1) / 100
money2 = (money * percent2) / 100
money3 = (money * percent3) / 100
print(f"первый человек получит {money1}")
print(f"второй человек получит {money2}")
print(f"третий человек получит {money3}")
