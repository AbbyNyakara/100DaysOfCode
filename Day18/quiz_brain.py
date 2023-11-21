class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questionlist = question_list


    def next_question(self):
        """
        Retrieves the question at the current question number
        """
        current_question = self.questionlist[self.question_number]
        question = input(f"Q: {self.question_number+1} {self.questionlist.text}. (True/False?): ")


