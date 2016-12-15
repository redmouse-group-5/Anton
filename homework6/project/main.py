#-=coding-UTF-8=-
from fun_pack import func1
from fun_pack import func2
from fun_pack import func3
import abc

#Мутим абстрактый класс
class FirstImput(metaclass=abc.ABCMeta):
	#Задаем ему атрибут
	x=0

#Объявление базового класса, наследуемого от абстрактного
class Main(FirstImput):
	"""Создать класс для первого задания"""			
    #Методы, в которых вызываем функции из модулей
	def mfirst(self):
		"""Вывести все функции функциями класса"""
		atrFirst = func1.first(self.x)
		return atrFirst

	def msecond(self):
		"""Вывести все функции функциями класса"""
		atrSecond = func2.second(self.x)
		return atrSecond

	def mthird(self):
		"""Вывести все функции функциями класса"""
		atrThird = func3.third(self.x)
		return atrThird

#Объявление конечного класса - наследника базового, в который пихаем конструктор и условия
class Final(Main):
	#Конструктор
	def __init__(self):
		#Переопределение абстрактного атрибута
		self.x = int(input('Введите число:\n'))

		#Блок условий
		if 1<=self.x<=3:
		    #Производим вызов метода mfirst при соблюдении условия
			new = self.mfirst()
		elif 4<=self.x<=6:
		    #Производим вызов метода msecond при соблюдении условия
			new = self.msecond()
		elif 7<=self.x<=9:
			#Производим вызов метода mthird при соблюдении условия
			new = self.mthird()
		else: print('Ошибка ввода!!!')


#Создаем экземпляр класса
obj = Final()