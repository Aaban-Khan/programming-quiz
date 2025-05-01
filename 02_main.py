import random 
import pygame 
import os 

pygame.mixer.init()

def play_sound(file):
    sound_path = os.path.join(os.path.dirname(__file__), file)
    if os.path.exists(file):
        # print(f"✅ Found file: {file}")
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    else:
        print(f"❗Sound file not found: {file}")

easy = [
    {
    "question": "Which company developed the Python language?",
    "options": {
        "A": "Microsoft",
        "B": "Apple",
        "C": "Google",
        "D": "None of the above"
    },
    "answer": "D"
},
{
    "question": "Which tag is used for a paragraph in HTML?",
    "options": {
        "A": "<p>",
        "B": "<h1>",
        "C": "<div>",
        "D": "<span>"
    },
    "answer": "A"
},
{
    "question": "Which symbol is used for comments in Python?",
    "options": {
        "A": "//",
        "B": "/* */",
        "C": "#",
        "D": "<!-- -->"
    },
    "answer": "C"
}
]

medium = [
    {
    "question": "What is the output of: print(type({})) in Python?",
    "options": {
        "A": "<class 'list'>",
        "B": "<class 'dict'>",
        "C": "<class 'set'>",
        "D": "<class 'tuple'>"
    },
    "answer": "B"
},
{
    "question": "Which of the following is not a valid data type in Python?",
    "options": {
        "A": "list",
        "B": "tuple",
        "C": "array",
        "D": "dictionary"
    },
    "answer": "C"
},
{
    "question": "Which HTML tag is used to insert an image?",
    "options": {
        "A": "<img>",
        "B": "<image>",
        "C": "<pic>",
        "D": "<src>"
    },
    "answer": "A"
}
]

hard = [
    {
    "question": "Which algorithm is used to find the shortest path in a graph?",
    "options": {
        "A": "DFS",
        "B": "BFS",
        "C": "Dijkstra's Algorithm",
        "D": "Greedy Algorithm"
    },
    "answer": "C"
},
{
    "question": "What is the time complexity of binary search?",
    "options": {
        "A": "O(n)",
        "B": "O(n log n)",
        "C": "O(log n)",
        "D": "O(n^2)"
    },
    "answer": "C"
},
{
    "question": "Which keyword is used to create a class in Python?",
    "options": {
        "A": "function",
        "B": "class",
        "C": "object",
        "D": "def"
    },
    "answer": "B"
}
]

score = 0
print("\nWelcome to the Programming Quiz!")
print("----------------------------------")

def level():
    global questions
    user_level = input("\nChoose difficult Level (easy/medium/hard)?: ").strip().lower()

    if user_level not in ["easy", "medium", "hard"]:
        print(f"❗Invalid Choice!! Choose difficult Level (easy/medium/hard)")
    else:
        if user_level == "easy":
            questions = easy
        elif user_level == "medium":
            questions = medium
        else:
            questions = hard
        random.shuffle(questions)
        logic()

def logic():
    global score 
    for q in questions:
        print(f"\nQ. {q['question']}\n")

        for key, val in q["options"].items():
            print(f"{key}. {val}")

        user_input = input(f"Choose your Option (A,B,C,D)? ").strip().upper()

        while user_input not in ['A', 'B', 'C', 'D']:
            user_input = input("Invalid! Please choose from A, B, C, or D: ").strip().upper()

        if user_input == q['answer']:
            score += 1
            print("Correct ✅")
            play_sound("audio/win.wav")
        else:
            print(f"❌ Wrong Answer!! Corrrect Answer is {q['answer']}")
            play_sound("audio/lose.wav")

    if score == len(questions):
        print("🏆 Perfect Score! You're a Code Ninja!")
    elif score > 0:
        print("👍 Good Job! You know some stuff!")
    else:
        print("😅 Keep practicing, bhai!")


while True:
    level()
    ask_user = input("\nDo you Want to Play Again?(y/n): ")
    if ask_user == "n":
        print(f"\nThanks for Playing 👏")
        play_sound("audio/tie.wav")
        break
    else:
        score = 0
