class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        valid_user_input = False
        while not valid_user_input:
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").capitalize()
            if user_answer in ["True", "False", "T", "F"]:
                valid_user_input = True
            else:
                print("\nKindly enter a valid entry.\n")
        self.check_answer(user_answer, question)

    def check_answer(self, user_answer, question):
        if user_answer == question.answer or user_answer == question.answer[0]:
            self.score += 1
            print("\nYou got it.")
        else:
            print("\nWrong answer.")
        print(f"The correct answer was: {question.answer}\nCurrent Score: "
              f"{self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
