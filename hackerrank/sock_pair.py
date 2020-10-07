import math
def sockMerchant(n, ar):
    ar.sort()
    result = 0
    c = 0
    for i in range(len(ar)):
        count=0
        count = ar.count(ar[c])
        print("array ar[i]--",ar[c])
        c += count
        result += int(math.floor(count/2))
        print(result)
        if c >= len(ar):
            break
    return result

ar = [10,20,10,20,10,40,20,10,50]
sockMerchant(len(ar),ar)
