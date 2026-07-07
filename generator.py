def prime_generator(start:int,end:int):
    for number in range(start,end+1):
        if number<2:
            continue
        is_prime=True
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                is_prime=False
                break
        if is_prime:
                yield number
start_number=int(input("Enter the first number:"))
end_number=int(input("Enter the second number:"))
print("Prime numbers:")
for prime in prime_generator(start_number,end_number):
    print(prime)