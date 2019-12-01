from threading import Timer

def sayhi():
    print('ok')

while True:
    timer=Timer(1,sayhi)
    timer.start()