import tkinter as tk    
from tkinter.ttk import Combobox  
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from key_cypher import Encryption as Enc
# Наследование свойств класса Frame

class Encryption(tk.Frame):
    def __init__(self, parent):
       
        super().__init__(parent)
        self.parent = parent 
        self.init_ui() # инициализация метода

    def init_ui(self):        
        self.pack(fill=tk.BOTH, expand=1)
        
        self.label_select = tk.Label(self, text='Выбор метода') 
        self.label_select.place(x=10, y=40)
        
        self.combo = Combobox(self)
        self.combo['values'] = ('Цезарь', 'Мультицезарь')
        self.combo.place(x=110, y=40)
        
        self.label_brose = tk.Label(self, text='Исходный текст')
        self.label_brose.place(x=10, y=80)
        
        self.path_text = tk.StringVar()
        self.text_brose = tk.Entry(self, textvariable=self.path_text)
        self.text_brose.place(x=110, y=80)
        
        self.btn_brose = tk.Button(self, text='Обзор', command=self.load_file)
        self.btn_brose.place(x=250, y=80)

        self.label_key = tk.Label(self, text='Введите ключ')
        self.label_key.place(x=10, y=120)
        
        self.key_var = tk.IntVar()
        self.key = tk.Entry(self, textvariable=self.key_var)
        self.key.place(x=110, y=120)
      
        self.btn_keygen = tk.Button(self, text='Применить')
        self.btn_keygen.place(x=250, y=120)
        
        self.btn_encrypt = tk.Button(self, text='Зашифровать', 
                command=lambda: Enc(self.path_text.get(), self.key_var.get()).AveMe())
        self.btn_encrypt.place(x=120, y=180)
        
        
    
    def select_cyph(self):
        print(self.combo.current()+1)
        return

    def load_file(self):
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.text_brose.insert(0, fname)
        return

    def entry_get_brose(self):
        key = self.key.get()
        print(key)
        with open ('key.txt', 'w', encoding='utf-8') as key_file:
            key_file.write(key)
        return 
    