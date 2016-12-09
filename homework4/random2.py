#-=coding-UTF-8=-
"""Написать программу которая заполняет случайным текстом строку.    
Попросить ввести  символы пользователя
Заменить регулярным выражением Это слово на ее 
ревертированное значение если это слово в начале или конце
это предложения"""

#импортируем всякое
import random
import re

#генерируем список с рандомными символами
xlist = random.sample('abcdefghijklmnopqrstuvwxyz1234567890',36)

xstring = ''
#делаем его стрингом
xstring.join(xlist, sep=None)

print (xstring)
xinput = input('Введите символы:\n')

if re.match(xinput, xstring):
	print (xinput[::-1])



