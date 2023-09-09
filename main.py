from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"\n{'-' * 30}\nYou have completed the quiz.\nFinal Score : {quiz.score}/{quiz.question_number}\n{'-' * 30}")
