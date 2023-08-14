import os 

try:
	import termcolor
except:
	os.system("pip install termcolor")
	print("Please reRun this code")


def list_directories(path):
    for root, dirs, files in os.walk(path):
        if any(file.endswith('.md') for file in files):
            print(root)

list_directories('.')

