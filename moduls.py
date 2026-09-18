# Built in Modules
import random
Names = ["Shehab","Sara","Hana","Islam","Sona","Sandy","Ream"]
print(random.choices(Names))
print(random.random())


# How to import a function from Module 
from random import randint
print(randint(1,10))

# How to make your own Module
import shehab as SHEBA  # make alias name
print(dir(SHEBA))
SHEBA.shehab()

# sys module
import sys
sys.path.append(r"D:\Games")
for i in sys.path:
    print(i)

# 1- Packages Downloaded From The Internet
# 2- Packages Are Folder Have Moudule


# Date and Time
import datetime
print(dir(datetime))
# Print time now
print(datetime.datetime.now())  # Every thing
print(datetime.datetime.now().year)  # Year
print(datetime.datetime.now().month) # Mounth
print(datetime.datetime.now().day)   # Day
print(40 * "=")
print(datetime.datetime.min)   # Start of the year
print(datetime.datetime.max)   # End of the year
print(40 * "=")
print(datetime.datetime.now().time())         # Every thing
print(datetime.datetime.now().time().hour)    # Hour
print(datetime.datetime.now().time().second)  # Second
print(datetime.datetime.now().time().minute)  # Minute
print(40 * "=")
# Print Specfic time
print(datetime.datetime(2005 , 9 , 27))
print(datetime.datetime(2005 , 9 , 27 , 6 , 20 , 30 ))

Nowday = datetime.datetime.now()
Birthday = datetime.datetime(2005 , 9 , 27)
print(f"I lived {(Nowday - Birthday).days} days")


# iterable vs iterator
list = [1,2,3,4,5]
X = iter(list)
print(next(X))
print(next(X))
print(next(X))
print(next(X))
print(next(X))  # error stop Iteration

print(40 * "=")
for i in list:
    print(i)

print("welcome to whose wallet game")
print("you will give me a list of names, and I will pick a person to pay")
str_names=input("if you are ready, enter the names separated by a space: ")
names= str_names.split(",")
IT=len(names)
import random
# index start from 0 but len start from 1
rand_ind=random.randint(1,IT-1)
print(f"ask {names[rand_ind]} to take his wallet out. Dinner is on him")
# using choice method
print("welcome to whose wallet game")
print("you will give me a list of names, and I will pick a person to pay")
names=input("if you are ready, enter the names separated by a space: ").split(",")
import random
print(f"ask {random.choice(names)} to take his wallet out. Dinner is on him")

# nested lists
frinds = [["Rolf", "Bob", "Anne"],["sady","fiona","jose"]]
print(frinds[0])
print(frinds[1])
print(frinds[0][0])
print(frinds[1][0])
frinds.append(["omar","lion"])
frinds.insert(2,["sara","sami"])
print(frinds)

# frist project
food=[]
food.append(["apples","bananas"])
food.append(["milk","water"])
print(food)
anser=input("press enter to change the content")
if anser:
  print("plese foloow the instructions (press enter to change the content)")
else:
  food[0].insert(0,"oranges")
  food[0].append("kiwis")
  food[1].remove("water")
  food[1].insert(0,"Tea")
  food[1].append("coffee")
  print(f"Here is the update\n{food}")

# second project
print(" welcome to place the the CAT 😺 in the night city🌇 ")
coulom_1=["🌇","🌇","🌇"]  
coulom_2=["🌇","🌇","🌇"]  
coulom_3=["🌇","🌇","🌇"] 
print(f"""
{coulom_1}
{coulom_2}
{coulom_3}
""")
player_chooice=int(input("""
where do you want to put the cat😺
by choosing a row and a column
please enter the row and after that enter the coulmn
""").strip())
if player_chooice==11:
 coulom_1.remove(coulom_1[0])
 coulom_1.insert(0,"😺")
 print(f"""
  {coulom_1}
  {coulom_2}
  {coulom_3}
  """)
elif player_chooice==12:
 coulom_1.remove(coulom_1[1])
 coulom_1.insert(1,"😺")
 print(f"""
  {coulom_1}
  {coulom_2}
  {coulom_3}
  """)
