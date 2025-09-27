"""
Challenge 20

Fibonnacci Sequence Generator

"""

def genFib(n):
    # find the fib number
    fib = [0, 1]
    for i in range(2, 51):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

## LOOP
while True:
    pos = input("\nWhich position in sequence?: ")
    if pos.lower() == 'exit':
        print("ok")
        break
    if not pos.isdigit() or not 0 <= int(pos) <= 50:
        print("Please enter a number between 0 and 50.")
        continue
    print(f"Fibonacci number is {genFib(int(pos))}")
