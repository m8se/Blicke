from urllib import *
from random import choice
from time import sleep

import re


url="http://www.hacker.org/challenge/misc/d/cave.php?name=jarCrack&password=1df1fe03"
logfile=open("log.txt","a")

def iter():
	
	global url
	resp=urlopen(url);
	print url
	text=resp.read()
	
	logfile.write(text)
	dungeon_level=re.findall(r'Level (\d+)',text)[0]
	level=re.findall(r'td>(\d+)',text)[0]
	print "Dungeon Level:"+dungeon_level
	print "Level:"+level	

	#print text


	urls = re.findall(r'href=[\'"]?([^\'" >]+)', text)

	next="";
	

	#Test if attack!
	if "cave.php?attack=1" in urls:	
		health=re.findall(r'td>(\d{2,})',text);
		print health[0]
		if(health<30 or len(health)==0):
			next="potion=0"	
		else:
			next="attack=1"

	map_routes= re.findall(r'm=([nswed])', text)
	if len(map_routes)!=0:
		print map_routes
		"""		
		if "d" in map_routes:
			if(int(dungeon_level)+3<int(level)):
				next="m=d"
			else:
				map_routes.remove("d")
		"""
		if "d" in map_routes:
			map_routes.remove("d")
			if(int(level)>int(dungeon_level)+2):
				"m=d"
		ch=choice(map_routes)
		print ch
		next="m="+ch
		
	if "cave.php?tres=1" in urls:
		next="tres=1"

	url="http://www.hacker.org/challenge/misc/d/cave.php?"+next+"&name=jarCrack&password=1df1fe03"

while True:
	iter() 
