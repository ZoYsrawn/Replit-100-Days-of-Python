#APPROACH 1
print("THE GRADE CALCULATOR")
print("=====================")
print()
print()
print(
    "Welcome to the Grade Calculator. Please answer the following questions to get your grade."
)
print()
mytest = input("What is the name of your test? ")
maxscore = int(input("What is the maximum score of the test? "))
myscr = float(input("What is your score? "))
percentage = round((myscr / maxscore) * 100, 2)

if percentage >= 90:
  print("Your grade for", mytest, "is A+ 🏆 with a percentage of", percentage,
        "%")
elif 80 <= percentage < 90:
  print("Your grade for", mytest, "is A 🤩 with a percentage of", percentage,
        "%")
elif 70 <= percentage < 80:
  print("Your grade for", mytest, "is B 👏🏻 with a percentage of", percentage,
        "%")
elif 60 <= percentage < 70:
  print("Your grade for", mytest, "is C 😊 with a percentage of", percentage,
        "%")
elif 50 <= percentage < 60:
  print("Your grade for", mytest, "is D 🙁 with a percentage of", percentage,
        "%")
elif percentage < 50:
  print("Your grade for", mytest, "is U 💀 with a percentage of", percentage,
        "%")
else:
  print("Invalid input. Please try again.")

#APPROACH 2

print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()

number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_perc = round(float(your_score / total_score) * 100, 2)

print("You got", final_perc, "%")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else:
  print("Try again!")
