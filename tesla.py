# Global variable for monthly investment
monthly_investment = 100

# Monthly Tesla stock prices from January 2020 to September 2024
tesla_prices = {
    "01/2020": 430.26, "02/2020": 673.69, "03/2020": 444.60, "04/2020": 507.61,
    "05/2020": 285.85, "06/2020": 202.37, "07/2020": 255.34, "08/2020": 297.00,
    "09/2020": 356.00, "10/2020": 421.32, "11/2020": 394.00, "12/2020": 597.95,
    "01/2021": 719.46, "02/2021": 814.29, "03/2021": 690.11, "04/2021": 667.93,
    "05/2021": 703.80, "06/2021": 627.80, "07/2021": 683.92, "08/2021": 700.00,
    "09/2021": 734.56, "10/2021": 780.59, "11/2021": 1143.89, "12/2021": 1095.20,
    "01/2022": 1149.67, "02/2022": 869.67, "03/2022": 840.20, "04/2022": 1081.92,
    "05/2022": 902.94, "06/2022": 729.59, "07/2022": 673.42, "08/2022": 885.00,
    "09/2022": 281.00, "10/2022": 254.43, "11/2022": 204.88, "12/2022": 185.22,
    "01/2023": 113.50, "02/2023": 193.53, "03/2023": 196.29, "04/2023": 206.78,
    "05/2023": 171.56, "06/2023": 256.80, "07/2023": 279.33, "08/2023": 245.00,
    "09/2023": 266.15, "10/2023": 302.00, "11/2023": 334.35, "12/2023": 400.51,
    "01/2024": 403.99, "02/2024": 362.20, "03/2024": 410.35, "04/2024": 323.00,
    "05/2024": 207.13, "06/2024": 256.80, "07/2024": 300.21, "08/2024": 227.69,
    "09/2024": 259.04
}

def calculate_investment_value():
    global monthly_investment
    # Calculation of total Tesla shares purchased over 60 months
    total_tesla_purchased = sum(monthly_investment / price for price in tesla_prices.values())

    # Current Tesla stock price (from the last available month, September 2024)
    current_tesla_price = tesla_prices["09/2024"]

    # Calculating the current value of total Tesla holdings
    current_value_of_holdings = total_tesla_purchased * current_tesla_price

    # Total investment over 60 months
    total_investment = monthly_investment * 60  # $100 per month for 60 months

    # Net gain or loss
    net_gain_loss = current_value_of_holdings - total_investment

    # Output the results
    print(f"Total Tesla Shares Purchased: {total_tesla_purchased:.8f} shares")
    print(f"Current Value of Holdings: ${current_value_of_holdings:.2f}")
    print(f"Total Investment: ${total_investment}")
    print(f"Net Gain/Loss: ${net_gain_loss:.2f}")

# Example usage
calculate_investment_value()

# To change the investment amount, simply modify the global variable and call the function again
monthly_investment = 200  # Change the investment to $200 per month
calculate_investment_value()
