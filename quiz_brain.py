class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        """Displays question and Prompts the user to enter an answer. Internally calls check_answer() to check the
        answer and update the score accordingly."""
        question = self.question_list[self.question_number]
        self.question_number += 1
        valid_user_input = False
        while not valid_user_input:
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").capitalize()
            if user_answer in ["True", "False", "T", "F"]:
                valid_user_input = True
            else:
                print("\nKindly enter a valid entry.\n")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Takes two string arguments - user answer and correct answer. Updates score and print messages accordingly to
        answer."""
        if user_answer == correct_answer or user_answer == correct_answer[0]:
            self.score += 1
            print("\nYou got it.")
        else:
            print("\nWrong answer.")
        print(f"The correct answer was: {correct_answer}\nCurrent Score: "
              f"{self.score}/{self.question_number}\n")

    def still_has_questions(self):
        """Returns a boolean after checking if the quiz still has questions left to ask user."""
        return self.question_number < len(self.question_list)
