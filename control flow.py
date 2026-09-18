#  If conditon
print("welcome to my application")
OLD = input("HOW OLD ARE YOU\n")
if int(OLD)  >=12:
 print("OK YOU HAVE ACCSESS TO USE THE APP")
else:
 print("SORRY YOU CAN'T USE THE APP")


print ("HI")
NOM = input("TYPE THE NUMBER\n")
if float(NOM) > 0:
 print("THE NUMBER IS POSITIVE")
if float(NOM)==0:
 print("ZERO")
else:
 print("THE NUMBER IS NEGATIVE")

GRAD = float(input("TYPE YOUR GRADES /100\n"))
if GRAD >= 98:
    print("A+")
elif GRAD >= 93:
    print("A")  
elif GRAD >= 85:
    print("B+")
elif GRAD >= 80:
    print("B")  
elif GRAD >=75:
    print("C+")
elif GRAD >= 50:
    print("C")
else:
    print("F")


# using the !=
pas = input("password\n")
if pas == "abc":
  print("welcome")
else:
  print("wrong password")
# using the ==
pas = input("password\n")
if pas != "abc":
  print("wrong password")
else:
  print("welcome")
# frist project
PIN=int(input("Enter a 4-digit PIN code:\n"))
if len(str(PIN))==4:
 import random
 my_random=random.randint(1000,9999)
 if my_random==PIN:
  print(my_random)
  print("right answer")
 else:
  print(f"wrong answer the right answer is {my_random}")
else:
  print("please enter 4 digits and numbers")


# seconde project
print("Welcome to the Coin Guessing Game!")
input("press Enter to start...")
import random
random_na=random.randint(0,1)
if random_na==1:
 print("Heads")
else:
 print("tails")


# import module
import random


# function to generate random number
rand_int = random.randint(-5,5)
print(rand_int)
import shehab
print(shehab.sh)


# function to generate random float number
import random
ran_flo = random.random()*3
print(ran_flo)
print(int(ran_flo//1))

# therid project
print("""
HI
welcome in the coin guessing game
choose a method to toss the coin:
1. using random.randint() 
2. using random.random()
""")
playerch = int(input("choose from 1 or 2 :\n"))
if playerch == 1:
  import random
  rand=random.randint(0,1)
  play_ch=int(input("choose from 1 or 0 :\n"))
  if rand == play_ch:
   print ("you win")
  elif rand != play_ch:
     print("you lose the nuamber is :",str(rand))
  else:
   print ("plese Follow the instructions")
elif playerch == 2:
  import random
  rand_float=random.random() 
  play_ch=float(input("choose from 1 or 0 :\n"))
  if play_ch>rand_float:
    print("you win")
  elif play_ch<rand_float: 
    print("you lose")
  else:
    print("plese Follow the instructions")
else:
  print("plese Follow the instructions")


# how to make a list
friends=["bola", "hassan", "elshar","jeo", "Mohamed ali", "ibrahem"]
print(friends)
print(friends[0])
# print last element in the list
print(friends[-1])
# moving backward
print(friends[-2])
# How to use the list
print("In our list today the frist one is ",friends[0],"And the lasr one is",friends[-1])
# Change a name in the list
friends[0]="belal"
print(friends[0])

# How to append an element to a list in python
colors = []
colors.append("red")
colors.append("blue")
print(colors)
colors.append("green")
print(colors[2])
colors[1] = "yellow"
print(colors[1])
print(colors)


# list 1st project
Frist_color=input("Add the frist color you like :\n")
answer=input("Do you want to add more colors ? Yes or No ?\n").upper()
if answer == "YES":
  second_color=input("Add another color to the list :\n")
  colors=[]
  colors.append(Frist_color)
  colors.append(second_color)
  print(f"the color you like are {colors} ")
elif answer == "NO":
  print("ok")
  colors=[]
  colors.append(Frist_color)
  print(f"the color you like are {colors} ")
else:
  print("plesae follow the instructions")



# last projecet
own_book = input("Enter name of book you own:\n")
if own_book:
  library=[]
  library.append(own_book)
  print("ok")
  another_book = input("Enter name of another book you own (or press 'Enter' to skip):\n")
  if another_book:
    library.append(another_book)
    print(f"your library: {library}")
  else:
    print(f"your library: {library}")
else:
  print("you forgot to enter a book")

new_block = input("enter a new book you wish to have in the future:\n")
if new_block:
  wishlist=[]
  wishlist.append(new_block)
  print("OK")
  another_new_book = input("Enter name of another book you want to own in future (or press 'Enter' to skip):\n")
  if another_new_book:
    wishlist.append(another_new_book)
    print(f"your Wishlist is { wishlist}")
  else:  
     print(f"your Wishlist is { wishlist}")
else:
  print("you forgot to enter a book please try again")

OK_book=input("Enter a name of book from your wishlist that you have acquired (or press 'Enter' to skip):\n")
if OK_book in wishlist:
 library.append(OK_book)
 wishlist.remove(OK_book)
 print(f"updated library: {library}")  
 print(f"updated wishlist: {wishlist}") 
else:  
   print(f"library: {library}")  
   print(f"wishlist: {wishlist}") 

donate_book=input("Enter a name of book from your library you wish to donate (or press 'Enter' to skip):\n")
if donate_book in library:
  library.remove(donate_book)
  print(f"final library after donation: {library}")
else:
  print(f"final library {library}")  

print("Thank You for your donation")

