
def collatz(n):
    while n > 1:
        print( int(n), end=',')
        if n % 2:
            n = 3*n+1
        else:
            n = n/2

n = int(input("Please enter a number BISH\n"))
print("The Sequence is : ", end=' ')

collatz(n)