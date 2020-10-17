from tkinter import *
from datetime import datetime

import mouseController as mc

maxListLen = 20

def toggleState():
	print('test')
	print(actionBtnTxt.get())
	isRunning = (actionBtnTxt.get()=='Start')
	if isRunning:
		mc.loop()
	btnTxt =  'Stop' if isRunning else 'Start'
	actionBtnTxt.set(btnTxt)
	now = datetime.now()
	log = str(now)+' '+btnTxt
	logList.insert(END, log)
	length = logList.size()
	if length >= maxListLen:
		logList.delete(0)
	logList.see(END)

root = Tk()
root.title('Automate')

root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)

# Parent widget for buttons
btnFrame = Frame(root)
btnFrame.grid(row=0, column=0, sticky=W+E)

actionBtnTxt = StringVar()
actionBtn = Button(btnFrame, textvariable=actionBtnTxt, command=toggleState)
actionBtnTxt.set('Start')
actionBtn.grid(row=0,column=0, padx=(10), pady=10)

# Log frame
logFrame = LabelFrame(root, text='Logs', padx=5, pady=5)
logFrame.grid(row=1, column=0, columnspan=3, padx=10,pady=10, sticky=E+W+N+S)

logFrame.columnconfigure(0, weight=1)
logFrame.rowconfigure(0,  weight=1)

logScrollbar = Scrollbar(logFrame)
logList = Listbox(logFrame, yscrollcommand = logScrollbar.set)
logList.grid(row=0,column=0, sticky=E+W+N+S)
logScrollbar.grid(row=0, column=1, sticky=E+W+N+S)
logScrollbar.config(command=logList.yview)

root.mainloop()
