E1=int(input("Enter your id\n"))
E2=int(input("Enter your id\n"))
E3=int(input("Enter your id\n"))
E4=int(input("Enter your id\n"))
E5=int(input("Enter your id\n"))
if (E1+E2)%2== 0 and (E2+E3)%2== 0 and (E3+E4)%2== 0 and (E4+E5)%2== 0 and (E5+E1)%2== 0:
    {
        print("Yes")
    }
else:
    print("No")