Coins = int(input("Enter the number of gold coins you have\n"))
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1>0 and n2>0 and n3 >0 and n1!=n2 and n2!=n3 and n3!=n1 and n1+n2+n3==Coins:
    print("Fair")
    
else:
    print("Not fair")