import random 
import pygame 
import os 

pygame.mixer.init()

def play_sound(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    else:
        print(f"❗Sound file not found: {file}")

questions = [
    {
        "question": "What does HTML stand for?",
        "options": {
            "A": "HyperText Markup Language",
            "B": "HighText Machine Language",
            "C": "Hyperloop Machine Language",
            "D": "None of the above"
        },
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": {
            "A": "Python",
            "B": "C++",
            "C": "JavaScript",
            "D": "Java"
        },
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": {
            "A": "6",
            "B": "8",
            "C": "9",
            "D": "5"
        },
        "answer": "B"
    }
]

score = 0
random.shuffle(questions)

def logic():
    global score 
    for q in questions:
        print(f"\nQ. {q['question']}\n")

        for key, val in q["options"].items():
            print(f"{key}. {val}")

        user_input = input(f"Choose your Option (A,B,C,D)? ").strip().upper()

        while user_input not in ['A', 'B', 'C', 'D']:
            user_input = input("Invalid! Please choose from A, B, C, or D: ").strip().upper()

        if user_input == q["answer"]:
            score += 1
            print("Correct ✅")
            play_sound("audio/win.wav")
        else:
            print(f"❌ Wrong Anser!! Corrrect Answer is {q["answer"]}")
            play_sound("audio/lose.wav")

    if score == len(questions):
        print("🏆 Perfect Score! You're a Code Ninja!")
    elif score > 0:
        print("👍 Good Job! You know some stuff!")
    else:
        print("😅 Keep practicing, bhai!")

print("Welcome to the Programming Quiz!")
print("----------------------------------")

while True:
    logic()
    ask_user = input("\nDo you Want to Play Again?(y/n): ")
    if ask_user == "n":
        print(f"\nThanks for Playing 👏")
        play_sound("audio/tie.wav")
        break
    else:
        score = 0

