##processes that run in parallel
##cpu bound tasks that are heavy on cpu usage
##parallel execution - multiple cores of the cpu
import multiprocessing 
import time
def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"cube:{i*i*i}")

if __name__=="__main__":
    ##creating processes
    p1=multiprocessing.process(target=square_numbers)
    p2=multiprocessing.process(target=cube_numbers)
    t=time.time()

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finished_time=time.time()-t
    print(finished_time)