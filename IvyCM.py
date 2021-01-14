from alive_progress import alive_bar
import os, time, random

class color():
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	BLUE1 = '\033[94m'
	MAGENTA = '\033[35m'
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	BLACK = '\033[1;30;48m'

def clean():
	os.system(['clear', 'cls'][os.name == 'nt'])

def banner():
	print(f'''{color.GREEN} _____            _____                _           __  __       _
|_   _|          / ____|              | |         |  \/  |     | |            
  | |_   ___   _| |     ___  _ __ ___ | |__   ___ | \  / | __ _| | _____ _ __ 
  | \ \ / / | | | |    / _ \| '_ ` _ \| '_ \ / _ \| |\/| |/ _` | |/ / _ \ '__|
 _| |\ V /| |_| | |___| (_) | | | | | | |_) | (_) | |  | | (_| |   <  __/ |   
|_____\_/  \__, |\_____\___/|_| |_| |_|_.__/ \___/|_|  |_|\__,_|_|\_\___|_|   
            __/ |                                                             
           |___/                  {color.BLUE1}github.com/weed-web    {color.BLACK}\n''')

combolist = []

def getuserfile():
	try:
		path_user = input(f'{color.YELLOW}Enter Path (Default: File Path) Of Your Users Text File: {color.BLACK}')
		if(path_user.endswith('.txt')):
			pass
		else:
			path_user = path_user + '.txt'
		read_user_file = open(path_user,'r').readlines()
		return read_user_file
	except OSError:
		print(f'{color.RED}File Not Found!{color.WHITE}')

def getpassfile():
	try:
		path_pss = input(f'{color.PURPLE}Enter Path (Default: File Path) Of Your Passwords Text File: {color.BLACK}')
		if(path_pss.endswith('.txt')):
			pass
		else:
			path_pss = path_pss + '.txt'
		read_pass_file = open(path_pss,'r').readlines()
		return read_pass_file
	except OSError:
		print(f'{color.RED}File Not Found!{color.WHITE}')

def getbetween():
	btw = input(f'{color.CYAN}Enter A Character That You Like To Put Between Them: {color.BLACK}')
	if(btw == ''):
		print(f'{color.RED}Character Not Found!')
	else:
		return btw

def makecombo(usernames, passwords, between):
	a = len(usernames)
	b = len(passwords)
	with alive_bar(a*b) as bar:
		for i in range(a):
			for j in range(b):
				combolist.append(f'{usernames[i]}{between}{passwords[j]}\n')
				k = random.sample(combolist, len(combolist))
				bar()
	file = open('combolist.txt','a')
	for i in range(0, a*b):
		file.write(k[i])

def start():
	try:
		clean()
		banner()
		usrs = getuserfile()
		while(usrs == None):
			usrs = getuserfile()
		usrs = [x.replace('\n', '') for x in usrs]
		usrs = [x.replace(' ', '') for x in usrs]
		clean()
		banner()
		pss = getpassfile()
		while(pss == None):
			pss = getpassfile()
		pss = [x.replace('\n', '') for x in pss]
		pss = [x.replace(' ', '') for x in pss]
		clean()
		banner()
		btwn = getbetween()
		while(btwn == None):
			btwn = getbetween()
		clean()
		banner()
		makecombo(usrs, pss, btwn)
		print(f'{color.MAGENTA}\nYour Combo List Is Ready!{color.WHITE}')
	except KeyboardInterrupt:
		print(f'{color.RED}\nExiting...{color.WHITE}')
		time.sleep(2)
		exit()

start()
