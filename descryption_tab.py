import tkinter as tk
from tkinter.ttk import Combobox 

class Descryption(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.text = tk.Text(self, width=20, height=10)
        self.text.pack()
        self.text.insert(1.0, 'Hello World!\nFoo\nBar\n\n123\n')

        self.button = tk.Button(self, text='Append', command=self.on_append)
        self.button.pack()
        #self.combo = Combobox(self)
        #self.combo['values'] = ('Цезарь', 'мультицезарь')
        #self.combo.pack()
        self.pack()

    def on_append(self):
        self.text.insert(tk.END, 'Go-go-go!\n')