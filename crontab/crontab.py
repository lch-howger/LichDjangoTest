import time

localtime = time.localtime(time.time())
file = open('test.txt', 'a')
file.write(str(localtime) + "\n")
file.close()
