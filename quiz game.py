import os
import random

# ANSI color codes for colorful output
COLORS = [
    '\033[95m',  # Magenta
    '\033[94m',  # Blue
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[91m',  # Red
    '\033[96m',  # Cyan
    '\033[0m'    # Reset
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def color_text(text, color_idx):
    return COLORS[color_idx % (len(COLORS)-1)] + text + COLORS[-1]

class Question:
    def __init__(self, prompt, options, answer, fun_fact):
        self.prompt = prompt
        self.options = options
        self.answer = answer
        self.fun_fact = fun_fact

questions = [
    Question(
        "Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Venus"],
        2,
        "Mars is red due to iron oxide (rust) on its surface!"
    ),
    Question(
        "Who wrote the play 'Romeo and Juliet'?",
        ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        2,
        "'Romeo and Juliet' is one of Shakespeare's most famous tragedies."
    ),
    Question(
        "What is the largest mammal in the world?",
        ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        2,
        "The blue whale can weigh up to 200 tons!"
    ),
    Question(
        "Which element has the chemical symbol 'O'?",
        ["Gold", "Oxygen", "Osmium", "Oganesson"],
        2,
        "Oxygen is essential for respiration in most living organisms."
    ),
    Question(
        "What is the capital of Japan?",
        ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        3,
        "Tokyo is one of the world's most populous cities."
    ),
]

def ask_question(q, idx):
    print(color_text(f"\nQuestion {idx+1}: {q.prompt}", idx))
    for i, opt in enumerate(q.options, 1):
        print(color_text(f"  {i}. {opt}", idx+1))
    while True:
        try:
            choice = int(input(color_text("Your answer (1-4): ", idx+2)))
            if 1 <= choice <= 4:
                return choice
            else:
                print(color_text("Please enter a number between 1 and 4.", 4))
        except ValueError:
            print(color_text("Invalid input. Enter a number.", 4))

def show_fun_fact(q, correct):
    if correct:
        print(color_text("Correct! 🎉", 2))
    else:
        print(color_text("Oops! That's not correct.", 1))
    print(color_text("Fun Fact: " + q.fun_fact, 3))

def main():
    clear_screen()
    print(color_text("🌈 Welcome to the Colorful Quiz Game! 🌈", 0))
    print(color_text("Test your knowledge and learn fun facts along the way!\n", 1))
    random.shuffle(questions)
    score = 0
    for idx, q in enumerate(questions):
        user_ans = ask_question(q, idx)
        correct = (user_ans == q.answer)
        if correct:
            score += 1
        show_fun_fact(q, correct)
        input(color_text("Press Enter to continue...", 5))
        clear_screen()
    print(color_text(f"Quiz Over! Your final score: {score}/{len(questions)}", 0))
    if score == len(questions):
        print(color_text("🏆 Perfect Score! You're a quiz master! 🏆", 2))
    elif score > len(questions)//2:
        print(color_text("Great job! Keep learning! 🌟", 3))
    else:
        print(color_text("Don't worry, try again for a better score! 💡", 1))

if __name__ == "__main__":
    main()