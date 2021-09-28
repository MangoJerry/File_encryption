import tkinter as tk
from tkinter.filedialog import askopenfilename 

class Descryption(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.label_brose = tk.Label(self, text='Шифр')
        self.label_brose.place(x=10, y=40)
        
        self.text_brose = tk.Entry(self)
        self.text_brose.place(x=110, y=40)
        
        self.btn_brose = tk.Button(self, text='Обзор', command=self.load_file)
        self.btn_brose.place(x=250, y=40)
        
        self.label_key = tk.Label(self, text='Выберите ключ')
        self.label_key.place(x=10, y=80)
        
        self.key = tk.Entry(self)
        self.key.place(x=110, y=80)
        
        self.btn_keygen = tk.Button(self, text='Обзор', command=self.load_key)
        self.btn_keygen.place(x=250, y=80)
        
        self.btn_descrypt = tk.Button(self, text='Расшифровать')
        self.btn_descrypt.place(x=120, y=140)

    def load_file(self):
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.text_brose.insert(0, fname)
        return
    
    def load_key(self):
        kname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*")))
        self.key.insert(0, kname)
        return