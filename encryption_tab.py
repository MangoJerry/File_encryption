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
        
        #self.combo_var = tk.StringVar()
        self.combo = Combobox(self)
        self.combo['values'] = ('Цезарь', 'Циклический цезарь', 'Мультицезарь')
        self.combo.place(x=110, y=40)
        # При выборе метода шифрования происходит событие event и вызывается функция select_cyph
        # Метод bind() позволяет связывать виджет, собитие и действие
        self.combo.bind("<<ComboboxSelected>>", self.select_cyph) 
        
        self.label_brose = tk.Label(self, text='Исходный текст')
        self.label_brose.place(x=10, y=80)
        
        # Поле ввода пути к файлу с исходным текстом для шифрования
        self.path_text = tk.StringVar()
        self.text_brose = tk.Entry(self, textvariable=self.path_text)
        self.text_brose.place(x=110, y=80)
        
        # Кнопка выбора пути к файлу
        self.btn_brose = tk.Button(self, text='Обзор', command=self.load_file)
        self.btn_brose.place(x=250, y=80)

        self.label_key = tk.Label(self, text='Введите ключ')
        self.label_key.place(x=10, y=120)
        # Поле ввода ключа
        
        # Ограничение на ввод ключа
        self.key_var = tk.IntVar() # Считываем изменения в поле
        vcmd = (self.register(self.validate_key), "%P")
        self.key = tk.Entry(self, textvariable=self.key_var, validate = 'key', 
                              validatecommand=vcmd) 
        self.key.place(x=110, y=120)
      
        # Тестовая кнопка
        #self.btn_clear = tk.Button(self, text='Очистить поля', command=self.clear)
        #self.btn_clear.place(x=250, y=120)


    def select_cyph(self, event):
        '''
        Функция выбора метода шифрования
        '''
        if self.combo.current() == 0:
            self.btn_encrypt = tk.Button(self, text='Зашифровать', 
                command=lambda: Enc(self.path_text.get(), 
                                    self.key_var.get()).AveMe())
            self.btn_encrypt.place(x=120, y=180)
        elif self.combo.current() == 1:
            self.btn_encrypt = tk.Button(self, text='Зашифровать', 
                command=lambda: Enc(self.path_text.get(),
                                self.key_var.get()).Сaesar_Сycle())
            self.btn_encrypt.place(x=120, y=180)
        elif self.combo.current() == 2:
            self.btn_encrypt = tk.Button(self, text='Зашифровать', 
                command=lambda: Enc(self.path_text.get(),
                                self.key_var.get()).Multi_Cucle())    
            self.btn_encrypt.place(x=120, y=180)
        return 
    
    # Функция выбора пути к файлу через диалогое окно
    def load_file(self):
        self.text_brose.delete(0, 'end')
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.text_brose.insert(0, fname)
        return
# Ограничение ввода ключа только цифрами
    def validate_key(self, value):
       return value == "" or value.isnumeric()
    