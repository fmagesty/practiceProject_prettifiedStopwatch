#! python 3
# stopwatch.py - A simple stopwatch program.
#use pyperclip module (ch 6) to copy the text output to the clipboard so the user can
# quickly paste the output to a text file or email. 

import time, pyperclip

copia = []

# Display the program's istructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')
input()                     # press ENTER to begin
print('Started.')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, str(totalTime).rjust(5), str(lapTime).rjust(5)), end='')
        copia.append('Lap #%s: %s (%s)' % (lapNum, str(totalTime).rjust(5), str(lapTime).rjust(5)))
        pyperclip.copy(str(copia.copy()))
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error message from displaying.
    print('\nDone.')