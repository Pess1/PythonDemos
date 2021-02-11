import datetime
import subprocess
import sys
import re

def main():
	serverIps = ['0.0.0.0']
	userName = 'uname'

	for serverIp in serverIps:

		ssh = subprocess.Popen(['ssh', '-t', userName + '@' + serverIp, "dpkg -l | grep -E 'mariadb|postgresql|nodejs'",],
			shell=False,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
		results = ssh.stdout.readlines()

		if not results:
			error = ssh.stderr.readlines()
			print('ERROR: %s' % error, sys.stderr)
		else:
			outputArr = []
			dict = {"depName": "", "depVer": ""}
			for result in results:
				formattedResult = str(result)[6:72].strip()
				objectData = re.sub("\s+", "|", formattedResult).split("|")
				dict["depName"] = objectData[0]
				dict["depVer"] = objectData[1]
				outputArr.append(dict)
			serverDict = {"serverIp": serverIp, "depInfo": outputArr}
			print(serverDict)
main()
