"""
File Name: TriviaQuiz.py
Date: 05-08-18
Author: Alex Herbert
Description: A program that tests users knowledge on streetwear related questions.
"""
#This list is used to provide a countdown to between each question
countdown = ['3','2','1','Next Question!','']
#This list provides questions which can be called upon during the quiz
questionlist = ["Question 1: What colour is Supreme's classic bogo? ",'Question 2: What country did Bape originate in? ', 'How many collaborations have The North Face and Supreme done? ','How many shoe collaborations have Off-White and Nike done? ','How many countries does Supreme haves stores in? ', 'What continent did Supreme originate in? ', 'Who is the founder of Off-White? (full name) ', 'Which popular streetwear brand did Louis Vuitton do a collaboration with? ', 'How many collaborations have Bape and Adidas done? ', 'How many collaboratiopns have Bape and Supreme done? ']
#This list contains the answers to questions, and items from it are called opun and compared to the user's answers
answerlist = ['red', 'japan', 'two', 'ten', 'three', 'america', 'virgil abloh', 'supreme', 'two', 'one']
#This function is used to 1) ask the question, 2) compare the answer to correct response, 3) give feedvback.
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
#Gives user introduction to quiz, and information about the formatting of response.
print('Welcome to the quiz! You will be tested on your hypebeast-related knowledge, so be ready! PLease enter your answers as full words, for example, 12 would be twelve. Thanks, and enjoy the quiz!')
#Sets question and answer from list, and runs 'ask' function
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
#finishes quiz
print('Thank you taking this quiz, it has now ended')
