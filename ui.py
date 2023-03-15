from tkinter import *
THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.create_text(
            150,
            125,
            text='Here goes the questions',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=true_img)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=false_img)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()


