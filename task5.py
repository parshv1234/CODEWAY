# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:48:42 2024

@author: Parshv
"""

print("Welcome to the quiz game!")
print('NOTE: If your spelling is incorrect, then it is considered as a wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play? ').lower()

if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. What does CPU stand for? ').lower()
    if ques == 'central processing unit':
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Current answer is --> central processing unit')

    # ------1
    question_no += 1
    ques = input(f'\n{question_no}. What does GPU stand for? ').lower()
    if ques == 'graphics processing unit':
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Current answer is --> graphics processing unit')

    # -----2
    question_no += 1
    ques = input(f'\n{question_no}. What does RAM stand for? ').lower()
    if ques == 'random access memory':
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Current answer is --> random access memory')

    # -----3
    question_no += 1
    ques = input(f'\n{question_no}. What does PSU stand for? ').lower()
    if ques == 'power supply unit':
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Current answer is --> power supply unit')

    # -----4
    question_no += 1
    ques = input(f'\n{question_no}. What does ROM stand for? ').lower()
    if ques == 'read only memory':
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Current answer is --> read-only memory')

    # ------5 

else:
    print('Thank you, you are out of the game.')
    quit()

print(f'\nNumber of questions: {question_no}')
print(f'Your score is: {score}')

try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    percentage = 0
    print('0% questions are correct')

print(f'{percentage}% of questions are correct.')
