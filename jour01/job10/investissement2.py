class InvestmentSimulation:
    def __init__(self, initial_investment, annual_return_rate):
        self.investment = initial_investment
        self.annual_return_rate = annual_return_rate / 100  # Convert percentage to decimal

    def display_annual_gain(self):
        annual_gain = self.investment * self.annual_return_rate
        print(f"Annual Gain at {self.annual_return_rate * 100}% return rate: {annual_gain:.2f} euros")

    def increase_capital_and_rate(self, increase_amount, increase_rate):
        self.investment += increase_amount
        self.annual_return_rate += increase_rate / 100  # Convert percentage to decimal
        print(f"\nAfter increasing capital by {increase_amount} euros and increasing return rate by {increase_rate}%,")
        self.display_annual_gain()

    def withdraw_and_decrease_rate(self, withdrawal_rate, decrease_rate):
        withdrawal_amount = self.investment * withdrawal_rate
        self.investment -= withdrawal_amount
        self.annual_return_rate -= decrease_rate / 100  # Convert percentage to decimal
        print(f"\nAfter withdrawing {withdrawal_rate * 100}% of the total amount and decreasing return rate by {decrease_rate}%,")
        self.display_annual_gain()

def main():
    # Initialize investment
    initial_investment = float(input("Enter the initial investment amount in euros: "))
    annual_return_rate = float(input("Enter the annual return rate in percentage: "))
    investment_simulation = InvestmentSimulation(initial_investment, annual_return_rate)

    # Display initial annual gain
    print("\nInitial Simulation:")
    investment_simulation.display_annual_gain()

    # Increase capital and return rate
    investment_simulation.increase_capital_and_rate(5000, 2)

    # Withdraw funds and decrease return rate
    investment_simulation.withdraw_and_decrease_rate(0.10, 1)

if __name__ == "__main__":
    main()
