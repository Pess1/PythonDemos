import datetime
import subprocess
import sys
import re

def main():
	serverIps = ['0.0.0.0']
	userName = 'uname'
	#This could later be used if Ip's were retrieved from an API
	for serverIp in serverIps:

		ssh = subprocess.Popen(['ssh', '-t', userName + '@' + serverIp, "dpkg -l | grep -E 'mariadb|postgresql|nodejs'",],
			shell=False,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
		results = ssh.stdout.readlines()
		# If result array is empty it is a falsy value
		if not results:
			error = ssh.stderr.readlines()
			print('ERROR: %s' % error, sys.stderr)
		else:
			#List to save the dicts containing dependency name and version
			outputArr = []
			#The before mentioned dict
			dict = {"depName": "", "depVer": ""}
			#Looping through the lines retrieved by the command
			#TODO: Create a function out of the formatter
			for result in results:
				#Select only interesting part of the string and remove leading and trailing whitespace
				formattedResult = str(result)[6:72].strip()
				#Add the depname and version to dict
				objectData = re.split("\s+", formattedResult)
				dict["depName"] = objectData[0]
				dict["depVer"] = objectData[1]
				outputArr.append(dict)
			#Creating the final output with serverIp and depInfo
			serverDict = {"serverIp": serverIp, "depInfo": outputArr}
			print(serverDict)
main()
