##Multithreading
## when to use Multi Threading
## I/O bound tasks that are heavy on input output operations
## concurrent execution - single core of the cpu



import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter:{letter}")
##creating threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
##starting  threads
t1.start()
t2.start()
##waiting for threads to complete
t1.join()
t2.join()
##print_numbers()
##print_letter()
finished_time=time.time()-t
print(f"Execution time without threading:{finished_time} seconds")                

