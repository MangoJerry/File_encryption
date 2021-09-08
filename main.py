# -*- coding: utf-8 -*-
"""

@author: ritak
"""

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

window = Tk()

window.title('Шифрин')

#lbl = Label(window, text="Шифрование / дешифрование данных", font=("Arial Bold", 15))
#lbl.grid(row=1, column=1, ipadx=3, ipady=6, padx=3, pady=5)
window.geometry('550x350')

# Вкладки
tab_control = ttk.Notebook(window) 
 
tab_encrypt = ttk.Frame(tab_control)  
tab_control.add(tab_encrypt, text='Шифрование')  
tab_control.pack(expand=1, fill='both')
 
tab_descrypt = ttk.Frame(tab_control)  
tab_control.add(tab_descrypt, text='Дешифрование')  
tab_control.pack(expand=1, fill='both') 

tab_info = ttk.Frame(tab_control)  
tab_control.add(tab_info, text='О программе')  
tab_control.pack(expand=1, fill='both') 

# Вкладка 1
# Выбор метода шифрования

lb_method = Label(tab_encrypt, text='Выбрать шифр')
lb_method.grid(row=0, column=0)

select_method_enc = Combobox(tab_encrypt)
select_method_enc['values'] = ('Цезарь')
select_method_enc.grid(column=1, row=0)

# Выбор файла

lb_brose = Label(tab_encrypt, text='Выбрать файл')
lb_brose.grid(row=2, column=1)
#file = filedialog.askopenfilename()


#text_path = Entry(window, width=25)  
#text_path.grid(row=1, column=1)

#btn_path = Button(text = 'Обзор', foreground="#007700")
#btn_path.grid(row=1, column=2)





window.mainloop()

