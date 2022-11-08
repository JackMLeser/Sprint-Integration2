import math
import random
import time

# Created a function for the game
def storyGame():
    #Jack Leser
    #A Mad-Libz Program where you can actually win
    #Intro to game and explanation
    print("Do you want to play the game? Type Y/N: ")
    yesOrNo = input("")
    #Made an if-else statment that takes an == relational operator
    #Made an if-elif-else statement
    if yesOrNo == "Y":
        print("Ok Let's Start!")
        time.sleep(2)
    elif yesOrNo == "N":
        print("Ok, Ending Game...")
        exit()
    else:
        print("We are going to start anyway")
        time.sleep(2)
    for x in range(1,4):
        print(x)
        time.sleep(1)
    print("Mad-Libz!")
    print("The game will prompt you to type a certain type of word, noun, verb, etc.\nyou will input those answers and we will create a funny story! ")
    time.sleep(3)
    #Example of how to play
    print("For example type an animal")
    animalExample = input("Type any animal: ")
    print("I own three " + animalExample + "'s")
    time.sleep(2)
    print("Great, now we understand how it works,so while I figure out how to make a game with all my project requirments, have fun!")
    time.sleep(2)
    #Start of game
    #Setting variables:
    name = input("Type your name: ")
    time.sleep(1)
    print("Wow what a unique name")
    time.sleep(1)
    city = input("What is a place you would never want to visit : ")
    time.sleep(1)
    print("Wow Great Choice >:)")
    time.sleep(1)
    family = input("Type your least Favorite person: ")
    time.sleep(1)
    print("So the variables you chose: ",name , city , family , sep = ' ')
    time.sleep(1)
    print("Hey "+ name * 10 + " !")
    time.sleep(1)
    print("We're going to your favorite place for vacation, " + city + "! You are going with the person you love the most! Yes it is, " + family +".")
    time.sleep(2)
    #Now I am going to use the operators needed to create a story
    #Math Equation Variables Games
    #Story Plays out
    num1 = int(input("Type any number, dont worry it wont affect you! : "))
    num2 = int(input("Type a number lower than that number, dont worry it won't affect you: "))
    #Using if-else statement and >= sign
    if num2 >= num1:
        num2 = num1 - 1
    else:
        num2 = num2
    # Using boolean Values
    if num1 or num2 == num1 and num2:
        num1 = input("Input a new number: ")
        num2 = input("Input a lower number than num1: ")
    else:
        num1 = num1
        num2 = num2
    firstProblem = num1 % num2
    time.sleep(2)
    print("Ok so the vacation is off to a great start and you are so pumped to be  going to " + city + " with " + family + "!")
    #Explanation of where you are at in the game
    time.sleep(2)
    print("But now there are problems, you are:")
    time.sleep(2)
    print("1. Low on gas..")
    time.sleep(2)
    print("2. Only have $" ,firstProblem,  " in your wallet..")
    time.sleep(2)
    print("3. In the middle of the place you actually hate the most!")
    #The Solution to the game
    time.sleep(2)
    print("All hope seems lost when you look around and you cant find " + family + ".")
    time.sleep(2)
    print(family + " comes back and gives you the ticket to a lottery ticket number he bought and guess what, YOU WON!")
    time.sleep(2)
    #Numeric Operators used
    winningLottery = (num1 * num2 - 1 + 4**5)
    #If statement to make sure you have a certain amount of $ to play the game
    if winningLottery <= 1000:
        winningLottery += 1000
    else:
        winningLottery += 1
        return
    #While-in-range statement iterative structure to confirm money

    while winningLottery in range(1000,100000000):
        print("You now have $", winningLottery, ".")
    time.sleep(1)
    print("You turn around and you see that " + family + " was just thrown into a car and a mob boss needs some money for his safe return.")
    time.sleep(1)
    #MobBossCalculations
    mobBossPayment = (winningLottery / 2)
    mobBossFloorPayment = mobBossPayment // 1
    print("Now you have", mobBossFloorPayment," which is still alot.")
    print("You calculate the cost of getting back home and ending this terrible trip.")
    time.sleep(2)
    print("You look in your wallet with excitement and you have $0 left, maybe the place you chose at the beginning is not the cheapest place to visit.")
    print("Thanks for playing with these variables: " + name, city, family, num1, num2, sep = ',', end = '' )
storyGame()