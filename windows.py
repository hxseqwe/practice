
from tkinter import Toplevel, Label, Button
from quiz import QuizWindow

class WorkWindow:
    def __init__(self, game):
        self.game = game
        self.work_window = Toplevel(game.starting)
        self.work_window.title("Работа")
        self.work_window.geometry("400x400")
        
        
        self.positions = [
            "Стажёр-лингвист (0 опыта)",
            "Junior Переводчик (100 опыта)",
            "Middle Переводчик (300 опыта)",
            "Senior Переводчик (600 опыта)",
            "Главный лингвист (1000 опыта)"
        ]
        
        Label(self.work_window, text="Доступные должности:").pack()
        
        
        current_pos = self.positions[min(self.game.work_level, len(self.positions) - 1)]
        Label(self.work_window, text=f"Текущая должность: {current_pos}").pack(pady=10)
        
        
        Button(self.work_window, text="Пройти тест A1", command=self.start_quiz).pack(pady=20)
        
        
        exp_needed = [100, 300, 600, 1000][min(self.game.work_level, 3)]
        Label(self.work_window, text=f"До следующей должности: {self.game.experience}/{exp_needed} опыта").pack()
    
    def start_quiz(self):
        QuizWindow(self.game, self.work_window)