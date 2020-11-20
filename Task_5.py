revenue = int(input('Enter your current revenue: '))
costs = int(input('Enter your current costs: '))
profit = revenue - costs

if profit > 0:
    print('Your current profit is {}, your profitability is {}, your profit per employee is {}'.format(profit,profitability,profit_per_employee))
    employees = float(input('Enter number of employees: '))
    profit_per_employee = employees/profit
    profitability = profit/revenue
else:
    print('Your loss is {}'.format(profit))