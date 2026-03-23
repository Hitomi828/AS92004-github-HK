#AS92004 Hitomi Kajihara
#version 1 (10/3/26)
#version 2 (13/3/26)
#version 3 (16/3/26)
#vertion 4 (17/03/26)


ADOULTAGE = 18

import random
import time
import os
import string

questions = [
    "1, Which planet in the solar system is farthest from the Sun? : ",
    "2, How many days does it take for Earth to orbit the Sun once? : ",
    "3, Which is the largest planet in the solar system? : ",
    "4, What color are hot stars? : ",
    "5, How many days does it take for the moon to complete one orbit? : ",
    "6, At what altitude above the Earth's surface is the boundary of space considered to be? : ",
    "7, What is the most abundant gas in Earth's atmosphere? : ",
    "8, Which planet is closest to Earth? : ",
    "9, Which planet in the solar system has the strongest gravitational pull? : ",
    "10, How does the Moon's gravity compare to Earth's? : ",
    "11, On which planet is the largest volcano in the solar system located? : ",
    "12, What are Saturn's rings made of? : ",
    "13, How many minutes does it take for light from the Sun to reach Earth? : ",
    "14, Who was the scientist who proposed the equations of the universe? : ",
    "15, What cosmic phenomenon did an international research team successfully capture in images for the first time in May 2019? : ",
    "16, Who proposed the “heliocentric theory,” which states that the planets revolve around the sun? : ",
    "17, What was the name of the space program that first landed humans on the Moon? : ",
    "18, Who was the first person to use a telescope for stargazing? : ",
    "19, How far is it from Earth to the Andromeda Galaxy? :  ",
    "20, Who was the first person to walk on the Moon? : ",
]


answers = [
    "Neptune",
    "About 365 days",
    "Jupiter",
    "Blue",
    "About 27 days",
    "100 km",
    "Nitrogen",
    "Venus",
    "Jupiter",
    "One-sixth",
    "Mars",
    "Ice",
    "About 8 minutes",
    "Einstein",
    "A black hole",
    "Copernicus",
    "Apollo program",
    "Galileo Galilei",
    "2.5 million light-years",
    "Neil Armstrong",
]


def cleaned_input(user_input: str) -> str:
     cleaned = user_input.lower()
     cleaned = cleaned.replace(" ", "")
     cleaned = cleaned.strip(string.punctuation)
     return cleaned

def clear_text():
    os.system('cls' if os.name == 'nt' else "clear")

#Welcome text
def welcome_text():
    name = input("Hello please tell me your name : ")
    return name

def welcome_text2(name):
    while True:
        try:
            age = int(input(f"Ok {name}. Then tell me your age.. enter here : "))
            return age
        except ValueError:
            print("Please enter a number .")

#Age check
def age_check(age):
    if age > ADOULTAGE: # type: ignore
        print("You are so old!! Go home and work.")
        exit()
    elif age < 11: # type: ignore
        print("NO you are so young...go home and sleep.")
        exit()
    else:
        ready = cleaned_input(input("Are you ready to play????"))
        if ready == "yes":
            print("perfect lets play!")
            time.sleep(1.5)
            clear_text()
        else:
            print("See you later then..")
            exit()

def show_instructions():
    print("")

def ask_show_instructions():
    while True: 
        answer = input("Do you want to see the instructions? yes/no " ).lower().strip() 
        answer = cleaned_input(answer)

        if answer in ["yes","y"]:
            show_instructions()
            return
        elif answer in ["no","n"]:
            return
        else:
            print("Please answer yes or no.") #Ask again


def ready_to_play():
    answer = cleaned_input(input("Are you ready to play?"))
    return answer in ["yes","y"]

def play_round():
    pass



def main():
    name = welcome_text()
    age = welcome_text2(name)
    age_check(age)



    ask_show_instructions()
    
    while True:
        if ready_to_play():
            play_round()
        else:
            break


main()


#Who was the first person to use a telescope for stargazing? Galileo Galilei
#Which planet in the solar system is farthest from the Sun? Neptune
#How many days does it take for the moon to complete one orbit? About 27 days
#What are Saturn's rings made of? Ice
#Which is the largest planet in the solar system? Jupiter
#How does the Moon's gravity compare to Earth's? One-sixth
#Who was the scientist who proposed the equations of the universe? Einstein
#How far is it from Earth to the Andromeda Galaxy? 2.5 million light-years
#Which planet in the solar system has the strongest gravitational pull? Jupiter
#Who proposed the “heliocentric theory,” which states that the planets revolve around the sun? Copernicus
#What color are hot stars? Blue
#How many minutes does it take for light from the Sun to reach Earth? About 8 minutes
#What cosmic phenomenon did an international research team successfully capture in images for the first time in May 2019? A black hole
#At what altitude above the Earth's surface is the boundary of space considered to be? 100 km
#Which planet is closest to Earth? Venus
#On which planet is the largest volcano in the solar system located? Mars
#How many days does it take for Earth to orbit the Sun once? About 365 days
#Who was the first person to walk on the Moon? Neil Armstrong
#What was the name of the space program that first landed humans on the Moon? Apollo program
#What is the most abundant gas in Earth's atmosphere? Nitrogen

#https://ichigo-drill.jp/quiz-universe