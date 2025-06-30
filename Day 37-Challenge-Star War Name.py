print("🌟Star Wars Name Generator🌟")

name = input("Input your first name,\nlast name,\nmother's madien name, and\nthe city where you were born, separated by a tab\n> ")

a,b,c,d = name.split()
firstname = f"{a[:3].capitalize()}{b[:3].lower()}"
lastname = f"{c[:2].capitalize()}{d[-3:].lower()}"
print("Your Star Wars name is ", firstname, lastname)
