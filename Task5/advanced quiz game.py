# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:27:50 2024

@author: Parshv
"""

import random

class MCQuestion:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def shuffle_choices(self):
        random.shuffle(self.choices)
        self.correct_choice = chr(65 + self.choices.index(self.correct_choice))

    def is_correct(self, user_choice):
        return user_choice.upper() == self.correct_choice

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_no = 0

    def display_welcome_message(self):
        print("Welcome to the Advanced Quiz Game!")
        print('********************************************************')

    def present_question(self, question):
        self.question_no += 1
        question.shuffle_choices()

        while True:
            print(f'\n{self.question_no}. {question.text}')
            for i, choice in enumerate(question.choices, 1):
                print(f"{chr(64 + i)}. {choice}")

            user_choice_letter = input("Enter the letter of your choice: ").upper()

            if user_choice_letter in [chr(65 + i) for i in range(len(question.choices))]:
                break
            else:
                print("Invalid choice. Please enter a valid letter (A, B, C, etc.).")

        if question.is_correct(user_choice_letter):
            self.score += 1
            print('Correct! You got 1 point')
        else:
            correct_index = ord(question.correct_choice) - ord('A')
            correct_letter = chr(65 + correct_index)
            print(f'Incorrect! The correct answer is --> {correct_letter}. {question.choices[correct_index]}')

    def play_game(self):
        for question in self.questions:
            self.present_question(question)

    def display_final_results(self):
        print("\nQuiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)} ({(self.score / len(self.questions)) * 100:.2f}%)")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'

# Sample Quiz Questions
quiz_questions = [
    MCQuestion("What does CPU stand for?", ["Central Processing Unit", "Central Process Unit", "Computer Personal Unit", "Central Processor Unit"], "Central Processing Unit"),
    MCQuestion("What does GPU stand for?", ["Graphics Processing Unit", "Graphical Processing Unit", "General Processing Unit", "Graphics Processor Unit"], "Graphics Processing Unit"),
    MCQuestion("What does RAM stand for?", ["Random Access Memory", "Randomly Accessed Memory", "Read Access Memory", "Random Accessable Memory"], "Random Access Memory"),
    MCQuestion("What does PSU stand for?", ["Power Supply Unit", "Power Source Unit", "Power Supplier Unit", "Power Storage Unit"], "Power Supply Unit"),
    MCQuestion("What does ROM stand for?", ["Read Only Memory", "Random Only Memory", "Read Once Memory", "Read Operation Memory"], "Read Only Memory"),
    # Add more questions as needed
]

def main():
    while True:
        game = QuizGame(quiz_questions)
        game.display_welcome_message()
        game.play_game()
        game.display_final_results()

        if not game.play_again():
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
