import os.path

def txtadd(filename):
	try:
		if filename[-4:-1]+filename[-1] != '.txt':
			filename = filename + '.txt'
	finally:
		return filename


save = os.path.isfile("pcnsave")
if save == True:
	fs = open("pcnsave", "r")
	filename = txtadd(fs.read())
	fs.close()
	filename = txtadd(input("Введите название по шаблону или оставьте пустым для загрузки сохранения ("+filename+"):"))
else:
	filename = txtadd(input("Введите название, включив в него звездочку (*) на место цифры (не использованный файл - 0):"))
	number = input("Введите номер файла (который стоит на месте звездочки):")
try:
	if filename=="":
		fs = open("pcnsave", "r")
		filename = txtadd(fs.read())
		fs.close()
	else:
		fs = open("pcnsave", "w")
		fs.write(filename)
		fs.close()
	f = open(filename.replace("*", number)+'')
except:
	print("Поместите номера в файл "+filename+".\nЗатем закройте программу и повторите попытку.\nНажмите enter для закрытия программы.")
	input()
	exit(0)
phones=[]


for line in f.readlines():
    phones.append(line)

print("Номеров было в \""+filename.replace("*", number)+'" :'+str(len(phones)))
replace_count = input("Сколько номеров перместить в \""+filename.replace("*", str(int(number)+1))+'\" и поместить в "Send.txt"?:')
replace_count=int(replace_count)
newlist=[]
try:
	for n in range(replace_count):
		newlist.append(phones[0])
		phones.pop(0)
except:
	print('Нельзя переместить больше номеров, чем есть в файле "'+filename.replace("*", number)+'" '+'('+str(len(phones))+')')
	input('Нажмите enter для закрытия')
	exit(0)
finally:
	f.close()

try:
	f = open(filename.replace("*", str(int(number)+1))+"", "a+")
	fsn = open('Send.txt', "w")
	'''
	if f.read()[-1] != "\n":
		f.write("\n")
	'''
	for n in newlist:
		f.write(n)
		fsn.write(n)
finally:
	f.close()

try:
	f = open(filename.replace("*", str(number))+"", "w")
	for n in phones:
		f.write(n)
finally:
	f.close()
input('Нажмите enter для закрытия')
