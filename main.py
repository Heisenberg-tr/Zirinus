__seviye__ = "8"


try:
	ZUS = open("webhook config/webhook-url.txt", "r")
	ZUS.close()
	

except:
	print("Finishing update...")
	print("%0")
	try:
		os.mkdir("webhook config")
	except:
		pass
	ZUSgt = open("webhook config/webhook-url.txt", "w")
	print("%25")
	ZUSgt.close()
	ZUSgt = open("webhook config/avatar-url.txt", "w")
	print("%50")
	ZUSgt.close()
	ZUSgt = open("webhook config/username.txt", "w")
	print("%75")
	ZUSgt.close()
	print("FINISHED SUCCESS")

print("Starting")



	

__versiyon__ = "0.8 GIT"
__maintain__ = True


try:
	import os
except:
	print("Corrupted python")
	exit()

try:
	import psutil
except:
	os.system("pip install psutil")
	import psutil

try:
	import os
	import socket
except:
	print("Python is corrupted")




try:
	import sockets
	import platform
except:
	os.system("pip install sockets")
	os.system("pip install platform")



try:
	bl = open("revision.txt", "r")
except:
	print("Cannot read revision file.")
	exit()

try:
	TOKENl = open("token.txt", "r").read().splitlines()
	KANALl = open("kanal.txt", "r").read().splitlines()
except:
	print("File not found")
	exit()
	

__checkrv__ = open("revision.txt", "r").read().splitlines()
if __checkrv__[0] != __seviye__:
	print("Make sure you re opened 'main.py' file in your terminal or code editor!")
	exit()
	


xsecimler = """
		_____________________________________
		|              |		     |
		|• 1           |	Spam  	     |
		|• 2           |	Webhook Spam |
		|• 3           |	Exit         |
		|______________|_____________________|
"""

secimler = """
		_____________________________________
		|              |		     |
		|• 1           |	Start 	     |
		|• 2           |	Exit         |
		|______________|_____________________|
"""





zirinus = """        

                                                
	,-------.,--.       ,--.                        
	`--.   / `--',--.--.`--',--,--, ,--.,--. ,---.  
	  /   /  ,--.|  .--',--.|      \|  ||  |(  .-'  
	 /   `--.|  ||  |   |  ||  ||  |'  ''  '.-'  `) 
	`-------'`--'`--'   `--'`--''--' `----' `----'  
                                                

"""

ckutu = """
	╭―――――――――――――――――――――――――――――――――――――――――――――――――――――――――╮
	│                                                         │
	│                   Discord : Zirin#0001                  │
	│                   Github : Heisenberg-tr                │
	│                Star the project if you liked!           │
	│                                                         │
	╰―――――――――――――――――――――――――――――――――――――――――――――――――――――――――╯
"""

kutu = """
┏───────────────────────────────────────
│																				 
│                        Discord : Zirin#0001
│
┗───────────────────────────────────────
"""


wspamch = """
		0|	Exit
		1|	Start
		2|	Guide
"""

textap = False

try:
	import pip
	import os
	import time
	import sys
	import threading
	import random
	import string
	import base64
	import string
except:
	print("Python is corrupted.")
	exit()
	


try:
	import colorama
	colorama.init()
	from colorama import Fore, Back, Style
	import requests
	import configparser
	from configparser import ConfigParser
	import shutil
except:
	os.system("pip install colorama")
	os.system("pip install requests")
	os.system("pip install configparser")
	os.system("pip install shutil")
	import colorama
	colorama.init()
	from colorama import Fore, Back, Style
	import requests
	import configparser
	from configparser import ConfigParser
	import shutil
	

hata = Fore.RED + Style.NORMAL + "[ ! ]" + Fore.YELLOW

def printc(s):
    print(s.center(shutil.get_terminal_size().columns))



def spam(token, chid, sure, mesaj):
	global textap
	if textap == False:
		print("SPAM > Started!")
		textap = True
	fail = False
	failauth = False
	ratelimit = False
	nochannelfound = False
	url = f"https://discord.com/api/v9/channels/{chid}/messages"
	print(Fore.RED + Style.BRIGHT)
	sure = int(sure)
