import tkinter as tk
from tkinter.filedialog import askopenfilename 
from Decoder import Decoder


class Descryption(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.label_brose = tk.Label(self, text='Шифр')
        self.label_brose.place(x=10, y=40)
        
        self.path_text = tk.StringVar()
        self.text_brose = tk.Entry(self, textvariable=self.path_text)
        self.text_brose.place(x=110, y=40)
        
        self.btn_brose = tk.Button(self, text='Обзор', command=self.load_file)
        self.btn_brose.place(x=250, y=40)
        
        self.label_key_path = tk.Label(self, text='Выберите ключ')
        self.label_key_path.place(x=10, y=80)
        
        self.path = tk.StringVar() # Считываем изменения в поле
        self.key_path = tk.Entry(self, textvariable=self.path)
        self.key_path.place(x=110, y=80)
        
        self.btn_brose = tk.Button(self, text='Обзор', command=self.load_key)
        self.btn_brose.place(x=250, y=80)
        
        self.label_key = tk.Label(self, text='Значение ключа')
        self.label_key.place(x=10, y=120)
        
        self.key_var = tk.IntVar() # Считываем изменения в поле
        vcmd = (self.register(self.validate_key), "%P")
        self.key = tk.Entry(self, textvariable=self.key_var, validate = 'key', 
                              validatecommand=vcmd)
        self.key.place(x=110, y=120)
        
        self.btn_descrypt = tk.Button(self, text='Расшифровать', command=lambda: Decoder( 
                                    self.key_var.get(), self.path_text.get()).Select_Method())
        self.btn_descrypt.place(x=120, y=160)

    def load_file(self):
        self.text_brose.delete(0, 'end')
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.text_brose.insert(0, fname)
        return 
    
    def load_key(self):
        self.key_path.delete(0, 'end')
        kname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.key_path.insert(0, kname)
        with open(kname, 'r', encoding='utf-8') as key_file:
            key_value = key_file.read()
            self.key.delete(0, 'end')
            self.key.insert(0, key_value)
        return
    
    def validate_key(self, value):
        return value == "" or value.isnumeric()