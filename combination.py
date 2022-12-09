Text = input();
pattern = input();
d = input();
d = int(d);
patternLen = len(pattern);
l=len(Text) - len(pattern)+1 ;
ans =0;
for i in range(0,l):
    if Text[i:i+len(pattern)] == pattern :
        ans+=1;
        
print(ans);
for i in range(0,l):
    if Text[i:i+len(pattern)] == pattern :
      print(i,end = " ");
for i in range(0, l):
    cnt = 0;
    curString = text[i: i+patternLen];
    for j in range(0, patternLen):
        if curString[j]!=pattern[j]:
         cnt+=1;
    if(cnt<=d):
       print(i, end=" ");      
