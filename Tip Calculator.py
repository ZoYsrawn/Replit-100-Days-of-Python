#APPROACH 1
myBill = float(input("What was the bill?: "))
tip = int(input("How much tip would you like to give? (in percent): "))
numberOfPeople = int(input("How many people?: "))
amount = myBill + (myBill * (tip / 100))
amountPerPerson = amount / numberOfPeople
amountPerPerson = round(amountPerPerson, 2)
print(f"Each person should pay: ${amountPerPerson}")

#APPROACH 2
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)