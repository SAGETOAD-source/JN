from concurrent.futures import ProcessPoolExecutor
import time
t=time.time()
def square_number(number):
    time.sleep(1)
    return f"Square: {number * number}"
numbers={1,2,3,4,5,6,788,4,5,6,7,98,9,6,5}
if __name__ == "__main__":
    with ProcessPoolExecutor (max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        for result in results:
            print(result)
        max_time=time.time()-t
        print(f"Max time taken in seconds: {max_time}")
    