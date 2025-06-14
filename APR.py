print("LOAN CALCULATOR")
print("This program calculates the monthly loan payment.")
print()

princi = 1000
print("$", princi, "over 10 years at 5% APR")
for i in range(1, 11):
  interest = princi * 0.05
  princi += interest
  print("Year", i, "is $", round(princi, 2))

total_interest = princi - 1000
print()
print("You paid $", round(total_interest, 2), "in interest!")
