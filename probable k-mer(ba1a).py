Text = input();
pattern = input();
l=len(Text) - len(pattern)+1 ;
ans =0;
for i in range(0,l):
    if Text[i:i+len(pattern)] == pattern :
        ans+=1;
        
print(ans);