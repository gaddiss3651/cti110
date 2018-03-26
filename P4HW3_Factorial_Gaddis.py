# CTI-110 
# P4HW3 Factorial
# Shannon Gaddis
# March 25, 2018


def main(n):
    if n == 0:
        return 1
    else:
        return n * main(n-1)
n=int(input("Enter a nonnegative integer: "))
print('The factorial of ',n, ' is ',main(n),'.', sep='')














