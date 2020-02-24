filein=open("a.txt","r");
a=filein.read().split()
l=[]
for i in range(6):
    o=(int (input('')))
    l.append(o)


fl=False
k=0
while k<len(a) and not fl:
    sList=a[k:k+4]
    j=0
    i=0
    fl=False;
    while j<=2 and  fl==False:
        if int(sList[i])==l[j] and int(sList[i+1])==l[j+1] and int(sList[i+2])==l[j+2] and int(sList[i+3])==l[j+3] :            
            fl=True
        else:
            j+=1
    k=k+4        
    print fl