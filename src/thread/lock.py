import threading
lock=threading.Lock()

balance=0
def change_it(value):
    # The below declaration lets the function know that we
    #  mean the global 'balance' when we refer to that variable, not
    #  any local one
    global balance
    balance=balance+value
    balance=balance-value

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

