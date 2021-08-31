#1-1
a = list(input())
new_a=[]

for i in a:
    if i=='y' or i=='z':
        new_a.append(chr(ord(i)-24))
    elif ord(i)<96 or ord(i)>122:
        new_a.append(i)
    else:
        new_a.append(chr(ord(i)+2))
        
for j in new_a:
    print(j,end='')
    



#1-2
import string
a="abcdefghijklmnopqrstuvwxyz"
b="cdefghijklmnopqrstuvwxyzab"
string='map'

c=string.maketrans(a,b)
print(string.translate(c))

