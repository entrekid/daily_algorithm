orders = input()[1:-1].split(", ")
orders = [elem[1:-1] for elem in orders]
result = []
bank = {}
for order in orders:
    law, deposit, money = order.split()
    money = int(money)
    if law == "DEPOSIT":
        if deposit in bank.keys():
            bank[deposit][1] += money
            result.append(200)
        else:
            result.append(404)
    
    elif law == "CREATE":
        if deposit in bank.keys():
            result.append(403)
        else:
            bank[deposit] = [money, 0]
            result.append(200)
    elif law == "WITHDRAW":
        if deposit not in bank.keys():
            result.append(404)
        elif deposit in bank.keys():
            if money > bank[deposit][0]:
                result.append(403)
            else:
                bank[deposit][1] -= money
                result.append(200)
print(result)


