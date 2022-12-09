text = input();
k = input();
k = int(k);
my_dict = {};
l = len(text) - k+1;

for i in range (0,l):
    curString = text[i:i+k]
    if curString in my_dict.keys():
        my_dict[curString]+=1;
    else:
        my_dict[curString] = 1;
        mx = max( my_dict.values());
for keys,values in my_dict.items():
     if(values == mx):
         print(keys,end =" ");