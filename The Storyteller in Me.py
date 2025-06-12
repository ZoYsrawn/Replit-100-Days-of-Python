print("""Welcome to your adventure simulator.
I am going to ask you a bunch of questions
and then create an epic story with you as the star!""")

s_name = input("What is your name? > ")
e_name = input("What is your worst enemy's name? > ")
my_superpower = input("What is your superpower? > ")
superpower = input("What is your enemy's superpower? > ")
place = input("Where do you live? > ")
food = input("What is your favorite food? > ")
friend_name = input("What is your best friend's name? > ")
fsuperpower = input("What is your best friend's superpower? > ")

print("""
Hello """ + s_name + ".", "\033[31m", "Your adventure is about to begin!", "\033[0m",)
print()

print("One day, " + s_name + " was walking through the park when he saw " + e_name + ".")
print("Suddenly, " + e_name + " activated his " + superpower + " and attacked " + s_name + " and damaged his priced wrist watch!")
print()
print(s_name + " was really upset and went to " + place + " to calm down.")
print("After eating " + food + ", " + s_name + " was ready to fight back!")
print(s_name + " called his best friend, " + friend_name + ", who had the power of " + fsuperpower + ".")
print(s_name + " and " + friend_name + " reached a place where " + e_name + " was hiding")
print(s_name + " used his " + my_superpower + " and his best friend " + friend_name + " used his " + fsuperpower + ".")
print("Together, they defeated " + e_name + "\033[35m", " and saved the day!", "\033[0m",)
print()

print("THE END")
