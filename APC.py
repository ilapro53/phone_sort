import clipboard
import str_edit as stredit

print('---Auto Phone Clip---')
file = input('Название файла:')
if file[-4:-1]+file[-1] != '.txt':
	file = file + '.txt'



run = True
clip = clipboard.paste()
clip = clipboard.paste()

print('Начало:')
while run == True:
	clip2 = clip
	clip = clipboard.paste()
	if clip != clip2:
		paste = clip.replace("-", "")
		paste = paste.replace(" ", "")
		paste = paste.replace("\n", "")
		paste = paste.replace(")", "")
		paste = paste.replace("(", "")
		if paste[0:1] == "8":
			paste = stredit.change(paste, 1 , "+7")

		f = open(file, "a+")
		f.write(paste+'\n')
		print('Записано: '+paste)
		f.close()
