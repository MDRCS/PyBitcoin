# Monthly Bitcoin prices from January 2020 to September 2024
bitcoin_prices = {
    "01/2020": 15244687.895855956, "02/2020": 14032276.919923479, "03/2020": 10586148.343373496,
    "04/2020": 14327966.853622656, "05/2020": 15321642.140355606, "06/2020": 14731567.244150743,
    "07/2020": 17313564.842167452, "08/2020": 17631359.924623117, "09/2020": 16628083.25503929,
    "10/2020": 21332958.197982565, "11/2020": 29702394.146494154, "12/2020": 42676413.44429957,
    "01/2021": 49325657.23879367, "02/2021": 67417279.1023843, "03/2021": 90555253.8379531,
    "04/2021": 86373598.27636154, "05/2021": 55280650.612654716, "06/2021": 53253110.642460465,
    "07/2021": 63023755.20351527, "08/2021": 71975399.3260943, "09/2021": 68378909.39416185,
    "10/2021": 95174313.86861314, "11/2021": 90565435.40438266, "12/2021": 73701841.61442699,
    "01/2022": 62321647.99211188, "02/2022": 69641961.44745068, "03/2022": 74061407.92496172,
    "04/2022": 64503689.51612904, "05/2022": 53553145.944179974, "06/2022": 34648438.01145663,
    "07/2022": 41308413.230535395, "08/2022": 36231568.75, "09/2022": 35993440.96224867,
    "10/2022": 37345685.394391775, "11/2022": 29889468.484965306, "12/2022": 27989593.099568725,
    "01/2023": 38561011.49266132, "02/2023": 39353423.10952067, "03/2023": 47296344.82758621,
    "04/2023": 48088260.40433476, "05/2023": 46021079.05082842, "06/2023": 50648473.44929137,
    "07/2023": 47898479.31597569, "08/2023": 43098707.21383879, "09/2023": 45976342.74117426,
    "10/2023": 58956993.36095677, "11/2023": 62327274.49455678, "12/2023": 69075576.92307693,
    "01/2024": 70933272.58466364, "02/2024": 102043281.2211343, "03/2024": 119099557.16399966,
    "04/2024": 102180024.25825715, "05/2024": 112311399.97235535, "06/2024": 105752942.5502102,
    "07/2024": 107781146.10269672, "08/2024": 96066694.10119961, "09/2024": 102125078.15291177
}

# Calculation of total Bitcoin purchased over 60 months
total_btc_purchased = sum(100 / price for price in bitcoin_prices.values())

# Current Bitcoin price (from the last available month, September 2024)
current_btc_price = bitcoin_prices["09/2024"]

# Calculating the current value of total Bitcoin holdings
current_value_of_holdings = total_btc_purchased * current_btc_price

# Total investment over 60 months
total_investment = 100 * 60  # $100 per month for 60 months

# Net gain or loss
net_gain_loss = current_value_of_holdings - total_investment

# Output the results
print(f"Total Bitcoin Purchased: {total_btc_purchased:.8f} BTC")
print(f"Current Value of Holdings: ${current_value_of_holdings:.2f}")
print(f"Total Investment: ${total_investment}")
print(f"Net Gain/Loss: ${net_gain_loss:.2f}")