elif player_chooice==13:
 coulom_1.remove(coulom_1[2])
 coulom_1.insert(2,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
elif player_chooice==21:
 coulom_2.remove(coulom_2[0])
 coulom_2.insert(0,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
elif player_chooice==22:
 coulom_2.remove(coulom_2[1])
 coulom_2.insert(1,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
""")
elif player_chooice==23:
 coulom_2.remove(coulom_2[2])
 coulom_2.insert(2,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
elif player_chooice==31:
 coulom_3.remove(coulom_3[0])
 coulom_3.insert(0,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
elif player_chooice==32:
 coulom_3.remove(coulom_3[1])
 coulom_3.insert(1,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
elif player_chooice==33:
 coulom_3.remove(coulom_3[2])
 coulom_3.insert(2,"😺")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)
else:
 print("pleas enter a valid number and follow the rules")
 print(f"""
 {coulom_1}
 {coulom_2}
 {coulom_3}
 """)


  #thired project
a=("""
██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝
""")
b=("""
░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")
c=("""
██████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╗░░██████╔╝
██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
""")
d=[a,b,c]
print("Welcome to the Rock , Paper , Scissors Game")
pla_cho=input("press Enter to contain or type help for the rules\n").lower().strip()
if pla_cho=="help":
  print("""
  ******Rules******
  1) You choose and the computer chooses
  2) Rock smashes Scissors -> Rock wins
  3) Scissors cut Paper -> Scissors win
  4) Paper covers Rock -> Paper wins
  """)
else:
 print("lets start")

import random
pla_cho_2=input("Enter your choice (Rock, Paper, Scissors)\n").lower().strip()
e=["rock","scissors","paper"]

pc_ch=random.choice(e)
if pla_cho_2 in e:
 if pla_cho_2=="rock":
  if pla_cho_2=="rock" and pc_ch=="paper":
     e[0]=d[0]
     e[1]=d[2]
     e[2]=d[1]
     print(f"\nYOUR CHOICE\n{a}")
     print(f"COMPUTER CHOICE\n{pc_ch}")
     print("sorry you lost")
  elif pla_cho_2=="rock" and pc_ch=="rock":
     e[0]=d[0]
     e[1]=d[2]
     e[2]=d[1]
     print(f"\nYOUR CHOICE\n{a}")
     print(f"COMPUTER CHOICE\n{pc_ch}")
     print("TIES")
  else:
     e[0]=d[0]
     e[1]=d[2]
     e[2]=d[1]
     print(f"\nYOUR CHOICE\n{a}")
     print(f"COMPUTER CHOICE\n{pc_ch}")
     print("congratiuation you won")
 elif pla_cho_2=="paper":
    if pla_cho_2=="paper" and pc_ch=="scissors":
       e[0]=d[0]
       e[1]=d[2]
       e[2]=d[1]
       print(f"\nYOUR CHOICE\n{c}")
       print(f"COMPUTER CHOICE\n{pc_ch}")
       print("sorry you lost")
    elif pla_cho_2==pc_ch:
       e[0]=d[0]
       e[1]=d[2]
       e[2]=d[1]
       print(f"\nYOUR CHOICE\n{c}")
       print(f"COMPUTER CHOICE\n{pc_ch}")
       print("TIES")
    else:
       e[0]=d[0]
       e[1]=d[2]
       e[2]=d[1]
       print(f"\nYOUR CHOICE\n{c}")
       print(f"COMPUTER CHOICE\n{pc_ch}")
       print("Sorry you lost")
 else:
    if pla_cho_2=="scissors" and pc_ch=="paper":
        e[0]=d[0]
        e[1]=d[2]
        e[2]=d[1]
        print(f"\nYOUR CHOICE\n{b}")
        print(f"COMPUTER CHOICE\n{pc_ch}")
        print("congartiuation you win")
    elif pla_cho_2==pc_ch:
     e[0]=d[0]
     e[1]=d[2]
     e[2]=d[1]
     print(f"\nYOUR CHOICE\n{b}")
     print(f"COMPUTER CHOICE\n{pc_ch}")
     print("TIES")
    else:
        e[0]=d[0]
        e[1]=d[2]
        e[2]=d[1]
        print(f"\nYOUR CHOICE\n{b}")
        print(f"COMPUTER CHOICE\n{pc_ch}")
        print("Sorry you lost")
else:
  print("invalid choice, please run the program again and choose Rock, Paper, Scissors")

print("DO YOU WANT TO PLAY AGAIN")




