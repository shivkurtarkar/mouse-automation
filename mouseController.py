# import mouse
import pyautogui
import time
import threading


def dummy(str):
	pass

def dummyCommands():
	return []

# def click(x, y):
# 	curr = mouse.get_position()
# 	mouse.move(x, y, )
# 	mouse.click('left')
# 	mouse.move(curr[0], curr[1])

def click(x, y):
	curr = pyautogui.position()
	pyautogui.click(x, y)
	pyautogui.moveTo(curr[0], curr[1])


def mouseLoc():
	return pyautogui.position()


class Controller():
	def __init__(self, logCursor=False, start=False, logCallback=None, commandsCallback=None):
		self.logCursor =logCursor
		self.isRunning = start
		
		self.thread = None
		if logCallback is None:
			self.logCallback = dummy
		else:
			self.logCallback=logCallback

		if commandsCallback is None:
			self.getCommands = dummyCommands
		else:
			self.getCommands = commandsCallback

	
	def __del__(self):
		self.stopThread()

	def toggleCursorLogging(self, state=None):
		if state is not None:
			self.logCursor = state
		else:
			self.logCursor = not self.logCursor
		if self.logCursor:
			self.startThread()
		else:
			self.stopThread()
		return self.logCursor

	def cursorLoggingStatus(self):
		return self.logCursor

	def start(self):
		self.isRunning = True
		# start the thread
		self.startThread()

	def stop(self):
		self.isRunning = False
		#stop the thread
		self.stopThread()
	
	def status(self):
		return self.isRunning
	
	def startThread(self):
		print('starting thread')
		if self.thread is None or not self.thread.is_alive():
			self.thread = threading.Thread(target=self.loop, args=())
			self.thread.start()
		else :
			print('Thread already running')
	def stopThread(self):
		if self.thread is None:
			print('Thread not running')
		else:
			if self.isRunning or self.logCursor:
				print('cant terminate thread')
			else:
				print('thread status:',self.thread.is_alive())
				if self.thread.is_alive():
					#stop thread
					self.isRunning= False
					self.logCursor= False
					print('Waiting for thread to terminate')
					if self.thread is not None and self.thread.is_alive():
						self.thread.join()
					print('Thread terminated')
					self.thread =None
				else:
					print('Thread already terminated')
		
	def loop(self):
		print('executing loop')
		currentTime = time.time()
		lastFrameTime = currentTime
		FPS = 1
		
		while self.isRunning or self.logCursor:
			currentTime = time.time()
			self.update(currentTime)
			sleepTime = 1./FPS - (currentTime - lastFrameTime)
			lastFrameTime = currentTime
			if sleepTime > 0:
				time.sleep(sleepTime)
			print('sleepTime:',sleepTime)			
			
	def update(self, currentTime):		
		print('update: ', currentTime)
		
		# do clicks
		if self.isRunning:
			commands =self.getCommands()
			self.runScript(commands)

		if self.logCursor:
			self.logCurrentPos()

	def logCurrentPos(self):
		cord = mouseLoc()
		self.logCallback(' cursor cord: ' +str(cord))

	def runScript(self, commands):
		for each in commands:
			if each[0] == 'click':
				x,y = each[1]
				self.logCallback(' clicking '+str((x,y)))
				click(x,y)
			elif each[0] == 'keypress':
				print('keypress not supported')
			else:
				print('Unsupported action :', each[0])
		
