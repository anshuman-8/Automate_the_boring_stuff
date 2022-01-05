import time

print('Press ENTER to begin.\n Afterward, press ENTER to "click" the stopwatch.\n Press Ctrl-C to quit.')

input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(2, ' '),str(totalTime).rjust(5, ' '), str(lapTime).rjust(5, ' ')), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')