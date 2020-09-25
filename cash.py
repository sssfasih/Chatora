dollars = 0
coins = 0
while dollars <= 0:
    try:
        dollars = float(input("Change Owed:"))
    except:
        pass
cents = round(dollars * 100)

while cents > 0:
    if cents >= 25:
        cents -= 25
        coins += 1
    elif cents >= 10:
        cents -= 10
        coins += 1
    elif cents >= 5:
        cents -= 5
        coins += 1
    elif cents >= 1:
        cents -= 1
        coins += 1

print(coins)