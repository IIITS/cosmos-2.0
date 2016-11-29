import os

def git_commit(directory):
	
	lst = os.listdir(directory)
	print lst
	for x in lst:
		#if os.path.isfile(str(x)):
			os.system("git add %s/%s" %(directory,x))
			os.system("git commit -m \"Adding gp\"")
			print "Added %s" % (x)

git_commit("gp")
print "Added all files...\nPreparing for pushing to master\n"
#os.system("git push origin master")		