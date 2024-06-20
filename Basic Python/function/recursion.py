# n! = 1 * 2 * 3 *......*n
# n! = 1 * 2 * 3 *......*(n-1)! *n
# n! = n * (n-1)!


# n = 3
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
f = factorial_iter(4)
print(f)

def factorial_recur(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recur(n-1)
print(factorial_recur(3))
