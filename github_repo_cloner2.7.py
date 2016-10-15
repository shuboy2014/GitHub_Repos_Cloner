# Author : Shubham Aggarwal
# Handle : shuboy2014
# python version : 2.7.12
# Date : 15-10-2016

import requests
import zipfile
import StringIO
import sys

check_username_url = "https://api.github.com/users/"
repos_url = "https://api.github.com/users/"
repo_zip_url= "https://github.com/"

def checkUsername(username=None):
	if username:
		url = check_username_url + username
		response = requests.get(url)
		user = response.json()
		if user.get("login",""):
			return True
		else:
			return False
	else:
		return False

def getRepos(username=None):
	print "Getting your Repository List"
	if username:
		try:
			url = repos_url + username + "/repos"
			response = requests.get(url)
			repos = response.json()
			return repos
		except Exception as e:
			print e
	else:
		return "Oops ! you don't have pass your username ."
	

def saveRepos(username, repos=None):
	if repos:
		try:
			for repo in repos:
				reponame = repo["name"]
				print reponame + " downloading...."
				repozipurl = repo_zip_url + username + "/" + reponame + "/archive/master.zip"
				get_repo_zip = requests.get(repozipurl)
				repozipfile = zipfile.ZipFile(StringIO.StringIO(get_repo_zip.content))
				print "Extracting " + reponame + "...."
				repozipfile.extractall()
				print reponame + "downloading Complete :)"
			return True
		except Exception as e:
			print e
			return False
	else:
		return "Oops! Your don't have any Repository"


def main():
	username = raw_input("Enter your Github Profile username : ")
	if checkUsername(username):
		repos = getRepos(username)
		status = saveRepos(username=username, repos=repos)
		if status:
			print "Done"
		else:
			print "Oops ! something went wrong :("
	else:
		print "Username does not exist !"

if __name__ == "__main__":
	main()
	sys.exit()
