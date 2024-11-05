import random
import string
random_string1=''
random_string2=''
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(8))
random_string1=random_string1+random_string
random_string_2 = ''.join(random.choice(string.ascii_letters) for _ in range(8))
random_string2=random_string2+random_string_2

decoded=''
inp=input('enter encoded key : ')
lst1=['k','m','n','g','o','s','q','p','h']
lst2=['1','2','3','4','5','6','7','8','9']
for momin in inp[8:16]:
    temp3=lst2.index(momin)
    temp4=lst1[temp3]
    decoded=decoded+temp4
print(decoded)
decoded=random_string1+decoded+random_string2
print(random_string1)
print(random_string2)
print('the key for this one is : ',decoded)
