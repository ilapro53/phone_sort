import str_edit as stredit

def txtadd(filename):
	try:
		if filename[-4:-1]+filename[-1] != '.txt':
			filename = filename + '.txt'
	finally:
		return filename

def txtremove(filename):
	try:
		if filename[-4:-1]+filename[-1] == '.txt':
			filename = filename[0:len(filename)-4]
	finally:
		return filename

print("---Очиститель номеров---")
filename = txtadd(input("Введите название файла:"))
try:
	f = open(filename)
except:
	print("Поместите номера в файл "+filename+".\nЗатем закройте программу и повторите попытку.\nНажмите enter для закрытия программы.")
	input()
	exit()
phones=[]
for line in f.readlines():
    phones.append(line)
print("Номеров было до обработки:"+str(len(phones)))
for n in range(len(phones)):
	phones[n] = phones[n].replace("-", "")
	phones[n] = phones[n].replace(" ", "")
	phones[n] = phones[n].replace("\n", "")
	phones[n] = phones[n].replace(")", "")
	phones[n] = phones[n].replace("(", "")
	if phones[n][0:1] == "8":
		phones[n] = stredit.change(phones[n], 1 , "+7")
phones = list(set(phones))
print("Номеров стало после обработки:"+str(len(phones)))
f = open(txtremove(filename)+'_output.txt', "w+")
for n in phones:
	f.write(n+"\n")
f.close()
input("Номера телефонов из "+filename+" обработаны и сохранены в "+txtremove(filename)+"_output.txt")