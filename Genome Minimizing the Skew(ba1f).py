text = input();
l = len(text);

cnt=0; 
mn=1e9;

for i in range(0, l):
    if text[i]=='C':
        cnt-=1;
    if text[i]=='G':
        cnt+=1;
    if cnt<mn:
        mn=cnt;
cnt=0;
for i in range(0, l):
    if text[i]=='C':
        cnt-=1;
    if text[i]=='G':
        cnt+=1;
    if cnt==mn:
        print(i+1, end=" ");
