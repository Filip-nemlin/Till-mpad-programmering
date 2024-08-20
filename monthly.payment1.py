def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate= annual_rate/12/100
    months=years*12
    calculate_monthly_payments=(principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return calculate_monthly_payments


principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")