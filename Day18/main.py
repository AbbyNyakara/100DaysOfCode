from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank from the list of questions in the data 

question_bank = []

for input in question_data:
    new_question = Question(q_text = input["text"], q_answer=input["answer"])
    question_bank.append(new_question)

# Create the quiz: 

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your total score is {quiz.score}/{len(question_bank)}")