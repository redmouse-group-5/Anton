#-=Coding-UTF-8=-

print("Общество в начале XXI века")
age = int(input("введите свой возраст: "))

class Main():
	def __init__(self,age):
		if 0<=age<=7:
			print("Вам в детский сад")
		elif 7<=age<=18:
			print ("вам в школу")
		elif 18<=age<=25:
			print("Вам в профессиональное учебное заведение")
		elif 25<=age<=60:
			print("Вам на работу")
		elif 60<=age<=120:
			print("Вам предоставляется выбор")
		else:
			print("Ошибка!"*5)
new = Main(age)