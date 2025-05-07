
import random
from tkinter import Toplevel, Label, Button, Radiobutton, IntVar
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


class QuizWindow:
    def __init__(self, game, parent):
        self.game = game
        self.quiz_window = Toplevel(parent)
        self.quiz_window.title("Тест уровня A1")
        self.quiz_window.geometry("500x300")
        
        self.questions = [
            {
                "question": "Как переводится 'apple'?",
                "options": ["Яблоко", "Апельсин", "Груша", "Банан"],
                "correct": 0
            },
            {
                "question": "Выберите правильный артикль: ___ book",
                "options": ["a", "an", "the", "-"],
                "correct": 0
            },
            {
                "question": "Как сказать 'Привет' по-английски?",
                "options": ["Goodbye", "Hello", "Thank you", "Please"],
                "correct": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.user_choice = IntVar()
        
        self.show_question()
    
    def show_question(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()
        
        if self.current_question >= len(self.questions):
            self.show_result()
            return
        
        question_data = self.questions[self.current_question]
        
        Label(self.quiz_window, text=question_data["question"]).pack(pady=10)
        
        for i, option in enumerate(question_data["options"]):
            Radiobutton(
                self.quiz_window,
                text=option,
                variable=self.user_choice,
                value=i
            ).pack(anchor="w")
        
        Button(self.quiz_window, text="Ответить", command=self.check_answer).pack(pady=20)
    
    def check_answer(self):
        if self.user_choice.get() == self.questions[self.current_question]["correct"]:
            self.score += 1
        
        self.current_question += 1
        self.show_question()
    
    def show_result(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()
        
        result_text = f"Правильных ответов: {self.score}/{len(self.questions)}"
        Label(self.quiz_window, text=result_text).pack(pady=20)
        
        if self.score >= len(self.questions) // 2 + 1:
            reward = random.randint(50, 100)
            exp_reward = random.randint(10, 20)
            
            self.game.money += reward
            self.game.experience += exp_reward
            
            Label(self.quiz_window, text=f"Вы заработали ${reward} и {exp_reward} опыта!").pack()
            self.game.money_counter.config(text=f"Деньги - {self.game.money}")
            self.game.experience_counter.config(text=f"Опыт - {self.game.experience}")
            
           
            exp_needed = [100, 300, 600, 1000][min(self.game.work_level, 3)]
            if self.game.experience >= exp_needed and self.game.work_level < 4:
                self.game.work_level += 1
                showinfo("Повышение!", f"Вы получили новую должность: {self.game.work_level + 1} уровень!")
        else:
            Label(self.quiz_window, text="Попробуйте ещё раз!").pack()
        
        Button(self.quiz_window, text="Закрыть", command=self.quiz_window.destroy).pack()
