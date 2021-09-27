# -*- coding: utf-8 -*-
"""

@author: ritak
"""

from tkinter import Tk, ttk
import tkinter as tk

# Импорт модулей, реализующих вкладки
from encryption_tab import Encryption as Enc
from descryption_tab import Descryption as Desc
from info_tab import Info as Inf


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Cat')
        self.window.geometry("500x500")
        self.create_widgets()  # Вызов функции создания вкладок
        # Вкладки
        
    def create_widgets(self):
        # Отступы 
        self.window['padx'] = 10
        self.window['pady'] = 10
        # Размер вкладок в окне     
        self.notebook = ttk.Notebook(self.window, width=500, height=500)

        # Создание виджетов на вкладках
        tab_enc = Enc(self.notebook)        
        tab_desc = Desc(self.notebook)
        tab_info = Inf(self.notebook)

        self.notebook.add(tab_enc, text="Шифование")
        self.notebook.add(tab_desc, text="Дешифрование")
        self.notebook.add(tab_info, text="О программе")
        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = App()
    program.window.mainloop()


