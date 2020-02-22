print("---Счетчик б/у номеров---")
filename = input("Введите название, включив в него звездочку (*) на место цифры (не использованный файл - 0):")
number = input("Введите номер файла (который стоит на месте звездочки):")
try:
	if filename=="":
		fs = open("pcnsave", "r")
		filename = fs.read()
		fs.close()
	else:
		fs = open("pcnsave", "w")
		fs.write(filename)
		fs.close()
	f = open(filename.replace("*", number)+'.txt')
except:
	print("Поместите номера в файл "+filename++".txt.\nЗатем закройте программу и повторите попытку.\nНажмите enter для закрытия программы.")
	input()
	exit()
phones=[]


for line in f.readlines():
    phones.append(line)

print("Номеров было в \""+filename.replace("*", number)+'.txt" :'+str(len(phones)))
replace_count = input("Сколько номеров перместить в \""+filename.replace("*", str(int(number)+1))+'.txt\" и поместить в "Send.txt"?:')
replace_count=int(replace_count)
newlist=[]
for n in range(replace_count):
	newlist.append(phones[0])
	phones.pop(0)
f.close()

try:
	f = open(filename.replace("*", str(int(number)+1))+".txt", "a+")
	'''
	if f.read()[-1] != "\n":
		f.write("\n")
	for n in newlist:
		f.write(n)
	'''
finally:
	f.close()

try:
	f = open(filename.replace("*", str(number))+".txt", "w")
	for n in phones:
		f.write(n)
finally:
	f.close()
input()
