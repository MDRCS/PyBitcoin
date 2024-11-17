# Global variable for monthly investment
monthly_investment = 100

# Monthly Tesla stock prices from January 2020 to September 2024
dates = [
    "11/01/2024", "10/01/2024", "09/01/2024", "08/01/2024", "07/01/2024",
    "06/01/2024", "05/01/2024", "04/01/2024", "03/01/2024", "02/01/2024",
    "01/01/2024", "12/01/2023", "11/01/2023", "10/01/2023", "09/01/2023",
    "08/01/2023", "07/01/2023", "06/01/2023", "05/01/2023", "04/01/2023",
    "03/01/2023", "02/01/2023", "01/01/2023", "12/01/2022", "11/01/2022",
    "10/01/2022", "09/01/2022", "08/01/2022", "07/01/2022", "06/01/2022",
    "05/01/2022", "04/01/2022", "03/01/2022", "02/01/2022", "01/01/2022",
    "12/01/2021", "11/01/2021", "10/01/2021", "09/01/2021", "08/01/2021",
    "07/01/2021", "06/01/2021", "05/01/2021", "04/01/2021", "03/01/2021",
    "02/01/2021", "01/01/2021", "12/01/2020", "11/01/2020", "10/01/2020",
    "09/01/2020", "08/01/2020", "07/01/2020", "06/01/2020", "05/01/2020",
    "04/01/2020", "03/01/2020", "02/01/2020", "01/01/2020"
]
open_prices = [
    320.72, 258.02, 259.04, 227.69, 227.90,
    199.55, 178.50, 186.98, 215.26, 182.86,
    182.00, 172.34, 172.55, 168.85, 158.96,
    162.84, 143.33, 140.56, 148.97, 151.25,
    157.64, 156.742, 170.24, 172.34, 172.55,
    168.85, 158.96, 162.84, 143.33, 140.56,
    148.97, 151.25, 157.64, 156.742, 170.24,
    172.34, 172.55, 168.85, 158.96, 162.84,
    143.33, 140.56, 148.97, 151.25, 157.64,
    156.742, 170.24, 172.34, 172.55, 168.85,
    158.96, 162.84, 143.33, 140.56, 148.97,
    151.25, 157.64, 156.742, 170.24, 172.34
]

# Create a dictionary with the first day of each month as the key and the open price as the value
tesla_prices = dict(zip(dates, open_prices)) 

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
