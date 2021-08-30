from tkinter import *

THEME_COLOR = "#375362"


class GUI:

    def __init__(self):

        self.window = Tk()
        self.window.title('Atualizador Processual')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=700, height=500, bg= 'white')
        self.question_text = self.canvas.create_text(150,125, text="Escolha o tribunal:", fill= THEME_COLOR, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # right_image = PhotoImage(file= 'images\\true.png')
        self.true_button = Button( highlightthickness=0 )
        self.true_button.grid(row=2, column= 1)

        self.clicked = StringVar()
        self.clicked.set("Escolha o Tribunal")
        self.drop_menu = OptionMenu(self.window, self.clicked, "option1", "option2", "option3", "option4")
        self.drop_menu.grid(column=1, row=0)
        #
        # # false_image = PhotoImage(file= 'images\\false.png')
        # self.false_button = Button(image= false_image, highlightthickness=0,command = self.false_pressed)
        # self.false_button.grid(row=2, column= 0)

        # self.score = Label(text= 'Score: 0',fg='white',bg= THEME_COLOR)
        # self.score.grid(column=1, row=0)
        #
        # self.get_next_question()








        self.window.mainloop()
