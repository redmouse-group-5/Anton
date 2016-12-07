stroka = input("Enter numbers via ','")
def step():
    spisok = stroka.split(',')
    for i in spisok:
    	n=int(i[0])
    	if n>=0:
    		n = n**(n-1)
    	elif n==1:
    		n = n**1
    	elif n<=0:
    		print('Input Error')
    	print (n)
    return (stroka)
new = step()
