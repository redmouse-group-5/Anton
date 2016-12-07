from fun_pack import func1
from fun_pack import func2
from fun_pack import func3



#Объявление переменной в которой хранится число:
x = int(input('Введите число от 1 до 9: '))

# Непосредственно блок условий
if 1<=x<=3:
	new = func1.first()
elif 4<=x<=6:
	new = func2.second(x)
elif 7<=x<=9:
	new = func3.third(x)
else:
	print('Ошибка ввода')