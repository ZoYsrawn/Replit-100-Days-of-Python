print("🌠  Accessing 2D Dictionaries  🌠")
print()

john = {"daysComp": 46, "streak": 22}
david = {"daysComp": 23, "streak": 23}
solomon = {"daysComp": 75, "streak": 6}
courseProg = {"john": john, "david": david, "solomon": solomon}

print(courseProg)

#Accessing into one layer:
print()
print(courseProg["john"])

#Accessing into two layers:
print()
print(courseProg["david"]["streak"])
