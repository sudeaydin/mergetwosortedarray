a=[3,5,7,10,12,16]
b=[1,4,18,21]
c=list()
na=len(a)
nb=len(b)
ia=0
ib=0
ic=0

while ib<nb and ia<na :
    if b[ib]<a[ia]:
        c.insert(ic,b[ib])
        ic=ic+1
        ib=ib+1
    else:
        c.insert(ic,a[ia])
        ic=ic+1
        ia=ia+1

if ia<na:
    for i in range(ia,na):
        c.insert(ic,a[i])
        ic=ic+1
else:
    for i in range(ib,nb):
        c.insert(ic,b[i])
        ic=ic+1


print(c)
