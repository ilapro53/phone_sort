import str_edit as stredit
print("---Очиститель номеров---")
filename = input("Введите название файла:")
try:
	f = open(filename+'.txt')
except:
	print("Поместите номера в файл "+filename+".txt.\nЗатем закройте программу и повторите попытку.\nНажмите enter для закрытия программы.")
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
f = open(filename+'_output.txt', "w+")
for n in phones:
	f.write(n+"\n")
f.close()
input("Номера телефонов из "+filename+".txt обработаны и сохранены в "+filename+"_output.txt")