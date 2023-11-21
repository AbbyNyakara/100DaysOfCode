from question_model import Question
from data import question_data

# Create a question bank from the list of questions in the data 

question_bank = []

for input in question_data:
    new_question = Question(q_text = input["text"], q_answer=input["answer"])
    question_bank.append(new_question)


print(question_bank[0].text)