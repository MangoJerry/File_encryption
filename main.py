# -*- coding: utf-8 -*-
"""

@author: ritak
"""

from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

window.title('Ефим Шифрин')

#lbl = Label(window, text="Шифрование / дешифрование данных", font=("Arial Bold", 15))
#lbl.grid(row=1, column=1, ipadx=3, ipady=6, padx=3, pady=5)
window.geometry('550x250')

lb2 = Label(window, text="Выбрать файл")
lb2.grid(row=1, column=0)

text_path = Entry(window, width=25)  
text_path.grid(row=1, column=1)

btn_path = Button(text = 'Обзор', foreground="#007700")
btn_path.grid(row=1, column=2)

select_method_enc = Combobox(window)
select_method_enc['values'] = ('Цезарь')
 #select_method_enc.current(0) 
select_method_enc.grid(column=0, row=0)



window.mainloop()

