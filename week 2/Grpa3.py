word=input("Enter the name\n").lower()
if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
    y="" 
    if 'a' in word:
        y+='a'
    if 'e' in word:
        y+='e'
    if 'i' in word:
        y+='i'
    if 'o' in word:
        y+='o'
    if 'u' in word:
        y+='u'
    print(y)
    
else:
    print('none')

