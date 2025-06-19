import os
import time

print("Welcome")
print("to")
print("Replit")

time.sleep(1)
os.system("clear")

for i in range(10, 0, -1):
  print(i)
  time.sleep(1)
  os.system("clear")

username = input("Username: ")
print("Welcome " + username)
