#-=coding-UTF-8=-
from fun_pack import func1
from fun_pack import func2
from fun_pack import func3

#Запись ввода в переменную
x= int(input('Введите число от 1 до 9:\n'))

#Объявление класса
class Main():
	"""Создать класс для первого задания"""

    #пихаем в конструктор наши условия
	def __init__(self, new):
		"""Создать конструктор, который будет в соответствии с параметром атрибута
        выполнять функцию класса"""
		if 1<=x<=3:
			#Производим вызов метода mfirst при соблюдении условия
			new = self.mfirst(x)
		elif 4<=x<=6:
			#Производим вызов метода msecond при соблюдении условия
			new = self.msecond(x)
		elif 7<=x<=9:
			#Производим вызов метода mthird при соблюдении условия
			new = self.mthird(x)
		else: print('Ошибка ввода!!!')
			
    #Методы, в которых вызываем функции из модулей
	def mfirst(self,x):
		"""Вывести все функции функциями класса"""
		atrFirst = func1.first(x)
		return atrFirst

	def msecond(self,x):
		"""Вывести все функции функциями класса"""
		atrSecond = func2.second(x)
		return atrSecond

	def mthird(self,x):
		"""Вывести все функции функциями класса"""
		atrThird = func3.third(x)
		return atrThird

#Создаем экземпляр класса и передаем в него наш х
obj = Main(x)