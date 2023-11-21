from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank from the list of questions in the data 

question_bank = []

for input in question_data:
    new_question = Question(q_text = input["text"], q_answer=input["answer"])
    question_bank.append(new_question)


questions = QuizBrain(question_list=question_bank)
questions.next_question()
