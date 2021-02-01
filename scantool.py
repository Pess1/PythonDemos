import datetime
import os

def main():
	serverIp = '0.0.0.0'
	serverNames = ['test_server1', "test_server2", "test_server3"]

	i = 0

	for serverName in serverNames:
		created = datetime.datetime.now()
		file = serverName + "_" + str(created.year) + "-" + str(created.month) + "-" + str(created.day) + "_" + created.strftime("%X") + ".txt"

		with open(file, 'w') as output:

			commandOutput = os.popen('ls -l').read()
			output.write(commandOutput)

main()
