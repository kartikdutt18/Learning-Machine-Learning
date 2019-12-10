#	Automating Merge of Gitub Repo
import os
import sys
import argparse


def makedir(path):
	if(not os.path.exists(path)):
		os.mkdir(path)
		"Path Created"
	else:
		"Path exists"


def mergeRepos(userName, baseRepoPath, nRepo):
		repoList = []
		os.chdir(baseRepoPath)
		print("Enter RepoNames")
		for i in range(nRepo):
    			repoList.append(str(input()))

		for repoName in repoList:
				remoteAdd = "git remote add -f "+repoName + \
					" git@github.com:"+userName+"/"+repoName+".git"
				merge = "git merge "+repoName+"/master --allow-unrelated-histories"
				try:
					os.system(remoteAdd)
					print("Remote Addition Completed")
					os.system(merge)
				except:
					print("Merge with ", repoName, " Failed")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog=None, usage=None)
	parser.add_argument('userName', type=str, help="Add your username")
	parser.add_argument('-baseRepoPath', type=str, default="./" ,help="Add your Base Repo-Path Local default=pwd")
	parser.add_argument('-nRepo', type=int, default=1,help="Number of Repos to be merged with default=1")
	args = parser.parse_args()
	mergeRepos(args.userName,args.baseRepoPath,args.nRepo)
	print(8*'*',"\t Repos Merged \t",8*'*')

