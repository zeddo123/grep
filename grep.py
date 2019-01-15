import sys
import re
import os

def rep (arg,file,n=False,v=False,r=False):
	if(file != None):
		file_object = open(file,'r')
		i = 0
		try:
			for line in file_object:
				i += 1
				if(v):
					if not(arg in line):
						if(n):
							print("{0}:{1}".format(i,line),end="")
						else:
							print("{0}".format(line),end="")
				else:
					if (arg in line):
						if(n):
							print("{0}:{1}".format(i,line),end="")
						else:
							print("{0}".format(line),end="")
		except UnicodeDecodeError:
			print("{0} unreadable".format(file))
		file_object.close()
	else:
		for p,d,f in os.walk(os.getcwd()):
			for i in f:
				rep(arg,p+'/'+i,n,v,r)
try:
	if(re.match(r'-\w+',sys.argv[1])):
		
		v = 'v' in sys.argv[1]
		r = 'r' in sys.argv[1]
		n = 'n' in sys.argv[1]

		try :
			arg = sys.argv[2]	
		except IndexError:
			print("no arg found")
			exit()
		
		if(r):
			try:
				ch = sys.argv[3]
				print("too many args")
				exit()
			except IndexError:
				file = None
		else:
			try :
				file = sys.argv[3]	
			except IndexError:
				print("no file name found")
				exit()
	else:
		arg = sys.argv[1]
		file = sys.argv[2]
		v = False
		r = False
		n = False
except IndexError:
	print("number of arguments is too short")
	exit()

rep(arg,file,n,v,r)