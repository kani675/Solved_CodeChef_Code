t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    b=sorted(d)
    if b==d:
        print("Yes")
    else:
        print("No")
