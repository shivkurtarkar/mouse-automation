from tkinter import *
from datetime import datetime

def toggleState():
	print('test')
	print(actionBtnTxt.get())
	isRunning = (actionBtnTxt.get()=='Start')
	btnTxt =  'Stop' if isRunning else 'Start'
	actionBtnTxt.set(btnTxt)
	now = datetime.now()
	log = str(now)+' '+btnTxt
	logList.insert(END, log)


root = Tk()
root.title('Automate')

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

logScrollbar = Scrollbar(logFrame)
logScrollbar.pack(side=RIGHT, fill=Y, expand=1)
logList = Listbox(logFrame, yscrollcommand = logScrollbar.set)
logList.pack(side=LEFT, fill=BOTH, expand=1)
logScrollbar.config(command=logList.yview)

root.mainloop()
