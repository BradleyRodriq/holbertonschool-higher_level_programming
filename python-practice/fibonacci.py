#!/usr/bin/python3

def fibonacci(n):
    sequence = [10, 20]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


for n in range(1, 11):
    print(f"Fibonacci sequence with {n} terms:", fibonacci(n))
