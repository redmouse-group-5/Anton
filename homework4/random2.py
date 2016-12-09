
"""Написать программу которая заполняет случайным текстом строку.    
Попросить ввести  символы пользователя
Заменить регулярным выражением Это слово на ее 
ревертированное значение если это слово в начале или конце
это предложения"""

import random
import re

stroka = 'abcdefghijklmnopqrstuvwxyz'
rand = random.shuffle(stroka,[rand])
xinput = input('Введите символы:\n')

if re.match(xinput, rand):
	print (xinput[::-1])


