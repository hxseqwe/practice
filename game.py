
import random
from tkinter import Tk, Toplevel, Label, Button
from windows import WorkWindow
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

class Game:
    def __init__(self):
        self.mood = 100
        self.day = 0
        self.money = 0
        self.experience = 0
        self.starting = None
        self.nick = ""
        self.work_level = 0 
        
        self.init_window()

    def init_window(self):
        self.window = Tk()
        self.window.geometry("700x500")
        self.window.config(bg="#0a3a48")
        self.window.resizable(False, False)

        Label(self.window, text="Симулятор переводчика", bg="#0a3a48", fg="white", font=("Arial", 20)).pack(anchor="center")

        Button(self.window, text="Начать игру", height=2, width=15, fg="white", bg="#4c5acd", command=self.show_life_choice).pack(pady=30)
        Button(self.window, text="Загрузить игру", height=2, width=15, fg="white", bg="#4c5acd").pack()

        self.window.mainloop()

    def show_life_choice(self):
        """Окно выбора: 'Завести девушку' или 'Стать лингвистом'."""
        self.window.destroy()
        
        self.choice_window = Tk()
        self.choice_window.title("Выбор пути")
        self.choice_window.geometry("700x500")
        self.choice_window.config(bg="#0a3a48")
        self.choice_window.resizable(False, False)

        Label(self.choice_window, text="Выберите свой путь:", bg="#0a3a48", fg="white", font=("Arial", 20)).pack(pady=50)

        
        self.girl_btn = Button(
            self.choice_window, 
            text="Завести девушку", 
            height=2, 
            width=20, 
            fg="white", 
            bg="#ff6b81",
            command=self.girl_choice
        )
        self.girl_btn.pack(pady=20)
        self.girl_btn.bind("<Enter>", self.run_away)  

        
        Button(
            self.choice_window, 
            text="Стать лингвистом", 
            height=2, 
            width=20, 
            fg="white", 
            bg="#4c5acd",
            command=self.linguist_choice
        ).pack(pady=20)

    def run_away(self, event):
        """Заставляет кнопку 'убегать' от курсора."""
        x = random.randint(50, 650)
        y = random.randint(50, 450)
        self.girl_btn.place(x=x, y=y)  

    def girl_choice(self):
        """Если выбрали 'Завести девушку'."""
        showinfo("Ошибка", "Девушка сбежала! Попробуйте 'Стать лингвистом' 😢")
        self.choice_window.destroy()
        self.init_window() 

    def linguist_choice(self):
        """Если выбрали 'Стать лингвистом'."""
        self.choice_window.destroy()
        self.setup_game_window()

    def setup_game_window(self):
        """Окно ввода никнейма."""
        self.starting = Tk()
        self.starting.title("Игра")
        self.starting.geometry("700x500")
        self.starting.config(bg="#0a3a48")
        

        Label(self.starting, text="Введите никнейм", bg="#0a3a48", fg="white", font=("Arial", 20)).pack()

        self.entry = ttk.Entry()
        self.entry.pack(anchor="n", padx=6, pady=6)

        Button(self.starting, text="Подтвердить", height=2, width=15, fg="white", bg="#4c5acd", command=self.start_game).pack()

    def start_game(self):
        self.nick = self.entry.get()
        self.starting.destroy()
        
        self.create_game_interface()
        self.mood_func()

    def create_game_interface(self):
        self.starting = Tk()
        self.starting.title("Игра")
        self.starting.geometry("700x500")
        self.starting.config(bg="#0a3a48")

        Label(self.starting, text=f"Добро пожаловать {self.nick}", bg="#0a3a48", fg="white").pack(anchor="nw")

        self.days_counter = Label(self.starting, text=f"День - {self.day}", bg="#0a3a48", fg="white")
        self.mood_counter = Label(self.starting, text=f"Настроение - {int(self.mood)}", bg="#0a3a48", fg="white")
        self.money_counter = Label(self.starting, text=f"Деньги - {self.money}", bg="#0a3a48", fg="white")
        self.experience_counter = Label(self.starting, text=f"Опыт - {self.experience}", bg="#0a3a48", fg="white")

        for label in [self.days_counter, self.mood_counter, self.money_counter, self.experience_counter]:
            label.pack(anchor="nw")

        Button(self.starting, text="Начать следующий день", height=2, width=20, fg="white", bg="#4c5acd", command=self.new_day).pack(side="bottom", anchor="se", padx=10, pady=10)
        
        Button(self.starting, text="Работа", height=2, width=12, fg="white", bg="#4c5acd", command=self.open_work_window).pack(anchor='center', pady=10)
        Button(self.starting, text="Навыки", height=2, width=12, fg="white", bg="#4c5acd", command=self.open_skills_window).pack(anchor='center', pady=10)
        Button(self.starting, text="Развлечение", height=2, width=12, fg="white", bg="#4c5acd", command=self.open_entertainment_window).pack(anchor='center', pady=10)

    def new_day(self):
        self.day += 1
        self.days_counter.config(text=f"День - {self.day}")

    def mood_func(self):
        if self.mood > 0:
            self.mood -= 0.5
            self.mood_counter.config(text=f"Настроение - {int(self.mood)}")
            self.starting.after(1000, self.mood_func)

    def open_work_window(self):
        WorkWindow(self)

    def open_skills_window(self):
        self.open_new_window("Навыки", "Здесь будет информация о навыках")

    def open_entertainment_window(self):
        self.open_new_window("Развлечение", "Здесь будет информация о развлечениях")

    def open_new_window(self, title, message):
        new_window = Toplevel(self.starting)
        new_window.title(title)
        new_window.geometry("300x200")
        Label(new_window, text=message).pack()
