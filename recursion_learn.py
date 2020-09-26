def fib(n):
    if(n==1 or n==2):
        return 1
    else :
        return fib(n-1)+fib(n-2)

def dyn_fib(n):
    space = [0]*n
    for x in range(n):
        if x == 0 or x == 1:
            space[x] = 1
        else:
            space[x] = space[x-1]+space[x-2]
    return space[len(space)-1]

print(fib(6))
print(dyn_fib(6))
