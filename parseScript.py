import re

def readFile(fileName):
	try:
		with open(fileName) as f:
			return f.read()
	except Exception as e:
		print("Error occurred: ", e)

def parseScript(scriptTxt):
	commandTxt = scriptTxt.split('\n')

	commandList = parseCommands(commandTxt)
	print(commandList)
	return commandList


def parseCommad(commandStr):
	try:
		if commandStr is None:
			return None
		commandStr = re.sub(' +', ' ', commandStr)
		c = commandStr.split(' ', 1)
		action= c[0]
		if 'click' in action:
			if len(c)>1:
				info = c[1].strip('( )').split(',')
				coords = [int(each) for each in info]
				if len(coords) == 2:
					return ['click', coords]
			return None
		elif 'keypress' in action:
			key = ('ALT')
			return ['keypress', key]
		else:
			return None
	except Exception as e:
		print('Exception occurred ', e)


def parseCommands(commandTxt):
	commandList =[]
	for each in commandTxt:
		command = parseCommad(each)
		if command is not None:
			commandList.append(command)

	# commandList = [
	# 	['click', (2003, 83)],
	# 	['keypress', 'ALT'],
	# 	['click', (2003, 83)]
	# ]
	return commandList