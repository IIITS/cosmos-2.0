import os

def git_commit(directory):
	if os.path.isdir(directory):
		lst = os.listdir(directory)
		print lst
		for x in lst:
			if os.path.isfile(str(x)):
				os.system("git add %s/%s" %(directory,x))
				os.system("git commit -m \"Modified %s\"" % (str(x)))
			else:
				git_commit(directory+"/"+x)
	else:
		os.system("git add %s" %(directory))
		os.system("git commit -m \"Made changes\"")
					
fol = raw_input("Enter the location:")
git_commit(fol)
print "Added all files...\nPreparing for pushing to master\n"
#os.system("git push origin master")		
