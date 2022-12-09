pattern=input();
ctr=input();
k=input();
k=int(k);
btr=""
dtr="" 
i=0
l = len(pattern);
while i < l:
    if pattern[i] == "A":
        btr = btr + "T"
    elif pattern[i] == "T":
        btr = btr + "A"
    elif pattern[i] == "G":
        btr = btr + "C"
    elif pattern[i] == "C":
        btr = btr + "G"
    i+=1

i=0
j=0
res=0
m = len(ctr)-len(pattern)+1;
s =len(btr) ;
while i<m:
    dtr=ctr[i:i+s]
    cnt=0
    j=0
    while j<len(dtr):
        if pattern[j]!=dtr[j]:
            cnt+=1
        j+=1
    if cnt==k:
     
        res = 1
       
        cnt=0
    i+=1



if res==0:
    print("HELLO")
else:
    print(btr)