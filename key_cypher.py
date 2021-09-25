# import os


class Encryption():
    def __init__(self, key):
        self.key = key

    def AveMe(self):
        cypher = []
        for element in range(len(key)):
            index = ord(key[element]) + 3 # суть шифра!!!
            cypher.append(chr(index))
        cypher.append(1)
        print(key)
        print(cypher)
        self.Save_file(cypher)

    def Сaesar_Сycle(self):
        cypher = []
        for element in range(len(key)):
            if (ord(key[element]) + element) > 126:
                '''
                диапозон доступных значений по таблице ASCII 33-126,
                потому, если значение больше 126, то (Temp - (126 - 33)).
                Если такое сучается, то добавить в конце индекс циклического
                символа, в конце зафиксировать количество изменений
                (текущее len - len_kay) и при дешифровке учесть, что
                последний символ - номер шифра, а предыдущие за ним - номера
                сиволов, прошедшие круг при шифровании.
                ord(key[element]) + element - 93
                '''

            index = ord(key[element]) + element  # суть шифра!!!
            cypher.append(chr(index))
        cypher.append(2)
        print(key)
        print(cypher)
        self.Save_file(cypher)

    def Save_file(self, cypher):
        file_cypher = full_path.replace('.txt', '_cypher.txt')
        str_cypher = ''
        for index in range(len(cypher)):
            str_cypher += str(cypher[index])
        print(str_cypher)
        with open(file_cypher, "w", encoding="utf-8") as file_write:
            file_write.write(str_cypher)


full_path = 'key_1.txt'
('При наличии пути к файлу (вне текущего каталога)\n'
 'раскомментить 3 строки ниже и удалить строку выше\n'
 'dir = ''C:/Users/xxx'' \n'
 'key_file = ''key_1.txt'' \n'
 'full_path = os.path.join(dir, key_file) \n')
with open(full_path, 'r', encoding='utf-8') as file_key:
    key = file_key.readline()

temp = Encryption(key)
temp.AveMe()
