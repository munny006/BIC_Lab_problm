text =input();
t = input();
k = input();
t= int(t);
k = int(k);
l = len(text) - k +1;
my_dict = {}
for i in range(0,l):
    Curstring = text[i:i+k]
    if Curstring in my_dict.keys() :
        my_dict[Curstring]+=1
    else :
        my_dict[Curstring] = 1
        ans = 0
for keys,values in my_dict.items():
  
     if(values==t):
         ans= 1
         w = keys[::-1]
         print(w)
     
if ans==0:
    print("Alas I lost the game")
        