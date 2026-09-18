# while loop
correct_password="Shehab_Hamd"
entered_password=input("Enter your password:\n")
while entered_password!=correct_password:
  print("wronge password")
  entered_password=input("Enter your password:\n")
print("correct password") 
# for loop
for i in range(1,11):
  print(i)

# while loop firist progrm
the_Guess_number=int(input("Guess a number between 1 and 10:\n"))
import random
secret_number=random.randint(1,10)
while the_Guess_number!=secret_number:
  if the_Guess_number==secret_number+1 or the_Guess_number==secret_number-1:
   print("you are almost neer")
  elif the_Guess_number>secret_number:
   print("Too High")
  elif the_Guess_number<secret_number:
    print("Too Low")

  the_Guess_number=int(input("Guess a number between 1 and 10:\n"))
print("Well done")

# hangeman using for loop 
import random
words=["car","cat","loin","rocket","dog","human"]
PC_cho=random.choice(words)
display=["_"]*len(PC_cho)
print(f"""
           Welcome in Hangman Game
THAT IS THE NUMBER OF THE WORD = {len(PC_cho)}

             {' '.join(display)}
  +---+
  |   |
      |
      |
      |
      |
=========

  TAKE CARE YOU HAVE ONLY six CHANCES
""")
counter=6
while "_" in display and counter!=0:
 player_cho=input("please enter only one letter\n").strip().lower()
 if player_cho not in PC_cho:
    counter-=1
    print(f"Wrong anser your tries is know = {counter} ")
    if counter == 5:
     print("""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """)

    elif counter == 4:
      print("""
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
      """)
    elif counter == 3:
     print("""
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
     """)
    elif counter == 2:
     print("""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
     """)
    else:
     print("""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========

     """)



 for positon in range(len(PC_cho)):
   if PC_cho[positon]==player_cho:
      display[positon] = player_cho
      print(f"Right anser your tries is know = {counter} ")
 print(' '.join(display))

if counter > 0:
  print("""
************
  YOU WIN!
************
  """)
else:
   print("""
   ************
     YOU LOSS!
   ************
    +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
   =========

   """)

# remove the punctuation
sen=input("write your sentencs:\n")
import string
for X in sen:
  if X in string.punctuation:
    sen=sen.replace(X," ")
print(sen)


