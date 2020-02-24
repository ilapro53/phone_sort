import clipboard
import str_edit as stredit

def txtadd(filename):
	try:
		if filename[-4:-1]+filename[-1] != '.txt':
			filename = filename + '.txt'
	finally:
		return filename

print('---Auto Phone Clip---')
file = txtadd(input('Название файла:'))
f = open(file, "a+")
f.close()
print('Файл "'+file+'" открыт\n')



run = True
clip = clipboard.paste()
clip2 = clipboard.paste()

print('Начало:')
while run == True:
	clip2 = clip
	clip = clipboard.paste()
	if clip != clip2:
		paste = clip
		paste = paste.replace("-", "")
		paste = paste.replace(" ", "")
		paste = paste.replace("\n", "")
		paste = paste.replace(")", "")
		paste = paste.replace("(", "")
		paste = paste.replace("\u2011", "")
		if paste[0:1] == "8":
			paste = stredit.change(paste, 1 , "+7")

		f = open(file, "a+")
		f.write(paste+'\n')
		print('Записано: '+paste)
		f.close()
