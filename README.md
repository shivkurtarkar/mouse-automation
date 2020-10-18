# mouse-automation

This a click bot. I have added a script section where you can write custom script that will tell bot what to do.
and whatever the bot does it logs out in the log section. 


![application gui](https://github.com/shivkurtarkar/mouse-automation/blob/master/pic/Screenshot_20201018_160843.png)

## Functionality
### Start/Stop
runs/stops the script
### Reload script
fetches default script saved in `scripts/autoScript.txt`
### Clear log
clears out logs
### Log cursor coordinate
logs cursor coordinate if turned on, to help you write script.

## File structure
### `main.py`
contains gui code. I have used tkinter to write application interface
### `parseScript.py`
contains code to read file and converting script text to commands
### `mouseController.py`
contains main logic that follows and executes the commands

## Instructions to getting started

Install dependencies by running in root directory
```pip3 install -r requirements.txt```

Run as a administrator since mouse control requires admin previlieges
On Linux
```sudo python3 main.py```

On windows open cmd as administrator
and run 
```python3 main.py```
