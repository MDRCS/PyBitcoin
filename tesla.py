# Global variable for monthly investment
monthly_investment = 100

# Monthly Tesla stock opening prices from November 2019 to November 2024
tesla_prices = {
    "11/2024": 310.57, "10/2024": 257.99, "09/2024": 259.04, "08/2024": 227.69,
    "07/2024": 227.90, "06/2024": 199.55, "05/2024": 182.00, "04/2024": 186.98,
    "03/2024": 215.26, "02/2024": 227.69, "01/2024": 201.02, "12/2023": 400.51,
    "11/2023": 334.35, "10/2023": 302.00, "09/2023": 266.15, "08/2023": 245.00,
    "07/2023": 279.33, "06/2023": 256.80, "05/2023": 171.56, "04/2023": 206.78,
    "03/2023": 196.29, "02/2023": 193.53, "01/2023": 113.50, "12/2022": 185.22,
    "11/2022": 204.88, "10/2022": 254.43, "09/2022": 281.00, "08/2022": 885.00,
    "07/2022": 673.42, "06/2022": 729.59, "05/2022": 902.94, "04/2022": 1081.92,
    "03/2022": 840.20, "02/2022": 869.67, "01/2022": 1149.67, "12/2021": 1095.20,
    "11/2021": 1143.89, "10/2021": 780.59, "09/2021": 734.56, "08/2021": 700.00,
    "07/2021": 683.92, "06/2021": 627.80, "05/2021": 703.80, "04/2021": 667.93,
    "03/2021": 690.11, "02/2021": 814.29, "01/2021": 719.46, "12/2020": 597.95,
    "11/2020": 394.00, "10/2020": 421.32, "09/2020": 356.00, "08/2020": 297.00,
    "07/2020": 255.34, "06/2020": 202.37, "05/2020": 285.85, "04/2020": 507.61,
    "03/2020": 444.60, "02/2020": 673.69, "01/2020": 430.26
}

def calculate_investment_value():
    global monthly_investment
    # Calculation of total Tesla shares purchased over the months provided
    total_tesla_purchased = sum(monthly_investment / price for price in tesla_prices.values())

    # Current Tesla stock price (from the last available month, November 2024)
    current_tesla_price = tesla_prices["11/2024"]

    # Calculating the current value of total Tesla holdings
    current_value_of_holdings = total_tesla_purchased * current_tesla_price

    # Total investment over the months provided
    total_investment = monthly_investment * len(tesla_prices)  # $100 per month for each month provided

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
