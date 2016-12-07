x = int(input('Enter number from 1 to 9: '))

if 1<=x<=3:
    s = input('Введите строку: ')
    n = int(input('Введите число повторов строки: ' ))
    i=1
    while i<=n:
	    i=i+1
	    print(s)

elif 4<=x<=6:
    m=int(input('В какую степень возвести число? '))
    proizv=x**m
    print (proizv)

elif 7<=x<=9:
	slog = 1
	while slog<=10:
		slog=slog+1
		x=x+1
		print(x)
		
else: print('Ошибка ввода')
