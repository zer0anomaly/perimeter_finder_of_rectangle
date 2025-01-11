Lenght = int(input("Lenght ?:"))
Width = int(input("Width ?:"))

def finder(Lenght, Width):
	global result
	result = 2 * (Lenght + Width)
	
finder(Lenght, Width)	
print(result)