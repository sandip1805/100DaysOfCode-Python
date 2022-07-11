
def factorial(n):
    if (n > 1):
        return n * factorial(n-1)
    else:
        return 1

if __name__ == "__main__":
    print("Factorial of number!!")    
    for i in range(1, 11):
        print(f"Factorial of {i} is {factorial(i)}")
    