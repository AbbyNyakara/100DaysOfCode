class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questionlist = question_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.questionlist)

    def next_question(self):
        """
        Retrieves the question at the current question number
        Asks the user a question and prompts an answer
        """
        question = self.questionlist[self.question_number]
        self.question_number += 1
        answer = input(f"Q {self.question_number}: {question.text}. (True/False)")

        # We will run the check_answer function here. Not in the main.py file
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks whether the user's answer to the quiz is correct."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")    
        else:
            print("You got it wrong")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")


