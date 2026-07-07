import time
from functools import wraps
def execution_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Function Name:{func.__name__}")
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        print(f"Execution Time: "f"{end_time-start_time:.6f}seconds")
        return result
    return wrapper
@execution_time
def calculate_sum():
    total=sum(range(1,1000000))
    print("Sum:",total)
@execution_time
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    print("Factorial:",result)
@execution_time
def find_even_numbers():
    even_numbers=[number for number in range (1,1000000) if number%2==0]
    print("Even Numbers Count:",len(even_numbers))
calculate_sum()
print()
factorial(10)
print()
find_even_numbers()