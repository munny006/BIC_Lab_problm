pattern = input();
text = input();
l = len(text) - len(pattern) +1 ;
for i in range(0,l):
    if text[i:i+len(pattern)] == pattern:
        print(i,end = " ");