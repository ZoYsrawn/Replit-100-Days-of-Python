#Approach #1

name = "Katie"
age = "28"
role = "Actuarial Scientist"

a = "This is {}, she is working as an {}, and she is {} years old.".format(name, role, age)
print(a)





#Approach #2

name = "Katie"
age = "28"
role = "Actuarial Scientist"

a = "This is {name}, she is working as an {role}, and she is {age} years old.".format(name=name, role=role, age=age)
print(a)