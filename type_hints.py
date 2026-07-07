def factorial(n:int)->int:
    result: int=1
    for i in range(1,n+1):
        result*=i
    return result
def is_prime(n:int)->int:
    if n<2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def is_palindrome(text:str)->bool:
    return text==text[::-1]
def calculate_average(numbers:list[float])->float:
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers)/len(numbers)
def find_maximum(numbers:list[int])->int:
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)
print("Factorial:",factorial(5))
print("Prime Number Check:",is_prime(7))
print("Palindrome Check:",is_palindrome("madam"))
print("Average:",calculate_average([10,20,30,40,50,60]))
print("Maximum Element:",find_maximum([10,50,20,80,30]))