#-=coding-UTF-8=-
"""Написать программу которая заполняет случайным текстом строку.    
Попросить ввести  символы пользователя
Заменить регулярным выражением Это слово на ее 
ревертированное значение если это слово в начале или конце
это предложения"""

#импортируем всякое
import random
import re

#генерируем стиринговый список с рандомными символами
xlist = str(random.sample('abcdefghijklmnopqrstuvwxyz1234567890',36))

#удаляем лишние сиволы
xstring = xlist[2::5]

#выводим для удобства проверки
print (xstring)
xinput = input('Введите символы:\n')

#если введенное значение содержится в строке, то выводим ее инвертированное значение
if re.findall(xinput, xstring):
	print (xinput[::-1])



