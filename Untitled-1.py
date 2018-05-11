"""
File Name: TriviaQuiz.py
Date: 05-08-18
Author: Alex Herbert
Description: A program that tests users knowledge on streetwear related questions.
"""

countdown = ['3','2','1','Next Question!','']
questionlist = ["Question 1: What colour is Supreme's classic bogo? ",'Question 2: What country did Bape originate in? ', 'How many collaborations have The North Face and Supreme done? ','How many shoe collaborations have Off-White and Nike done? ','How many countries does Supreme haves stores in? ', 'What continent did Supreme originate in? ', 'Who is the founder of Off-White? (full name) ', 'Which popular streetwear brand did Louis Vuitton do a collaboration with? ', 'How many collaborations have Bape and Adidas done? ', 'How many collaboratiopns have Bape and Supreme done? ']
answerlist = ['red', 'japan', 'two', 'ten', 'three', 'america', 'virgil abloh', 'supreme', 'two', 'one']
def ask():
   answer = input(q)
   finalanswer = answer.lower()
   if finalanswer == a:
        print('Correct!')
        for item in countdown:
            print(item)
   if finalanswer != a:
        print('Incorrect :(')
        print('The correct answer was' + answer)
        for item in countdown:
            print(item)

print('Welcome to the quiz! You will be tested on your hypebeast-related knowledge, so be ready! PLease enter your answers as full words, for example, 12 would be twelve. Thanks, and enjoy the quiz!')
q = questionlist[0]
a = answerlist[0]
ask()

q = questionlist[1]
a = answerlist[1]
ask()

q = questionlist[2]
a = answerlist[2] 
ask()

q = questionlist[3]
a = answerlist[3]
ask()

q = questionlist[4]
a = answerlist[4]
ask()

q = questionlist[5]
a = answerlist [5]
ask()

q = questionlist[6]
a = answerlist[6]
ask()

q = questionlist[7]
a = answerlist[7]
ask()

q = questionlist[8]
a =answerlist[8]
ask()

q = questionlist[9]
a = answerlist[9]
ask()
