import random

print("Welcome to Camel! \nYou have stolen a camel to make your",
      "way accross the great Mobi desert. \nThe natives want their",
      "camel back and are chasing you down!\nSurvive your desert trek",
      "and outrun the natives!")

miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen = 5
rockets = 0

done = False
while (done == False):
   
   print("A. Drink from your canteen.")
   print("B. Ahead moderate speed.")
   print("C. Ahead full speed.")
   print("D. Stop for the night.")
   print("E. Status check.")
   print("Q. Quit.")
   print("R. Attach rockets to your camel.")

   user_input = input("Please choose an action:\n(A, B, C, D, E, Q)\n")

   if(user_input.upper() == "R"):
      rockets = 5
      print("Like Wile E. Coyote, you now have a rocket powered camel.")
   elif(user_input.upper() == "Q"):
      done = True
   elif(user_input.upper() == "E"):
      print("Miles Traveled:", miles_traveled)
      print("Drinks in canteen", canteen)
      print("The natives are", (natives_traveled*-1), "miles behind you.\n")
   elif(user_input.upper() == "D"):
      camel_tiredness = 0
      print("The camel is happy!")
      natives_traveled += random.randint(7,14)
      scorpion = random.randint(1,50)
      if(scorpion == 50):
         print("A scorpion attacks you in your sleep.")
         print("You are now dead.")
         done = True
   elif(user_input.upper() == "C"):
      miles = random.randint(10,20)
      miles_traveled += miles+rockets
      print("You have traveled", miles, "miles!")
      thirst += 1
      camel_tiredness += random.randint(1,3)
      natives_traveled += random.randint(7,14)
   elif(user_input.upper() == "B"):
      miles = random.randint(4,13)
      miles_traveled += miles+rockets
      print("You have traveled", miles, "miles!")
      thirst += 1
      camel_tiredness += 1
      natives_traveled += random.randint(7,14)
   elif(user_input.upper() == "A"):
      if(canteen == 0):
         print("Error, there are no more drinks in the canteen!")
      else:
         canteen -= 1
         thirst = 0
   else:
      print("Incorrect input, try again.")

   if(thirst > 4 and thirst <= 6):
      print("You are thirsty!")
   elif(thirst > 6):
      print("You have died of thirst!")
      done = True
   
   if(camel_tiredness > 5 and camel_tiredness <= 8):
      print("Your camel is getting tired!")
   elif(camel_tiredness > 8):
      print("Your camel has died!")
      done = True

   if(natives_traveled == 0):
      print("The natives have caught up, you are dead!")
      done = True
   elif(natives_traveled > -15 and natives_traveled < 0):
      print("The natives are getting close!")

   if(miles_traveled >= 200):
      print("You have escaped the natives!\nYou Win!")
      done = True
     
   oasis = random.randint(1,20)
   if(oasis == 20):
      print("You find an oasis!\nYou refill your canteen.")
      canteen = 5
      thirst = 0
      camel_tiredness = 0
      scorpion = random.randint(1,50)
      if(scorpion == 50):
         print("A scorpion attacks you in your sleep.")
         print("You are now dead.")
         done = True

   sandstorm = random.randint(1,30)
   if(sandstorm > 25 and sandstorm <= 27):
      print("A sandstorm suddenly overtakes you!")
      print("You get lost and lose some miles.")
      miles_traveled -= sandstorm
   elif(sandstorm > 27 and sandstorm <= 29):
      print("A sandstorm surprises you!")
      print("Your canteen is now filled with sand.")
      canteen = 0
   elif(sandstorm == 30):
      print("You have died in a horrible sandstorm.")
      done = True
