def power(x, n):
    result = 1
    for _ in range(abs(n)):
        result *= x
    return result if n >= 0 else 1/result

x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
print(power(x, n))
