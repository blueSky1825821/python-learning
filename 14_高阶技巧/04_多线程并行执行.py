"""
进程：一个程序，运行在系统之上，之歌程序为一个运行进程，并分配进程id方便系统管理
    进程之间的内存是隔离的
线程：归属于进程，一个进程可以开启多个线程，执行不同的工作，是进程的实际工作最小单位
    内存是共享的
并行执行：同一时间做不同的工作，进程之间就是并行执行，线程也可并行执行

import threading
thread_obj = threading.Thread(group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None)
group:暂时无用
target：执行的目标任务名
name：线程名
启动线程
thread_obj.start()
"""

import threading
import time


def sing(msg):
    while True:
        print(f"正在唱歌...{msg}")
        time.sleep(1)

def dance(msg):
    while True:
        print(f"正在跳舞...{msg}")
        time.sleep(1)

if __name__ == '__main__':
    # 创建线程对象
    thread_sing = threading.Thread(target=sing, args=("happy",))
    thread_dance = threading.Thread(target=dance, kwargs={"msg": "happy"})
    # 启动线程
    thread_sing.start()
    thread_dance.start()