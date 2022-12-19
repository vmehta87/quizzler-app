from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some Question text',
            font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, columnspan=2, row=1, padx=50, pady=50)

        self.score = Label(text='Score:', fg='white', bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        check_image = PhotoImage(file='images/true.png')
        self.check = Button(image=check_image, highlightthickness=0, command=self.check_pressed)
        self.check.grid(column=0, row=2)

        ex_image = PhotoImage(file='images/false.png')
        self.ex = Button(image=ex_image, highlightthickness=0, command=self.ex_pressed)
        self.ex.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='The End')
            self.check.config(state='disabled')
            self.ex.config(state='disabled')

    def check_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def ex_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
