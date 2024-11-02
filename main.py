import datetime
import matplotlib.pyplot as plt

def calculate_investment_growth(initial, monthly_savings, yearly_rate, target):
    investment = initial
    months = 0
    investments = [investment]
    while months < 240:
        investment += (investment * yearly_rate / 12)
        
        if investment < target:        
            investment += monthly_savings
        
        months += 1
        investments.append(investment)
    return investments, months

initial_investment = 130000  # Example initial investment
savings_rates = [1500]  # Example savings rates
yearly_return_rates = [0.05]  # Yearly rates 5%
target_investments = [300000, 400000, 500000, 600000, 700000]  # Example target investments

scenarios = {}
for rate in savings_rates:
    for yearly_rate in yearly_return_rates:
        for target in target_investments:
            investments, months = calculate_investment_growth(initial_investment, rate, yearly_rate, target)
            scenarios[(rate, yearly_rate, target)] = investments

# Generate a list of dates starting from today
start_date = datetime.date.today()
max_months = max(len(investments) for investments in scenarios.values())
dates = [start_date + datetime.timedelta(days=30 * i) for i in range(max_months)]

# Plot the results using Matplotlib
plt.figure(figsize=(10, 6))
for (rate, yearly_rate, target), investments in scenarios.items():
    plt.plot(dates[:len(investments)], investments, label=f'{rate} EUR/m, {yearly_rate*100}%, Target {target} EUR')

plt.title('Investment Growth Scenarios')
plt.xlabel('Date')
plt.ylabel('Investment Value (EUR)')
plt.legend(title='Scenario', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
