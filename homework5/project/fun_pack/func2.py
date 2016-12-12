#Описание функции second()
def second(x):
	"""Если введено от 4 до 6 - возвести число в степень, указанную пользователе"""
	m=int(input('В какую степень возвести число?:\n '))
	proizv=x**m
	print(proizv)
	return(proizv)