
# mortgage amt. ($)
P = 344000
P = float(input("Enter mortgage amount ($): "))

# interest rate (annual %)
r = 3.5
r = float(input("Enter annual interest rate (%): "))

# duration (years)
y = 30
y = int(input("Enter loan duration (years): "))

# extra amount paid toward principal each month ($)
principal_increase = 100 
principal_increase = float(input("Enter extra principal paid per month ($): "))

# monthly interest rate
i = r * 0.01 / 12
N = y * 12

# original monthly payment (EMI)
M = P * (i * (1 + i)**N) / ((1 + i)**N - 1)

# Original Loan Total
og_total_paid = M * N

# Original Interest Paid
interest_paid = og_total_paid - P

# ---- NEW LOAN WITH EXTRA PAYMENT ----
new_payment = M + principal_increase
remaining_principal = P
months = 0
new_total_paid = 0

while remaining_principal > 0:
    interest = remaining_principal * i
    principal_paid = new_payment - interest

    # if last payment overshoots
    if principal_paid > remaining_principal:
        principal_paid = remaining_principal
        new_payment = interest + principal_paid

    remaining_principal -= principal_paid
    new_total_paid += new_payment
    months += 1

# results
new_years = months / 12
money_saved = og_total_paid - new_total_paid

# ---- OUTPUT ----
print()
print("-------------- Results --------------")
print(f"Original monthly payment: ${round(M, 2)}")
print(f"New monthly payment: ${round(M + principal_increase, 2)}")
print()

print(f"Original loan duration: {y} years")
print(f"New loan duration: {round(new_years, 2)} years")
print()

print(f"Original total paid: ${round(og_total_paid, 2)}")
print(f"New total paid: ${round(new_total_paid, 2)}")
print()

print(f"Total money saved: ${round(money_saved, 2)}")
print(f"Years saved: {y - round(new_years, 2)}")

