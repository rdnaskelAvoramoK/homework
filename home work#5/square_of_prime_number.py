lim = int(input("Enter max number: "))

def prime(n):
    for i in range(3, n):
        if n % i == 0:
            return 0
    return n*n

row=[x for x in range(2,lim+1)]
li=list(map(lambda x: prime(x),row))

print([k for k in li if k > 0])