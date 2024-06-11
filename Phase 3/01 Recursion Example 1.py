def printThis(i,n):
    if i>=n:
        print("Base condition got hit")
        return
    print("Hello",i)
    print("World",i)
    printThis(i+1,n)
    print("This",i)
    print("is recursion",i)
printThis(1,8)
