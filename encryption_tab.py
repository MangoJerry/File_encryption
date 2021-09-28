import tkinter as tk    
from tkinter.ttk import Combobox  
from tkinter.filedialog import askopenfilename

# Наследование свойств класса Frame

class Encryption(tk.Frame):
    def __init__(self, parent):
       
        super().__init__(parent)
        #self.parent = parent 
        self.init_ui() # инициализация метода

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)
        
        self.label_select = tk.Label(self, text='Выбор метода') 
        self.label_select.place(x=10, y=40)
        
        self.combo = Combobox(self)
        self.combo['values'] = ('Цезарь', 'Мультицезарь')
        self.combo.place(x=100, y=40)
        
        self.label_brose = tk.Label(self, text='Обзор')
        self.label_brose.place(x=10, y=65)
        
        self.text_brose = tk.Entry(self)
        self.text_brose.place(x=100, y=65)
        
        self.btn_brose = tk.Button(self, text='Обзор')
        self.btn_brose.place(x=250, y=65)

    def load_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))

        if fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return
        return
