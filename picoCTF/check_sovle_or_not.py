#!/usr/bin/python3

import os 
import sys
try:
	import termcolor
except:
	os.system("pip install termcolor")




os.system("cls")
#     ✓    ✘ 

base_dir = []
for i in os.listdir():
	if i == sys.argv[0][2:]:
		continue
	base_dir.append(i)


s = 1
max_space = 40
for i in base_dir:
	print(f"\t\t\t{termcolor.colored(i,'yellow')}")
	for x in os.listdir(f"{i}"):
		len_dir = len(x)
		if x == sys.argv[0][2:]:
			continue
		if os.path.exists(f"{i}/{x}/solve.txt"):
			print(termcolor.colored(s,"cyan"),termcolor.colored(")","magenta"),termcolor.colored(x,"green")," "* (max_space - len_dir),termcolor.colored("✓","green"))
		else:
			print(termcolor.colored(s,"cyan"),termcolor.colored(")","magenta"),termcolor.colored(x,"green")," "* (max_space - len_dir),termcolor.colored("✘","red"))

		s += 1
	print("--------------------------------------------")
	s = 1
