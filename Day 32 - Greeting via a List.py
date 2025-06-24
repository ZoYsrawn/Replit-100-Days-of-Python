import random

print("▼ ▼ ▼  GREETINGS  ▼ ▼ ▼")
print()
print()
hello = ["Hello", "Hola", "Konnichi Wa", "مرحبا", "안녕하세요", "Ciao", "Здравствуйте", "Selam", "السلام علیکم", "Guten tag"]

x = random.randint(0, len(hello)-1)
print(hello[x])
