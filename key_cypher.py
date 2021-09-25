
class Encryption():
    def __init__(self, key):
        self.key = key
        self.AveMe()

    def AveMe(self):
        cypher = []
        for element in range(len(key)):
            index = ord(key[element]) + 3
            cypher.append(chr(index))
        cypher.append(1)
        self.Save_file(cypher)

    def Save_file(self, cypher):
        Save_file_Temp = open("Cypher_file.txt")
        with open("Cypher_file.txt", "w", encoding="utf-8") as filewrite: #...
            for index, symbol in enumerate(a_Z):
                filewrite.write(f'{symbol} {symbol_list[index]}\n')


    '''
    далее необходимо создать метод, вызываемый AveMe (и остальными шифровщиками)
    который будет записывать зашифрованный ключ в другой документ.
    Нужно содать виртуальный метод, что будет проверять правильность введенных символов в ключе
    '''


with open('key_1.txt', 'r', encoding='utf-8') as file_key:
    key = file_key.readline()
cyp = Encryption(key)
print(cyp)
