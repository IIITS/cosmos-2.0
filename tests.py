import os

def git_commit(directory):
	print "Checking for %s" %(directory)
	lst = os.listdir(directory)
	for x in lst:
		if os.path.isdir(str(x)):
			print "GIT COMMIT FOR %s " % (x)
			git_commit(directory+"/"+x)
		if os.path.isfile(str(x)):
			os.system("git add %s" %(x))
			os.system("git commit -m \"Adding gp\"")
			print "Added %s" % (x)

git_commit("gp")
print "Added all files...\nPreparing for pushing to master\n"
os.system("git push origin master")		