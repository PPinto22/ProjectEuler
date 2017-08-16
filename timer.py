import time

def formatTime(time):
    hours, rem = divmod(time, 3600)
    minutes, seconds = divmod(rem, 60)
    milis = 1000*(seconds-int(seconds))
    timeString = ''
    if int(hours) > 0:
        timeString += "{:0>2}h ".format(int(hours))
    if int(minutes) > 0:
        timeString += "{:0>2}m ".format(int(minutes))
    if int(seconds) > 0:
        timeString += "{:0>2}s ".format(int(seconds))
    timeString += "{:.3f}ms".format(milis)
    return timeString

def run(function):
    initial_time = time.clock()
    function()
    elapsed_time = time.clock() - initial_time
    print "Execution time: "+formatTime(elapsed_time)