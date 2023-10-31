from currency_convert import convert

usd_amount = 100
eur_amount = convert(usd_amount, "USD", "EUR")
print(f"{usd_amount} USD = {eur_amount} EUR")
