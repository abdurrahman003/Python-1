l=['aa','012',2,4,5,6,7,8,9,]
print(l)
p=input("Enter 1 to append, 2 to length and 3 to quit ")

if p == 1:
    e= input("Enter the value ")
    e.append(l)
    print("The list is altered :",l)

if p == 2:
    ll=len(l)
    print(l)

if p == 3:
    print("TQ")
    exit()

 

