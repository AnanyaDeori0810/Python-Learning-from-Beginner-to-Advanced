word=str(input("Enter a word\n"))
m=len(word)
if (m>=4):
    if (m%2!=0):
        print(word)
    elif (m%2==0):
        if (word[-1]=='.'):
            print(word[0:m-1])
        else:
            print(word+'.')
#else:
    print("Not applicable")