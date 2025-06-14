print("List Generator")
print("--------------")
print()
print("This program generates a list of numbers.")
print("You will be asked to enter the number of elements")
print()
st = int(input("Start at: "))
en = int(input("End before: "))
incr = int(input("Increment between values: "))
if st > en and incr > 0:
  print(
      "Invalid input. Start value must be less than end value when increment is positive."
  )
elif st < en and incr < 0:
  print(
      "Invalid input. Start value must be greater than end value when increment is negative."
  )
else:
  print("Generating list...")
  print()
  for i in range(st, en, incr):
    print(i)