#	print(" SPAM > START SUCCESFUL!")
	veri = {"content": mesaj}
	oturum = {"authorization":token}
	onS = False
	print(Fore.GREEN + Style.NORMAL)
	while True:
		time.sleep(sure)
		SPAMistek = requests.post(url=url, data=veri, headers=oturum)
		print(Fore.CYAN + Style.BRIGHT)
		if onS == False:
			print("Status		Status Code")
			onS=True
		if SPAMistek.status_code == 404:
			nochannelfound = True
			fail = True
		if SPAMistek.status_code == 429:
			ratelimit = True
		if SPAMistek.status_code == 401:
			failauth = True
			fail = True
		print(Fore.GREEN)
		if fail == True:
			print(Fore.RED)
			prdis = "Failed"
		else:
			prdis = "Success"
		print(f"{prdis}		{SPAMistek.status_code}")
		if nochannelfound == True:
			print("Double check your channel IDs (located in kanal.txt)")
		if failauth == True:
			print("Double check your tokens! (located in token.txt)")
		if ratelimit == True:
			print("Ratelimit dedected")
			print("Thread put on sleep for 5 seconds due to ratelimit protection")
			time.sleep(5)
		if fail == True:
			exit()
		
		

def webhookspam(mesaj, sure, webhookurl):
	try:
		config_username = open("webhook config/username.txt", "r").read()
		config_avatarurl = open("webhook config/avatar-url.txt", "r").read()
		config_webhookurl = open("webhook config/webhook-url.txt")
	except:
		print("Required files not found, try re-installing Zirinus")
		exit()
	print("Started success")
	veri = {
		"content" : mesaj,
		"username" : config_username,
		"avatar_url" : config_avatarurl
	}
	
	while True:
		time.sleep(sure)
		wspam = requests.post(webhookurl, json=veri)
		if wspam.status_code == 204:
			print("SUCCESS")
		if wspam.status_code == 404:
			print(Fore.RED)
			print("Check your webhook url")
			exit()
		if wspam.status_code == 429:
			print("Ratelimit dedected, putting thread in sleep for 3 seconds.")
			time.sleep(3)
		if wspam.status_code == 200:
			print("SUCCESS (not normal)")

def grs(length):
    letters = string.ascii_letters
    rstr = ''.join(random.choice(letters) for i in range(length))
    return rstr		

def threadgen0():
	print("LAUNCH >> 0")
	while True:
		gen0zrt = random.randint(1000000000000000000, 1090875122611191908)
		gen0ec = gen0zrt.encode("ASCII")
		gen0get = base64.b64encode(gen0ec)
		gen0take = gen0get.decode("ASCII")
		gen0take = gen0take[:-2]
		gen0take = gen0take + "."
		gen0load = grs(39)
		gen0bom = gen0take + gen0load
		
	
def threadgen1():
	print("LAUNCH >> 1")
def threadgen2():
	print("LAUNCH >> 2")
def threadgen3():
	print("LAUNCH >> 3")
def threadgen4():
	print("LAUNCH >> 4")
def threadgen5():
	print("LAUNCH >> 5")

def tokengen():
	tgdeploy0 = threading.Thread(target=threadgen0)
	tgdeploy1 = threading.Thread(target=threadgen1)
	tgdeploy2 = threading.Thread(target=threadgen2)
	tgdeploy3 = threading.Thread(target=threadgen3)
	tgdeploy4 = threading.Thread(target=threadgen4)
	tgdeploy5 = threading.Thread(target=threadgen5)
	
	
	

def tokengenUI():
	print(Fore.RED + Style.BRIGHT)
	temizle(zirinus)
	print(Style.NORMAL + Fore.GREEN)
	print("""
		0|	EXIT
		1|	START
	""")
	print()
	while True:
		secim = input("	>>>")
		if secim == "0":
			exit()
			break
		if secim == "1":
			tokengen()
			break
		print(f"{hata} {secim} is not a choice!")
	
		
		


def spamUI():
	print(Fore.RED + Style.BRIGHT)
	temizle(zirinus)
	print(Fore.CYAN + Style.BRIGHT)
	print(Fore.GREEN + Style.NORMAL)
	print("	0|	Exit")
	print("	1|	Start")
	print("	2|	Guide")
	while True:
		secim = input("		")
		if secim == "0":
			print(Style.BRIGHT + Fore.RED)
			temizle(zirinus)
			xirinus()
		if secim == "1":
			print("Please enter the message that you want to spam")
			mesaj = input("	>>>")
			print()
			print("Please enter delay (we recommend to not going below 1)")
			while True:
				try:
					sure = float(input("	>>>"))
					break
				except:
					print(f"{hata} Please enter a valid number!")
				
			
			print("if its stucked at starting, check if kanal.txt and token.txt file is not empty")
			print()
			print("Starting...")
			for token in TOKENl:
				for kanal in KANALl:
					threadSPAM = threading.Thread(target=spam, daemon=True, args=(token, kanal, sure, mesaj))
					threadSPAM.start()
		if secim == "2":
			print("""
	Guide:
				
		Open token.txt file in a text editor
		Then Write your token
		To use multiple tokens just go to new line
			
		Open kanal.txt file in a text editor
		Then write the channel ID you want to spam	
		To spam multiple channels just go to new line
		
			""")
	
	

		
