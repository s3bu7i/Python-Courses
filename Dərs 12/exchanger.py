from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("From Currency (e.g., USD): ").upper()
            to_currency = input("To Currency (e.g., EUR): ").upper()

            result = convert_currency(amount, from_currency, to_currency)
            print(f"{amount:.2f} {from_currency} is equal to {result:.2f} {to_currency}")

        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != "yes":
            print("Thank you for using the Currency Converter!")
            break

if __name__ == "__main__":
    main()
