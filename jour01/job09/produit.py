class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")
        print()

def main():
    # Create product objects
    product1 = Product("Product A", 100.0, 100)

    # Display initial product information
    print("Initial Product Information:")
    product1.display_info()

    # User purchases product, update stock
    quantity_purchased = int(input("Enter the quantity you want to purchase for Product A: "))
    product1.stock -= quantity_purchased
    print(f"{quantity_purchased} units of Product A purchased. Updated stock.")

    # Product price increases by 10%
    product1.price *= 1.1
    print("Product price increased by 10%.")

    # Display updated product information
    print("\nUpdated Product Information:")
    product1.display_info()

if __name__ == "__main__":
    main()
