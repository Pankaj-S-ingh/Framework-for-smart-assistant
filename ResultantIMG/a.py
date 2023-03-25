a=input()
b=''
for i in range(a):
    if i==1 or i==3 :
        b+=str(int(a[i])-5)
    else:
        b+=a[i]
print(b)
