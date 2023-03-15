from data import question_data
from question_model import Question
from quiz_logic import QuizLogic

question_bank = [Question(question['question'], question['correct_answer']) for question in question_data]

quiz_logic = QuizLogic(question_bank)

while quiz_logic.still_have_questions():
    quiz_logic.next_question()

quiz_logic.end_of_quiz()
