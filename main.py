#coding=utf8
from multiprocessing import Process

def test(name):
    print 'hello',name
if __name__=='__main__':
    p=Process(target=test,args=('lvshr',))
    p.start()
    p.join()