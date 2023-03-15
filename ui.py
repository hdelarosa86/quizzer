from tkinter import *
from quiz_logic import QuizLogic
THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_logic: QuizLogic):
        self.quiz = quiz_logic

        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.q_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Here goes the questions',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=true_img, command=self.is_true_pressed)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=false_img, command=self.is_false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=question_text)

    def is_true_pressed(self):
        result = self.quiz.check_answer('True')
        self.get_next_question()

    def is_false_pressed(self):
        result = self.quiz.check_answer('False')
        self.get_next_question()


