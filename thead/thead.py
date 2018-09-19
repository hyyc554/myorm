# -*- coding: utf-8 -*-

from threading import Thread
import time

def work():
    with open('123.txt','w') as f:
        data =f.read()
        f.write('weqweq')
        time.sleep(5)

    print('hello')


if __name__ == '__main__':
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t3 = Thread(target=work)
    t1.start()
    t2.start()
    t3.start()

    print('主线程/主进程')
