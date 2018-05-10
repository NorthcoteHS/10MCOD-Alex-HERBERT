"""
File Name: TriviaQuiz.py
Date: 05-08-18
Author: Alex Herbert
Description: A program that tests users knowledge on a variety of topics.
"""

countdown = ['3','2','1','Next Question!','']
questionlist = ["Question 1: What colour is Supreme's classic bogo? ",'Question 2: What country did Bape originate in? ', 'How many collaborations have The North Face and Supreme done?']
answerlist = ['red', 'japan', 'two']
def ask():
    answer = input(q)
    finalanswer = answer.lower()
    if finalanswer == a:
        print('Correct!')
        for item in countdown:
            print(item)
    if finalanswer != a:
        print('Incorrect :(')
        for item in countdown:
            print(item)


q = questionlist[0]
a = answerlist[0]
ask()

q = questionlist[1]
a = answerlist[1]
ask()

q = questionlist[2]
a = answerlist[2] 
ask()
