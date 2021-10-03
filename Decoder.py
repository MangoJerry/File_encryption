import os
import random


class Decoder:
    def __init__(self, key_cypher):
        self.key_cypher = key_cypher
        # Условия выбора метода декодировки
        if key_cypher[-1] == '1':
            self.Dec_AveMe()
        elif key_cypher[-1] == '2':
            self.Dec_Сaesar_Сycle()
        else:
            self.Dec_Multi_Cucle()

    def Dec_AveMe(self):
        '''
        Каждый элемент ключа смещается на 3 символа по таблице ASCII
        :return: ->list
            Ключ_шифр + №_шифратора
        '''
        key = []
        for element in range(len(key_cypher) - 1):
            index = ord(key_cypher[element]) - 3  # суть шифра
            key.append(chr(index))
        self.Save_file(key)

    def Dec_Сaesar_Сycle(self):
        '''
        Значения по ASCII от 33 до 126, потому при index < 33
        key_cypher[element] - element + (126 - 32) - т.е. зацикливается
        поиск елемента снова с конца (со 126).
        В конце ключ_шифр+Len_key+№_шифра. В нашем случае №2.
        :return: -> list
            Ключ_шифр + Len_key + №_шифратора
        '''
        key = []
        if (int(key_cypher[-2]) + 2) != len(key_cypher):
            len_key = int(str(key_cypher[-3] + key_cypher[-2]))
        else:
            len_key = key_cypher[-2]
        for element in range(len_key):
            if (ord(key_cypher[element]) - element) < 33:
                index = ord(key_cypher[element]) - element + (126 - 32)
                key.append(chr(index))
            else:
                index = ord(key_cypher[element]) - element  # суть шифра
                key.append(chr(index))
        self.Save_file(key)

    def Dec_Multi_Cucle(self):
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
        queue = ''
        key = []
        cypher_index = 0 #Индекс по шифру
        key_index = 0 #Индекс по ключу
        number_succ = 0 #Количество удачных поисков 16ричек
        len_key_imag = key_cypher.index('~')
        for second_index in range(len_key_imag):
            if cypher_index < len_key_imag:
                # print(key_cypher[len_key_imag  + 2 + number_succ + key_index], cypher_index)
                #print(key_index)
                print(key_cypher.rindex(str(key_index)))
                if str(key_index) in key_cypher:
                    if key_cypher.rindex(str(key_index)) > len_key_imag:
                        #print('dfgdg')
                        if (int(ord(key_cypher[len_key_imag + 1 + number_succ])) > 64 and
                            int(ord(key_cypher[len_key_imag + 1 + number_succ])) < 91):
                            print('dfgdg')
                            element = key_cypher[cypher_index:3]
                            key.append(int(str(element), 16))  # str мб лишнее
                            cypher_index += 5
                            key_index += 2
                            number_succ += 1
                        else:
                            element = ord(key_cypher[cypher_index]) - 20
                            key.append(chr(element))
                            key_index += 1
                            cypher_index += 1
                else:
                    element = ord(key_cypher[cypher_index]) - 1
                    key.append(chr(element))
                    key_index += 1
                    cypher_index += 1

        # print(len_key_imag + cypher_index + 3 + number_succ)

        self.Save_file(key)

    def Save_file(self, key):
        '''
        Метод записывает зашифрованный ключ одним из
        методов-шифраторов выше в файл в текущей дирекории
        с названием файла с ключом + _cypher
        :param cypher: -> list
        :return:
            file with name key_file + '_Decoder.txt'
        '''
        file_dec = full_path.replace('_cypher.txt', '_Decoder.txt')
        str_dec = ''
        for index in range(len(key)):
            str_dec += str(key[index])
        print(str_dec)
        with open(file_dec, "w", encoding="utf-8") as file_write:
            file_write.write(str_dec)


full_path = 'key_1_cypher.txt'
'''
При наличии пути к файлу (вне текущего каталога)
раскомментить 3 строки ниже и удалить строку выше
dir = ''C:/Users/xxx''
key_cypher_file = ''key_1_cypher.txt''
full_path = os.path.join(dir, key_cypher_file)
Добавить "import os" в начале 
'''
with open(full_path, 'r', encoding='utf-8') as key_cypher_file:
    key_cypher = key_cypher_file.readline()
# os.remove(full_path)
temp = Decoder(key_cypher)