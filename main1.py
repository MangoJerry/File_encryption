# -*- coding: utf-8 -*-
"""

@author: ritak
"""

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

window = Tk() # экземпляр класса TK() модуля tkinter
# создать свой дочерний класс? 

window.title('Шифрин')
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
select_method_enc['values'] = ('Цезарь', 'Мульти_Цезарь')
select_method_enc.grid(column=1, row=0)



lb_brose = Label(tab_encrypt, text='Выбрать файл')
lb_brose.grid(row=2, column=1)








window.mainloop()

