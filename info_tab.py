import tkinter as tk

class Info(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        label_text = ''' Эта программа предназначена для шифрования 
        и дешифрования текста в формате *.txt. 
        Выбранныей посредством диалогового окна текст
        шифруется одним из трех вариаций шифра Цезаря. 
        Зашифрованный текст записывается в файл, 
        в отдельный файл записывается ключ шифрования.
        Ключ шифрования должен храниться в секрете от любого 
        человека, 
        который не должен прочитать зашифрованное сообшение. 
        Для дешифрации текста необходимо выбрать 
        файл с шифром и ключ посредством диалогового окна и 
        готовый текст сохранится в файле.'''
        self.label_info = tk.Label(self, text=label_text)
        self.label_info.pack()
        self.pack()

