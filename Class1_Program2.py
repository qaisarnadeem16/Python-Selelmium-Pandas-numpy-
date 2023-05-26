import pandas as pd

S1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S1.head())
print(S1.head(3))

print(S1.tail())
print(S1.tail(3))


def fibonacci(n):
    fib_seq=[0,1]
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    return fib_seq

fibonacci_series = fibonacci(10)
print(fibonacci_series)
