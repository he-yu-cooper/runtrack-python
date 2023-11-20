# Initialize investment
initial_investment = 10000  # Initial investment amount is 10,000 euros
annual_return_rate = 0.05  # Annual return rate is 5%

# Calculate and display initial annual gain
initial_gain = initial_investment * annual_return_rate
print(f"Initial Annual Gain: {initial_gain:.2f} euros")

# Investor increases capital by 5000 euros, and the annual return rate increases by 2%
initial_investment += 5000
annual_return_rate += 0.02

# Calculate and display annual gain after increasing capital
new_gain = initial_investment * annual_return_rate
print(f"New Annual Gain after increasing capital: {new_gain:.2f} euros")

# Investor withdraws 10% of the total amount, and the annual return rate decreases by 1%
withdrawal_amount = initial_investment * 0.10
initial_investment -= withdrawal_amount
annual_return_rate -= 0.01

# Calculate and display final annual gain after withdrawal
final_gain = initial_investment * annual_return_rate
print(f"Final Annual Gain after withdrawal: {final_gain:.2f} euros")
