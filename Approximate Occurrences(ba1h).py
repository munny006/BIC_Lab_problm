pattern = input();
text = input();
d = input();
d = int(d);
l = len(text)-len(pattern)+1;
patternLen = len(pattern);

# for i in range(0, l):
#     cnt = 0;
#     idx = 0;
#     for j in range(i, i+patternLen):
#         if(text[j]!=pattern[idx]):
#             cnt+=1;
#         idx+=1;
#     if(cnt<=d):
#         print(i, end=" ");

for i in range(0, l):
    cnt = 0;
    curString = text[i: i+patternLen];
    for j in range(0, patternLen):
        if curString[j]!=pattern[j]:
            cnt+=1;
    if(cnt<=d):
        print(i, end=" ");