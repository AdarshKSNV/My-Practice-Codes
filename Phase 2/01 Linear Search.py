l=[10,11,23,5,67,8]
T=int(input("Enter a Number :"))
for i in range(0,len(l)):
    if T==l[i]:
        print("The element is found at ",i)
        break
