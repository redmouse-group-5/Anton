xinput = input('Enter a string:\n')
xsep = input('Enter a separate symbol:\n')
def sep():
	spisok = xinput.split(xsep)
	for i in spisok:
		print(i," -- ", len(i))
	return (spisok)

new = sep()
