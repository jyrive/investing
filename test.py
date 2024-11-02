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

# Example data
initial_investment = 130000
savings_rates = [1000, 1500, 2000]
yearly_return_rates = [0.05, 0.05]
target_investments = [300000, 400000, 500000]

scenarios = {}
for rate in savings_rates:
    for yearly_rate in yearly_return_rates:
        for target in target_investments:
            investments, months = calculate_investment_growth(initial_investment, rate, yearly_rate, target)
            scenarios.setdefault(rate, []).append((yearly_rate, target, investments))

# Generate a list of dates starting from today
start_date = datetime.date.today()
max_months = max(len(investments) for group in scenarios.values() for _, _, investments in group)
dates = [start_date + datetime.timedelta(days=30 * i) for i in range(max_months)]

# Determine the grid size
num_scenarios = len(scenarios)
num_cols = len(savings_rates)  # Set number of columns based on the number of savings rates
num_rows = (num_scenarios + num_cols - 1) // num_cols

# Create a figure and a grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))
axes = axes.flatten()  # Flatten the 2D array of axes

# Determine the maximum investment value across all scenarios
max_investment_value = max(investment for group in scenarios.values() for _, _, investments in group for investment in investments)

# Plot each group of scenarios in a separate subplot
for ax, (rate, group) in zip(axes, scenarios.items()):
    for yearly_rate, target, investments in group:
        ax.plot(dates[:len(investments)], investments, label=f'{yearly_rate*100}% Target {target} EUR')
        ax.annotate(f'{int(investments[-1])} EUR', 
                    xy=(dates[len(investments)-1], investments[-1]), 
                    xytext=(10, 10), 
                    textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.set_title(f'{rate} EUR/m')
    ax.set_xlabel('Date')
    ax.set_ylabel('Investment Value (EUR)')
    ax.set_ylim(0, max_investment_value)  # Set the y-axis limit
    ax.legend()
    ax.grid(True)

# Hide any unused subplots
for ax in axes[num_scenarios:]:
    ax.axis('off')

plt.tight_layout()
plt.show()