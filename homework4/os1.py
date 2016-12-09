#-=coding:UTF-8=-
"""Написать программу которая в интерактивном режиме просит ввести путь к папкам. Затем просит ввести название папки/файла.
   Затем если по заданному пути находится файл/папка то выводить:
   ее полный путь, размер, тип объекта (файл или директория), 
   дату создания изменения объекта."""

import os
import datetime

inpass = input('Введите путь к папкам:\n')
infile = input('Введите название папки/файла:\n')
outpass = inpass+'/'+infile

def modification_date(filename):
	ttime = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(ttime)

def filestats(filename):
	statinfo = os.stat(filename)
	return statinfo

if os.path.exists(outpass):
    print(modification_date(outpass),'\n',filestats(outpass),'\n', outpass)


elif infile == " ":
	if os.path.exists(outpass):
	    outpass = inpass
	    print(modification_date(outpass),filestats(outpass), outpass)