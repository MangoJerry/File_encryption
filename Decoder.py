import os


class Decoder:
    def __init__(self, key):
        self.key = key
        if int(key) > 159:
            self.key = int(key) % 159
        # Здесь нужно указать на имя файла, которое у Вас, Маргаритка, на вкладке кодирования
        file_cypher = 'text_1_cypher.txt'
        self.file_cypher = file_cypher
        # Определение метода шифрования из считывания символа в файле_шифре
        with open(file_cypher, 'r', encoding='utf-8') as file_number_methods:
            number_methods = file_number_methods.readline()[-2]
        if number_methods == '1':
            self.Dec_AveMe()
        elif number_methods == '2':
            self.Dec_Сaesar_Сycle()
        else:
            self.Dec_Multi_Cucle()

    def Dec_AveMe(self):
        '''
        :about_it
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
        :return: ->file.txt
            Название файла "Имя_файла_текса + _Name_шифратора"
        '''
        # Проверка на наличие одноименного файла_дешифра
        if os.path.exists(self.file_cypher.replace('.txt', '_recypher_AveMe.txt')):
            temp_file = self.file_cypher.replace('.txt', '_recypher_AveMe.txt')
            os.remove(temp_file)
        # Создание расшифрованного файла с названием метода
        file_recypher = self.file_cypher.replace('.txt', '_recypher_AveMe.txt')
        key = int(self.key)
        # Открытие и работа с файлом_шифром
        with open(self.file_cypher, 'r', encoding='utf-8') as file_text_cypher:
            # Пробежка по всем строкам файла
            for line in file_text_cypher:
                # Строка_дешифр для записи построчно в новый файл + ее обнуление
                recypher = ''
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    # Проверка на локализацию ползунка и перенос при необходимости
                    if 126 < ord(line[index]) - key < 1040:
                        index_recypher = ord(line[index]) - key - 913  # суть шифра
                        recypher += chr(index_recypher)
                    elif ord(line[index]) - int(key) < 32:
                        index_recypher = ord(line[index]) - key + 1072  # суть шифра
                        recypher += chr(index_recypher)
                    else:
                        index_recypher = ord(line[index]) - key  # суть шифра
                        recypher += chr(index_recypher)
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                    recypher = recypher[:-1]
                # Запись строки в файл
                with open(file_recypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода - удаляем
                    if os.stat(file_recypher).st_size == 0:
                        recypher = recypher[:-1]
                    file_write.write(recypher + '\n')

    def Dec_Сaesar_Сycle(self):
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
        # Проверка на наличие одноименного файла_дешифра
        if os.path.exists(self.file_cypher.replace('.txt', '_recypher_Сaesar_Сycle.txt')):
            temp_file = self.file_cypher.replace('.txt', '_recypher_Сaesar_Сycle.txt')
            os.remove(temp_file)
        # Создание расшифрованного файла с именем метода
        file_recypher = self.file_cypher.replace('.txt', '_recypher_Сaesar_Сycle.txt')
        key = int(self.key)
        # Открытие и работа с файлом_шифром
        with open(self.file_cypher, 'r', encoding='utf-8') as file_text:
            # Пробежка по всем строкам файла
            for line in file_text:
                # Строка_шифр для записи построчно в новый файл + ее обнуление
                recypher = ''
                # Индекс для зацикливания и тумблер для выбора направления вектора роста индекса
                cycle_index = 0
                tumbler = 1
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    # Проверка циклического индекса и тумблера на рост/уменьшение
                    if cycle_index <= 9 and tumbler == 1:
                        # Проверка на локализацию ползунка и перенос при необходимости
                        if 126 < ord(line[index]) - key - cycle_index < 1040:
                            index_cypher = ord(line[index]) - key - 913 - cycle_index  # суть шифра
                            recypher += chr(index_cypher)
                        elif ord(line[index]) - key - cycle_index < 32:
                            index_cypher = ord(line[index]) - key - cycle_index + 1072 # суть шифра
                            recypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) - key - cycle_index  # суть шифра
                            recypher += chr(index_cypher)
                        # Условие роста циклического индекса
                        cycle_index += 1
                    # Если индекс > 9, то тумблер в 0 и начало уменьшения индекса
                    else:
                        tumbler = 0
                        # Проверка на локализацию ползунка и перенос при необходимости
                        if 126 < ord(line[index]) - key - cycle_index < 1040:
                            index_cypher = ord(line[index]) - key - 913 - cycle_index  # суть шифра
                            recypher += chr(index_cypher)
                        elif ord(line[index]) - key - cycle_index < 32:
                            index_cypher = ord(line[index]) - key - cycle_index + 1072  # суть шифра
                            recypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) - key - cycle_index  # суть шифра
                            recypher += chr(index_cypher)
                        # Условие уменьшения циклического индекса
                        cycle_index -= 1
                    # Если циклический индекс упал до 0, то пора начинать сначала
                    if tumbler == 0 and cycle_index == 0:
                        tumbler = 1
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                     recypher = recypher[:-1]
                print(recypher)
                # Запись строки в файл
                with open(file_recypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода - удаляем
                    if os.stat(file_recypher).st_size == 0:
                        recypher = recypher[:-1]
                    file_write.write(recypher + '\n')

    def Dec_Multi_Cucle(self):
        '''
        :about_it
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
        :return: ->file.txt
            Название файла "Имя_файла_текса + _Name_шифратора"
        '''
        # Проверка на наличие одноименного файла_дешифра
        if os.path.exists(self.file_cypher.replace('.txt', '_recypher_Dec_Multi_Cucle.txt')):
            temp_file = self.file_cypher.replace('.txt', '_recypher_Dec_Multi_Cucle.txt')
            os.remove(temp_file)
        # Создание расшифрованного файла с названием метода
        file_recypher = self.file_cypher.replace('.txt', '_recypher_Dec_Multi_Cucle.txt')
        key = int(self.key)
        # Открытие и работа с файлом_шифром
        with open(self.file_cypher, 'r', encoding='utf-8') as file_text_cypher:
            # Пробежка по всем строкам файла
            for line in file_text_cypher:
                # Строка_дешифр для записи построчно в новый файл + ее обнуление
                recypher = ''
                next_iter = 0
                # Пробежка по каждому элементу строки
                for index in range(len(line)):
                    # Пропуск 3 следующих итераций при парном числе
                    if next_iter > 0:
                        next_iter -= 1
                        continue
                    # Условие для двух цифр подрят
                    elif line[index] == '0' and index + 4 <= len(line):
                        if line[index + 1] == 'x':
                            if 47 < ord(line[index + 2]) < 58:
                                # element = line[index:4] - не работает
                                element = line[index] + line[index+1] + line[index+2] + line[index+3]
                                recypher += str(int(element, 16))
                                next_iter = 3
                    # Проверка на локализацию ползунка и перенос при необходимости
                    elif 126 < ord(line[index]) - key < 1040:
                        index_recypher = ord(line[index]) - key - 913  # суть шифра
                        recypher += chr(index_recypher)
                    elif ord(line[index]) - int(key) < 32:
                        index_recypher = ord(line[index]) - key + 1072  # суть шифра
                        recypher += chr(index_recypher)
                    else:
                        index_recypher = ord(line[index]) - key  # суть шифра
                        recypher += chr(index_recypher)
                # Удаление символа переноса в конце каждой строки текста
                if ord(line[index]) == 10:
                    recypher = recypher[:-1]
                # Запись строки в файл
                print(recypher)
                with open(file_recypher, "a", encoding="utf-8") as file_write:
                    # Если файл пустой, то в конце первой строки индекс метода - удаляем
                    if os.stat(file_recypher).st_size == 0:
                        recypher = recypher[:-1]
                    file_write.write(recypher + '\n')


full_path = 'key_1.txt'
'''
При наличии пути к файлу (вне текущего каталога)
раскомментить 3 строки ниже и удалить строку выше
dir = ''C:/Users/xxx''
key_cypher_file = ''key_1_cypher.txt''
full_path = os.path.join(dir, key_cypher_file)
Добавить "import os" в начале
Сделать так для обоих файлов full_path_text = 'text_1.txt'
'''
with open(full_path, 'r', encoding='utf-8') as key_file:
    key = key_file.readline()
temp = Decoder(key)
# temp.Dec_Сaesar_Сycle()