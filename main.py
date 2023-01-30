import tkinter as tk
from tkinter import Menu
import math
from tkinter.messagebox import showerror
from tkinter import PhotoImage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Var
        self.entry_text = 'Gebe dein Aktuelles Gewicht ein: '
        self.image_button = PhotoImage(file='button.png')

        #Drop Down


        #Window
        self.title('Science-Calc')
        self.geometry('400x600')
        self.configure(background='#212121')

        #Label
        self.label = tk.Label(self, text='The Science Calculator', font='Arial, 18', bg='#011522', fg='white')
        self.label.pack(fill=tk.X)

        self.label02 = tk.Label(self, text='Gebe dein Aktuelles Gewicht ein: ', font='Arial, 14', bg='#282C34', fg='white')
        self.label02.pack()

        #Entry
        self.entry01 = tk.Entry(self, font='Arial, 14', text='Gebe dein Aktuelles Gewicht ein: ')
        self.entry01.pack(pady=50, ipadx=3, ipady=8)

        #Button
        self.button = tk.Button(self, text='Calculate', font='Arial, 14', command=self.calculate)
        self.button.pack(pady=40, ipadx=30)
        #self.button.place()

        #Output-Label
        self.label = tk.Label(self, bg='#011522', font='Arial, 12', text='Hier erscheint dein Ergebniss', fg='white')
        #self.label.place(y=10)
        self.label.pack(ipadx=90, ipady=50, pady=105)
        #self.label.grid(column=12)



    def calculate(self):
        try:
            self.kg = int(self.entry01.get())
            self.ofm = 1.62
            self.ofe = 9.81
            self.result = self.kg * self.ofm / self.ofe
            #print(self.result)
            self.result = f'Dein Gewicht auf dem Mond beträgt {round(self.result, 2)}kg'
            self.label.configure(text=self.result)
        except ValueError as error:
            showerror(title='Error', message=error)


if __name__ == '__main__':
    app = App()
    app.mainloop()

