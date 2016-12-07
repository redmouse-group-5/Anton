#-_coding:utf-8_-

#Объявление переменной в которой хранится число:
x = int(input('Введите число от 1 до 9: '))

#Описание функции first()
def first(*args):
	"""Если введено от 1го до 3х вывести строку столько раз, сколько попросит пользователь"""
	stroka = input('Введите строку:\n')
	xnumber = int(input('Введите количество повторений:\n'))
	for i in range(xnumber):
		print(stroka)
	return(stroka)
#Описание функции second()
def second():
	"""Если введено от 4 до 6 - возвести число в степень, указанную пользователе"""
	m=int(input('В какую степень возвести число?:\n '))
	proizv=x**m
	print(proizv)
	return(proizv)
#Описание функции third()
def third(x):
	"""Если введено от 4 до 6 - возвести число в степень, указанную пользователе"""
	for i in range(10):
		x+=1
		print(x)

# Непосредственно блок условий
if 1<=x<=3:
	new=first()
elif 4<=x<=6:
	new= second()
elif 7<=x<=9:
	new = third(x)
else:
	print('Ошибка ввода')
