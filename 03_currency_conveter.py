import requests

# Define a list of currencies
CURRENCIES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "INR": "Indian Rupee"
}

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

def fetch_exchange_rates(base_currency):
    """Fetch exchange rates for the given base currency."""
    try:
        response = requests.get(API_URL.format(base_currency))
        response.raise_for_status()
        return response.json().get('rates', {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, source_currency, target_currency, rates):
    """Convert amount from source to target currency using provided rates."""
    if source_currency not in rates or target_currency not in rates:
        raise ValueError("Invalid currency code provided.")
    
    converted_amount = amount * (rates[target_currency] / rates[source_currency])
    return converted_amount

def get_user_input():
    """Get user input for currency conversion."""
    try:
        amount = float(input("Enter the amount to convert: "))
        print("Available currencies:")
        for code, name in CURRENCIES.items():
            print(f"{code}: {name}")
        
        source_currency = input("Select source currency (code): ").upper()
        target_currency = input("Select target currency (code): ").upper()

        return amount, source_currency, target_currency
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
        return get_user_input()

def main():
    """Main function to run the currency converter."""
    while True:
        amount, source_currency, target_currency = get_user_input()
        rates = fetch_exchange_rates(source_currency)

        if rates:
            try:
                converted_amount = convert_currency(amount, source_currency, target_currency, rates)
                print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
            except ValueError as ve:
                print(ve)

        another_conversion = input("Would you like to convert another amount? (y/n): ").lower()
        if another_conversion != 'y':
            break

if __name__ == "__main__":
    main()