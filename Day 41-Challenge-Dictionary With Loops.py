websiteDict = {"name" : "name", "URL" : "url", "Desc" : "desc", "rating" : "rate"}

answers = input("Input the website name\nthe URL\na description for the website\na star rating out of 5 ").split(",")

name, URL, desc, rating = answers

websiteDict["name"] = name
websiteDict["URL"] = URL
websiteDict["Desc"] = desc
websiteDict["rating"] = rating

for name, value in websiteDict.items():
  print(f"{name}: {value}")