a=input("enter a string")
c=0
for i in range(len(a)):
    if a[i]!=a[len(a)-i-1]:
        c=c+1
if c==0:
    print("this string is polindroom")
else:
    print("this string is not polindroom")