#!/usr/bin/python3

import os 
import sys
try:
	import termcolor
except:
	os.system("pip install termcolor")




os.system("cls")

#     ✓    ✘ 

x = 1
max_space = 40
for directory in os.listdir():
	len_dir = len(directory)
	if directory == sys.argv[0][2:]:
		continue
	if os.path.exists(f"{directory}/solve.txt"):
		print(termcolor.colored(x,"cyan"),termcolor.colored(")","magenta"),termcolor.colored(directory,"green")," "* (max_space - len_dir),termcolor.colored("✓","green"))
	else:
		print(termcolor.colored(x,"cyan"),termcolor.colored(")","magenta"),termcolor.colored(directory,"green")," "* (max_space - len_dir),termcolor.colored("✘","red"))

	x += 1
