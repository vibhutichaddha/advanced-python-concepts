import os
from datetime import datetime
from functools import wraps
def log_function(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        os.makedirs("logs",exist_ok=True)
        with open("logs/function.log","a") as file:
            file.write(f"Timestamp:{datetime.now()}\n"
                       f"Function name:{func.__name__}\n"
                       f"Arguments:args={args},kwargs={kwargs}\n"
                       f"Return Value:{result}\n"
                       f"{'-'*40}\n")
        return result
    return wrapper
@log_function
def add(a,b):
    return a+b
@log_function
def multiply(a,b):
    return a*b
@log_function
def greet(name):
    return f"Hello, {name}!"
print(add(10,5))
print(multiply(10,5))
print(greet("ABC"))