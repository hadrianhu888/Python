import math 

def is_prime(num): 
    """checks if the number is prime or not"""
    if num <= 1: 
        return False
    if num == 2: 
        return True
    if num > 2 and num % 2 == 0: 
        return False
    max_div = math.floor(math.sqrt(num)) 
    for i in range(3, 1 + max_div, 2): 
        if num % i == 0: 
            return False
    return True

def list_primes(num): 
    """Returns a list of prime numbers up to num"""
    primes = []
    for index in range(1, num + 1): 
        if is_prime(index): 
            primes.append(index)
    return primes

def print_next_prime(num): 
    """Prints the closest prime number larger than num"""
    index = num 
    while True: 
        index += 1
        if is_prime(index): 
            print(index)
            break
        
def main(): 
    """Main function"""
    num = int(input("Enter a number: "))
    if is_prime(num): 
        print("The number is prime")
    else: 
        print("The number is not prime")
    print_next_prime(num)
    list_primes(num)
        
if __name__ == "__main__":
    main()
