import html
class QuizLogic:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_have_questions(self):
        if self.question_number < len(self.question_list)
            return True
        else:
            return False
    def next_question(self):
        index = self.question_number
        current_question = self.question_list[index]
        current_question_text = html.unescape(current_question.text)
        response = input(f'Q.{self.question_number + 1} {current_question_text} True/False: ')
        self.check_answer(response, current_question.answer)
        return response

    def check_answer(self, user_response, answer):
        if user_response.lower() == answer.lower():
            print('You got the correct answer!')
            self.score += 1
        else:
            print('You got the wrong answer.')
        self.question_number += 1

        print(f'The correct answer was {answer} ')
        print(f'Your score is {self.score}/{self.question_number}\n')

    def end_of_quiz(self):
        print('You completed the quiz!')
        print(f'Your final score is: {self.score}')

