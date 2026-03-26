#AS92004 Hitomi Kajihara
#version 1 (10/03/26)
#version 2 (13/03/26)
#version 3 (16/03/26)
#vertion 4 (17/03/26)
#version 5 (24/03/26)
#version 6 (26/03/26)
#version 7 (27/03/26)

ADOULTAGE = 18

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
    ["Neptune"],
    ["About 365 days","365","365 days",],
    ["Jupiter"],
    ["Blue"],
    ["About 27 days","27","27 days"],
    ["100 km","100"],
    ["Nitrogen"],
    ["Venus"],
    ["Jupiter"],
    ["One-sixth","1/6","one sixth"],
    ["Mars"],
    ["Ice"],
    ["About 8 minutes","8","8 minutes"],
    ["Einstein"],
    ["A black hole","black hole"],
    ["Copernicus"],
    ["Apollo program","apollo"],
    ["Galileo Galilei","Galileo"],
    ["2.5 million light-years","2.5 million"],
    ["Neil Armstrong","armstrong"],
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
    print("""
█░█ █▀▀ █░░ █░░ █▀█   █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █░█ █▄░█ █ █░█ █▀▀ █▀█ █▀ █▀▀   █▀█ █░█ █ ▀█
█▀█ ██▄ █▄▄ █▄▄ █▄█   ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄█ █░▀█ █ ▀▄▀ ██▄ █▀▄ ▄█ ██▄   ▀▀█ █▄█ █ █▄""")
    name = input("\nPlease tell me your name : ")
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
        ready = cleaned_input(input("\nAre you ready to play???? (yes/no) : "))
        if ready == "yes":
            print("""
█▀█ █▀▀ █▀█ █▀▀ █▀▀ █▀▀ ▀█▀   █░░ █▀▀ ▀█▀ █▀   █▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █
█▀▀ ██▄ █▀▄ █▀░ ██▄ █▄▄ ░█░   █▄▄ ██▄ ░█░ ▄█   ▄█ ░█░ █▀█ █▀▄ ░█░ ▄""")
            time.sleep(1.5)
            clear_text()
        else:
            print("See you later then..")
            exit()

def show_instructions():
    print("\nHi. This quiz is about universe. \nAll quiz is from : https://ichigo-drill.jp/quiz-universe \nYou can choose difficulty.. ")

def ask_show_instructions():
    while True: 
        answer = input("\nDo you want to see the instructions? (yes/no) :  " ).lower().strip() 
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

def choose_difficulty():
    while True:
        print("\nChoose difficulty :")
        print("1. EASY   (10 questions)")
        print("2. MIDIUM (15 questions)")
        print("3. HARD   (20 questions)")
        choice = input("Enter 1 or 2 or 3 : ").strip()

        if choice == "1":
            return 10
        elif choice == "2":
            return 15
        elif choice == "3":
            return 20
        else:
            print("Invaild choice. Please enter 1 or 2 or 3. ")
        
def play_round(index):
    print(questions[index])
    user_answer = cleaned_input(input("Your answer : "))
    time.sleep(1.5)
    clear_text()
    
    correct_list = [cleaned_input(a) for a in answers[index]]

    if user_answer in correct_list:
            print("Thats correct!!!")
            return True, user_answer
    else:
            print(f"Humm its rong.... Correct answer is {answers[index][0]} ")
            return False, user_answer
    


def main():
    name = welcome_text()
    age = welcome_text2(name)
    age_check(age)

    ask_show_instructions()
    
    total_questions = choose_difficulty()

    score = 0
    history = []

    for i in range(total_questions):
        print(f"Question {i+1}:")
        correct, user_answer = play_round(i)

        if correct:
            score += 1

        history.append ({
            "question": questions [i],
            "your_answer": user_answer,
            "correct_answer": answers[i][0],
            "result": "Correct" if correct else "Wrong"
        })

        print()

    print(f"{name}, you got {score} out of {total_questions} correct ")


    show = cleaned_input(input("Do you want to see the result history? (yes/no): "))

    if show != "yes":
        print("OK! Thank you for playing!!!")
        return


    print("\n-------HISTORY-------\n")

    for item in history:
        print(f"Q: {item['question']}")
        print(f"Your answer: {item['your_answer']}")

        if item["result"] == "Correct":
            print(f"Result: Correct!")
        else:
            print(f"Result: Wrong… Correct answer was: {item['correct_answer']}")

        print()

    print("Thank you fpor playing!!")

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