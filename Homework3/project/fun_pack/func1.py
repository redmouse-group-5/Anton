#Описание функции first()
def first(*args):
	"""Если введено от 1го до 3х вывести строку столько раз, сколько попросит пользователь"""
	stroka = input('Введите строку:\n')
	xnumber = int(input('Введите количество повторений:\n'))
	for i in range(xnumber):
		print(stroka)
	return(stroka)