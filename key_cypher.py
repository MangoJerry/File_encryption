import random, os

         
class Encryption:
    def __init__(self, full_path_text, key, number_cyph):
        #self.Cheak_Key(key)  # Вызов метода_проверки корректности ключа
        self.key = key
        if key > 159:
            self.key = key % 159
        with open ('key.txt', 'w', encoding='utf-8') as key_file:
            key_file.write(str(key))
        self.full_path_text = full_path_text
        self.number_cyph = number_cyph

    def AveMe(self):
        '''
        Для дешифратора:
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-126, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
        :return: ->file.txt
            Название файла "Имя_файла_текса" + "_cypher.txt"
        '''
        # Проверка на наличие файла
        print(self.key)
        print(self.full_path_text)
        print('Цезарь')
        print(self.number_cyph)
        
        # Проверка на наличие файла
        if os.path.exists(self.full_path_text.replace('.txt', '_cypher.txt')):
            temp_file = self.full_path_text.replace('.txt', '_cypher.txt')
            os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии - условие выше)
        file_cypher = self.full_path_text.replace('.txt', '_cypher.txt')
        # key - итак типа int
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
                    if ord(line[index]) + key > 126 and \
                            ord(line[index]) + key < 1040:
                        index_cypher = ord(line[index]) + key + 913  # суть шифра
                        cypher += chr(index_cypher)
                    elif ord(line[index]) + int(key) > 1103:
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
                    file_write.write(cypher + str(self.number_cyph) + '\n')


    def Сaesar_Сycle(self):
        '''
        Для дешифратора:
            Каждый элемент текста смещается на key символов по таблице ASCII.
            Адекватные символы находятся на позициях: 32-123, 1040-1103.
            От сюда следует зациклить перенос ползунка таблицы на 32 при
            индексе > 1103 и на 1040 при индексе > 123, чтобы индекс не попал
            в интервалы ...-31, 124-1039, 1104-...
            Данный шифратор отличается от AveMe тем, что на каждом вычислении
            индекса по таблице ASCII происходит циклическое увеличение/умень-
            шение на 1 числа сдвигов (растет до 10, затем падает до 0, затем
            снова растет и тд.)
        :return: ->file
            Название файла "Имя_файла_текса" + "_cypher.txt"
        '''
        print(self.key)
        print(self.full_path_text)
        key = self.key
        print('Цикл')
        print(self.number_cyph)
        # Проверка на наличие файла
        if os.path.exists(self.full_path_text.replace('.txt', '_cypher.txt')):
            temp_file = self.full_path_text.replace('.txt', '_cypher.txt')
            os.remove(temp_file)
        # Создание нового шифра (удаляя предыдущий при его наличии)
        file_cypher = self.full_path_text.replace('.txt', '_cypher.txt')
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
                        if 126 < ord(line[index]) + int(key) + cycle_index < 1040:
                            index_cypher = ord(line[index]) + int(key) + 914 \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        elif ord(line[index]) + int(key) > 1103:
                            index_cypher = ord(line[index]) + int(key) - 1073 \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) + int(key) \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        # Условие роста циклического индекса
                        cycle_index += 1
                    # Если индекс > 9, то тумблер в 0 и начало уменьшения индекса
                    else:
                        tumbler = 0
                        # Проверка на локализацию ползунка и перенос при необходимости
                        if 126 < ord(line[index]) + int(key) + cycle_index < 1040:
                            index_cypher = ord(line[index]) + int(key) + 914 \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        elif ord(line[index]) + int(key) > 1103:
                            index_cypher = ord(line[index]) + int(key) - 1073 \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        else:
                            index_cypher = ord(line[index]) + int(key) \
                                           + cycle_index  # суть шифра
                            cypher += chr(index_cypher)
                        # Условие уменьшения циклического индекса
                        cycle_index -= 1
                    # Если циклический индекс упал до 0, то пора начинать сначала
                    if tumbler == 0 and cycle_index == 0:
                        tumbler = 1
                print(cypher)
                # Запись строки в файл
                with open(file_cypher, "a", encoding="utf-8") as file_write:
                    file_write.write(cypher + str(self.number_cyph) + '\n')

#------------------Multi_Cucle метод не готов---------------------
    def Multi_Cucle(self):
        '''
        Для дешифратора:
            Каждый элемент ключа смещается на 1 символ по таблице ASCII,
            если текущий элемент и следующий за ним - цифры, то они
            шифруются в 16ричной системе счисления, если следующий элемент
            не цифра, то текущий просто смещается на 20 индексов по таблице
            ASCII. При этом для парных цифр фиксируется индекс с установкой
            одной из букв A-Z, а для одинарных a-z.
            В конце ставится номер шифра, в данном случае №3.
        Рс. Необходимо придумать алгоритм распознавания длины ключа, так
            как она может быть больше 9 и составлять двузначное число.
        :return: -> list
            ключ_шифр+(a-z+индексы/A-Z+индекс)+...+Len_key+№_шифратора
        '''
        cypher = []
        queue = ''
        for element in range(len(key)):
            if 47 < ord(key[element]) < 58:
                # Условие для двух цифр подрят
                if ((element + 2) <= len(key)) and (47 < ord(key[element + 1]) < 58):
                    index = str(key[element]) + str(key[element + 1])
                    # Условие для 0xс в 0х0с
                    if int(index) < 15:
                        index = hex(int(index))
                        exception = ''
                        exception = str(index[0] + index[1]) + '0' + str(index[2])
                        cypher.append(exception)
                    else:
                        cypher.append(hex(int(index)))
                    rand_ASCII = random.randint(65, 90)
                    queue += chr(rand_ASCII) + str(element)
                else:
                    index = ord(key[element]) + 20  # суть шифра
                    cypher.append(chr(index))
                    rand_ASCII = random.randint(97, 122)
                    queue += chr(rand_ASCII) + str(element)
            else:
                index = ord(key[element]) + 1  # суть шифра
                cypher.append(chr(index))
        cypher.append('~')
        cypher.append(str(queue))
        cypher.append(3)
        print(key)
        print(cypher)
        self.Save_file(cypher)


   # @staticmethod
   # def Cheak_Key(test_key):
   #     for index in range(len(test_key)):
   #         if ord(test_key[index]) > 57 or ord(test_key[index]) < 48:
   #             raise TypeError("Ключ должен быть целым числом")
   #     if int(test_key) <= 0 or int(test_key) > 150:
   #         raise ValueError("Ключ должен быть числом от 0 до 150. "
    #                         "Большее значение даст нерациональную нагрузку"
    #                         " на ЦП, а алгоритм зациклен на 150 единицах")


#full_path_key = 'key_1.txt'
'''
При наличии пути к файлу (вне текущего каталога)
раскомментить 3 строки ниже и удалить строку выше
dir = ''C:/Users/xxx''
key_file = ''key_1.txt''
full_path = os.path.join(dir, key_file)
Добавить "import os" в начале.
Сделать так для обоих файлов full_path_text = 'text_1.txt'
'''
#<<<<<<< HEAD
#with open('key.txt', 'r', encoding='utf-8') as file_key:
#    key = file_key.readline()
#temp = Encryption(key)
#  temp.AveMe()
#temp.Сaesar_Сycle()
#=======
#with open(full_path_key, 'r', encoding='utf-8') as file_key:
#    key = file_key.readline()
#temp = Encryption(key)
#temp.AveMe()
# temp.Сaesar_Сycle()
#>>>>>>> c2870f55e1ebb7cda007d6d84719faa2cc5affda
# temp.Multi_Cucle()
