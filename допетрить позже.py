_string_ = input("Введите строку:\n")
sep = ' '			           #Символ разделения
_list_=_string_.split(sep)	   # разделение строки по символу sep
_index_ = [] 				   #Создание пустого списка
for i in _list_:               #Для каждого элемента в списке _list_
    _index_.append(len(i))     #Добавить в другой список количество букв в словах из списка _list_
    for n in _index_:          #Для каждого члена списка _index_
        if int(n) == max(_index_): #Если член списка является максимальным значением
            print(i)    #вывести соответствующее слово
