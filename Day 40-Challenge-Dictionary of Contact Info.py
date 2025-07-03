print("🌟  Contact Card  🌟")

myDict = {}

name = input("Input your name >").strip().capitalize()
print()
dob = input("Input your date of birth (dd/mm/yyyy) >").strip()
print()
telnum = input("Input your telephone number >").strip()
print()
email = input("Input your email >")
print()
address = input("Input your address >")
print()
print("-------------------------------------------------------")

myDict["name"] = name
myDict["dob"] = dob
myDict["telephone"] = telnum
myDict["email"] = email
myDict["address"] = address

print(f"""
Hi {myDict["name"]}, Our dictionary says that you were
born on {myDict["dob"]}, we can call you on {myDict["telephone"]},
email {myDict["email"]}, or write to {myDict["address"]}
""")

