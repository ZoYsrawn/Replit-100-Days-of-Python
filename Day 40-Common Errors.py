#ERROR 1

myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")

#ASNWER 1

myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

# This code outputs 'Your name is David and your age is 128'.

print("---------------------------------------------------------------------------------------------------")

#ERROR 2

myUser = {"name": "David", "age": 128}

print(myUser{"name"})

#ANSWER 2

myUser = {"name": "David", "age": 128}

print(myUser["name"])

print("---------------------------------------------------------------------------------------------------")

#ERROR 3

myUser = {name: "David", "age": 128}

print(myUser["name"])

#ANSWER 3

myUser = {"name": "David", "age": 128}

print(myUser["name"])

print("---------------------------------------------------------------------------------------------------")

#ERROR 4

myUser = {name:"David", "age": 128, "age" = 129}

print(myUser)

#ANSWER 4

myUser = {name:"David", "age": 128}

myUser["age"] = 129

print(myUser)

print("---------------------------------------------------------------------------------------------------")