from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import time

from  mouseController import *

maxListLen = 20
mc = None

def log(txt):
	now = datetime.now()
	log = str(now)+' :: '+txt
	logList.insert(END, log)
	
	while logList.size() >= maxListLen:
		logList.delete(0)
	logList.see(END)

mc = Controller(callback =log)

def toggleState():
	print('test')
	print(actionBtnTxt.get())
	isRunning = (actionBtnTxt.get()=='Start')
	if isRunning:
		mc.start()
	else:
		mc.stop()
	btnTxt =  'Stop' if isRunning else 'Start'
	actionBtnTxt.set(btnTxt)

def reloadScript():
	print('reloading script')

def clearLogs():
	print('clearing Logs')
	logList.delete(0,END)

def logCursor():
	loggingState =  mc.toggleCursorLogging()
	print('logging cursor ', loggingState)
	txt = 'Log Cursor Cords' + (' (ON)' if loggingState else '')
	logCursorLocBtnTxt.set(txt)

def on_closing():
	print('close event..')
	mc.toggleCursorLogging(False)
	mc.stop()
	mc.stopThread()
	root.quit()

root = Tk()
root.title('Automate')

root.columnconfigure(2,weight=1)
root.rowconfigure(2,weight=1)

root.protocol("WM_DELETE_WINDOW", on_closing)

row=0
# Parent widget for buttons
btnFrame = Frame(root)
btnFrame.grid(row=row, column=0, sticky=W+E)

actionBtnTxt = StringVar()
actionBtn = Button(btnFrame, textvariable=actionBtnTxt, command=toggleState)
actionBtnTxt.set('Start')
actionBtn.grid(row=0,column=0, padx=(10), pady=10)

reloadScriptBtn= Button(btnFrame, text='Reload Script', command=reloadScript)
reloadScriptBtn.grid(row=0, column=1, padx=(10), pady=10)

clearLogsBtn = Button(btnFrame, text='Clear Logs',command=clearLogs)
clearLogsBtn.grid(row=0, column=2, padx=(10), pady=10)

logCursorLocBtnTxt = StringVar()
logCursorLocBtn = Button(btnFrame, textvariable=logCursorLocBtnTxt,command=logCursor)
logCursorLocBtnTxt.set('Log Cursor Cords')
logCursorLocBtn.grid(row=0, column=3, padx=(10), pady=10)

row=row+1
# script frame
scriptFrame = LabelFrame(root, text='Script', padx=5, pady=5)
scriptFrame.grid(row=row, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

scriptFrame.columnconfigure(0, weight=1)
scriptFrame.rowconfigure(0,  weight=1)

scriptTxt = ScrolledText(scriptFrame, wrap=WORD, height=7)
scriptTxt.grid(row=0,column=0, sticky=E+W+N+S)

row=row+1
# Log frame
logFrame = LabelFrame(root, text='Logs', padx=5, pady=5)
logFrame.grid(row=row, column=0, columnspan=3, padx=10,pady=10, sticky=E+W+N+S)

logFrame.columnconfigure(0, weight=1)
logFrame.rowconfigure(0,  weight=1)

logScrollbar = Scrollbar(logFrame)
logList = Listbox(logFrame, yscrollcommand = logScrollbar.set)
logList.grid(row=0,column=0, sticky=E+W+N+S)
logScrollbar.grid(row=0, column=1, sticky=E+W+N+S)
logScrollbar.config(command=logList.yview)

root.mainloop()
