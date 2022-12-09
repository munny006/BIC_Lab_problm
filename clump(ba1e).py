text = input();
k = input();
L = input();
t = input();

k = int(k);
L = int(L);
t = int(t);

my_dict = {};

size = len(text)-L+1;
for i in range(0, size):
    window = L-k;
    for j in range(i, i+window):
        curString = text[j: j+k];
        cnt = text[i:i+L].count(curString);
        if(cnt >= t):
            my_dict[curString] = 1;

for keys,values in my_dict.items():
    print(keys, end=" ");