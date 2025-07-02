import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

myword = random.choice(listOfWords)
mywordList = list(myword)
correct_letters = []
life = 6
x = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("🌟   H A N G M A N  🌟")
print()

while True:
  inputLetter = input("Choose a letter:")
  if inputLetter in myword:
    print("Correct!")
    display = ""
    for letter in myword:
        if letter == inputLetter:
            display += letter
            correct_letters.append(inputLetter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

  else:
    print("Nope, not in here.")
    life = life - 1
    print(f"{life} left")
    print()
    print(HANGMANPICS[x])
    x= x+1
    if life < 1:
      print("YOU LOSE")
    
    
    