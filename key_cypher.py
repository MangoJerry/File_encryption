import os
import tkinter.messagebox as mb


class Encryption:
    def __init__(self, full_path_text, key):
        self.full_path_text = full_path_text
        self.key = key
        if int(key) > 159:
            self.key = int(key) % 159
            # Создание файла с ключом и запись в него
        if os.path.exists(self.full_path_text):
            if os.path.exists(self.full_path_text.replace('.txt', '_key.txt')):
                temp_file = self.full_path_text.replace('.txt', '_key.txt')
                os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии - условие выше)
            file_key = self.full_path_text.replace('.txt', '_key.txt')
            with open(file_key, 'w', encoding='utf-8') as key_file:
                key_file.write(str(self.key))
        else:
            mb.showerror("Ошибка", f'Путь {self.full_path_text} ссылается на несуществующий файл') 
        
    def AveMe(self):
        '''
        :about_it
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
        :return: ->file.txt
            Название файла "Имя_файла_текса + _cypher.txt"
        '''
        # Проверка на наличие одноименного файла_шифра
        if os.path.exists(self.full_path_text):
            if os.path.exists(self.full_path_text.replace('.txt', '_cypher.txt')):
                temp_file = self.full_path_text.replace('.txt', '_cypher.txt')
                os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии - условие выше)
            file_cypher = self.full_path_text.replace('.txt', '_cypher.txt')
        else:
            mb.showerror("Ошибка", f'Путь {self.full_path_text} ссылается на несуществующий файл')
        key = self.key
        # Открытие и работа с файлом_текстом
        with open(self.full_path_text, 'r', encoding='utf-8') as file_text:
            # Пробежка по всем строкам файла
            for line in file_text:
                # Строка_шифр для записи построчно в новый файл + ее обнуление
                cypher = ''
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    # Проверка на локализацию ползунка и перенос при необходимости
                    if 126 < ord(line[index]) + key < 1040:
                        index_cypher = ord(line[index]) + key + 913  # суть шифра
                        cypher += chr(index_cypher)
                    elif 1103 < ord(line[index]) + key:
                        index_cypher = ord(line[index]) + key - 1072  # суть шифра
                        cypher += chr(index_cypher)
                    else:
                        index_cypher = ord(line[index]) + key  # суть шифра
                        cypher += chr(index_cypher)
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                    cypher = cypher[:-1]
                print(cypher)
                # Запись строки в файл
                with open(file_cypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода
                    if os.stat(file_cypher).st_size == 0:
                        cypher += '1'
                    file_write.write(cypher + '\n')
            mb.showinfo("Ок", "Текст успешно зашифрован")
                    
    def Сaesar_Сycle(self):
        '''
        :about_it
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
            Данный шифратор отличается от AveMe тем, что на каждом вычислении
            индекса по таблице ASCII происходит циклическое увеличение/умень-
            шение на 1 числа сдвигов (растет до 10, затем падает до 0, затем
            снова растет и тд.)
        :return: ->file
            Название файла "Имя_файла_текса + _cypher.txt"
        '''
        # Проверка на наличие файла
        if os.path.exists(self.full_path_text):
            if os.path.exists(self.full_path_text.replace('.txt', '_cypher.txt')):
                temp_file = self.full_path_text.replace('.txt', '_cypher.txt')
                os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии)
            file_cypher = self.full_path_text.replace('.txt', '_cypher.txt')
        else:
            mb.showerror("Ошибка", f'Путь {self.full_path_text} ссылается на несуществующий файл')
            
        key = int(self.key)
        # Открытие и работа с файлом_текстом
        with open(self.full_path_text, 'r', encoding='utf-8') as file_text:
            # Пробежка по всем строкам файла
            for line in file_text:
                # Строка_шифр для записи построчно в новый файл + ее обнуление
                cypher = ''
                cycle_index = 0
                tumbler = 1
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    # Проверка циклического индекса и тумблера на рост/уменьшение
                    if cycle_index <= 9 and tumbler == 1:
                        # Проверка на локализацию ползунка и перенос при необходимости
                        if 126 < ord(line[index]) + key + cycle_index < 1040:
                            index_cypher = ord(line[index]) + key + 913 + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        elif 1103 < ord(line[index]) + key + cycle_index:
                            index_cypher = ord(line[index]) + key - 1072 + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) + key + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        # Условие роста циклического индекса
                        cycle_index += 1
                    # Если индекс > 9, то тумблер в 0 и начало уменьшения индекса
                    else:
                        tumbler = 0
                        # Проверка на локализацию ползунка и перенос при необходимости
                        if 126 < ord(line[index]) + key + cycle_index < 1040:
                            index_cypher = ord(line[index]) + key + 913 + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        elif ord(line[index]) + key > 1103:
                            index_cypher = ord(line[index]) + key - 1072 + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) + key + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        # Условие уменьшения циклического индекса
                        cycle_index -= 1
                    # Если циклический индекс упал до 0, то пора начинать сначала
                    if tumbler == 0 and cycle_index == 0:
                        tumbler = 1
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                     cypher = cypher[:-1]
                print(cypher)
                # Запись строки в файл
                with open(file_cypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода
                    if os.stat(file_cypher).st_size == 0:
                        cypher += '2'
                    file_write.write(cypher + '\n')
            mb.showinfo("Ок", "Текст успешно зашифрован")

    def Multi_Cucle(self):

        '''
        :about_it
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
            Каждая пара цифр преобразуются в 16ти-ричную систему счисления.
        :return: ->file
            Название файла "Имя_файла_текса + _cypher.txt"
        '''

        # Проверка на наличие одноименного файла_шифра
        if os.path.exists(self.full_path_text):
            if os.path.exists(self.full_path_text.replace('.txt', '_cypher.txt')):
                temp_file = self.full_path_text.replace('.txt', '_cypher.txt')
                os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии - условие выше)
            file_cypher = self.full_path_text.replace('.txt', '_cypher.txt')
        else:
            mb.showerror("Ошибка", f'Путь {self.full_path_text} ссылается на несуществующий файл')
        key = int(self.key)
        # Открытие и работа с файлом_текстом
        with open(self.full_path_text, 'r', encoding='utf-8') as file_text:
            # Пробежка по всем строкам файла
            for line in file_text:
                # Строка_шифр для записи построчно в новый файл + ее обнуление
                cypher = ''
                next_iter = 0
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    if next_iter > 0:
                        next_iter -= 1
                        continue
                    # Проверка на локализацию ползунка и перенос при необходимости
                    # Условие для двух цифр подрят
                    elif 47 < ord(line[index]) < 58 and 47 < ord(line[index + 1]) < 58:
                        element = str(line[index]) + str(line[index + 1])
                        next_iter = 1
                        # Условие для 0xс в 0х0с
                        if int(element) < 15:
                            element = hex(int(element))
                            exception = str(element[0] + element[1]) + '0' + str(element[2])
                            cypher += exception
                        else:
                            cypher += hex(int(element))
                    elif 126 < ord(line[index]) + key < 1040:
                        index_cypher = ord(line[index]) + key + 913  # суть шифра
                        cypher += chr(index_cypher)
                    elif 1103 < ord(line[index]) + key:
                        index_cypher = ord(line[index]) + key - 1072  # суть шифра
                        cypher += chr(index_cypher)
                    else:
                        index_cypher = ord(line[index]) + key  # суть шифра
                        cypher += chr(index_cypher)
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                    cypher = cypher[:-1]
                print(cypher)
                # Запись строки в файл
                with open(file_cypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода
                    if os.stat(file_cypher).st_size == 0:
                        cypher += '3'
                    file_write.write(cypher + '\n')
            mb.showinfo("Ок", "Текст успешно зашифрован")

