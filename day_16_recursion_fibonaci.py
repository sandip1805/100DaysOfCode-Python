def fibonacci(n):
    if(n >= 3):
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1

if __name__ == "__main__":
    print("Fibonacci number!!")    
    for i in range(1, 11):
        print(f"Fibonacci number at {i} is {fibonacci(i)}")
