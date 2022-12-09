x = input();
y = input();

n = len(x); 
ans=0;

for i in range(0, n):
    if x[i]!=y[i]:
        ans+=1;

print(ans);


