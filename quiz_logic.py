import html


class QuizLogic:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_question = {}
        self.score = 0

    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        index = self.question_number
        self.question_number += 1
        self.current_question = self.question_list[index]
        current_question_text = html.unescape(self.current_question.text)
        return f'Q.{self.question_number} {current_question_text}'
        # self.check_answer(response, current_question.answer)

    def check_answer(self, user_response):
        correct_answer = self.current_question.answer
        if user_response.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def end_of_quiz(self):
        print('You completed the quiz!')
        print(f'Your final score is: {self.score}')
