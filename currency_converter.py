import requests

# API URL to fetch exchange rates
API_URL = "https://v6.exchangerate-api.com/v6/ed7d06b60917adb2c6447f5f/latest/USD"

# Function to fetch exchange rates from the API
def get_exchange_rates(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data["conversion_rates"]
        else:
            raise Exception("Failed to fetch exchange rates.")
    except Exception as e:
        raise e

# Function for currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Unsupported currency. Please recheck the currency codes (e.g., , EUR).")

    conversion_rate = exchange_rates[to_currency]
    converted_amount = amount * conversion_rate

    return converted_amount, conversion_rate

# Function to handle user input
def get_user_input():
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source amount currency (e.g., INR): ").upper()
        to_currency = input("Enter the target currency (e.g., USD): ").upper()
        return amount, from_currency, to_currency
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value for the amount.")

# Function to display the result
def display_result(amount, from_currency, to_currency, converted_amount, conversion_rate):
    print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    print(f"Conversion rate: 1 {from_currency} = {conversion_rate:.6f} {to_currency}")

def main(api_url):
    print("Welcome to the Currency Converter!")
    print("You can convert between different currencies using real-time exchange rates.")

    try:
        exchange_rates = get_exchange_rates(api_url)
        amount, from_currency, to_currency = get_user_input()
        converted_amount, conversion_rate = convert_currency(amount, from_currency, to_currency, exchange_rates)
        display_result(amount, from_currency, to_currency, converted_amount, conversion_rate)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_url = "https://v6.exchangerate-api.com/v6/ed7d06b60917adb2c6447f5f/latest/USD"
    main(api_url)