def webhookspamui():
	print(Fore.RED + Style.BRIGHT)
	temizle(zirinus)
	print(Fore.GREEN)
	print(wspamch)
	print()
	while True:
		secim = input("	>>>")
		if secim == "0":
			exit()
			break
		if secim == "1":
			print("Please enter the message that you want to spam ")
			mesaj = input("	>>>")
			print()
			print("Please enter delay")
			try:
				sure = float(input("	>>>"))
			except:
				print(f"{hata} Please enter a valid number")
				print(Fore.GREEN)
			webhookurl = open("webhook config/webhook-url.txt", "r").read().splitlines()
			for whookurl in webhookurl:
				whookspam = threading.Thread(target=webhookspam, daemon=True, args=(mesaj, sure, whookurl))
				webhookspam.start()
		
		if secim == "2":
			print("""
				Guide
				
				To change username avatar etc go to webhook config directory
				
				to spam multiple webhooks just go to new line			""")
			






def xirinus():
	print(Fore.CYAN + Style.BRIGHT)
	print(Fore.GREEN + Style.NORMAL)
	print(xsecimler)
	while True:
		secim = input("		")
		if secim == "1":
			spamUI()
			break
		if secim == "2":
			print()
			webhookspamui()
			break
		if secim == "3":
			exit()
			break
		print(f"{hata} {secim} is not a choice!")






def temizle(yazi):
	if os.name == "NT":
		os.system("cls")
	if os.name == "posix":
		os.system("clear")
	if yazi != False:
		print(yazi)



def printf(yazi, sure):
	for i in yazi:
		time.sleep(sure)
		print(i, end='')
		sys.stdout.flush()
	print()


#ZUSgetlevel = open("revision.txt", "r").read().splitlines()


def baslangic(arg):
	ZUSgetlevel = open("revision.txt", "r").read().splitlines()
	temizle(False)
	if arg != False:
		print(Fore.CYAN + Style.BRIGHT)
		printf("> Checking For Updates", 0.07)
		try:
			ZUSSU = requests.get("https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/revision.txt")
		except:
			printf("> Cannot check updates, internet is no avalaible", 0.03
			)
			baslangic(False)
		ZUSdata = ZUSSU.text
		ZUSdata = str(ZUSdata)
		ZUSdata = ZUSdata[:1]
		if ZUSdata != ZUSgetlevel[0]:
			printf("> Update available...", 0.07)
			ZUSGC = requests.get("https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/changelog.txt")
			print()
			ZUSCdata = ZUSGC.text
			print(ZUSCdata)
			printf("> Updating Zirinus", 0.07)
			print("%0")
			ZUSget = requests.get("https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/main.py")
			ZUSdeploy = ZUSget.text
			print("%25")
			ZUSgetmain = open("main.py", "w")
			ZUSgetmain.write(ZUSdeploy)
			ZUSgetmain.close()
			print("%50")
			ZUSget = requests.get("https://raw.githubusercontent.com/Heisenberg-tr/Zirinus/main/revision.txt")
			ZUSdeploy = ZUSget.text
			print("%75")
			ZUSgetrevision = open("revision.txt", "w")
			ZUSgetrevision.write(ZUSdeploy)
			ZUSgetrevision.close()
			print("%100")
			print("Updating process is finished, please re open main.py file in your code editor or terminal")
			exit()
		else:
			printf("> Zirinus is on already newest version", 0.07)
		time.sleep(0.3)
	print(Fore.WHITE)
	temizle(False)
	print(Style.BRIGHT + Fore.RED)
	print(zirinus)
	print(Fore.WHITE + Style.BRIGHT)
	printc(ckutu)
	print(Fore.GREEN + Style.NORMAL)
	print(secimler)
	while True:
		secim = str(input("			"))
		if secim == "1":
			print(Fore.RED + Style.BRIGHT)
			temizle(zirinus)
			xirinus()
			break
		if secim == "2":
			ayarlar()
			break
		if secim == "3":
			exit()
		print(f"{hata} {secim} is not a choice")
		print(Fore.GREEN)

	

if __name__ == "__main__":
	baslangic(True)
else:
	print("This project cannot be imported as a module!")
	exit()
	