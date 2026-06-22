import multiprocessing
import math
import sys
import time
#increae the maximum number of digits for intrger conversioN
sys.set_int_max_str_digits(1000000)
# Function to compute factorial
def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} computed")
    return result
if __name__ == "__main__":
    numbers = [5000,6000,700,8000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)
    end_time = time.time()
    print(f"Results:{results}")
    print(f"Time taken: {end_time - start_time} seconds")