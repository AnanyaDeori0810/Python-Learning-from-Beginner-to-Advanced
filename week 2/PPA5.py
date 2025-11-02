x1=float(input("Enter the coodrinate for x1\n"))
y1=float(input("Enter the coodrinate for y1\n"))
x2=float(input("Enter the coodrinate for x2\n"))
y2=float(input("Enter the coodrinate for y2\n"))
x3=float(input("Enter the coodrinate for x3\n"))
m=(y2-y1)/(x2-x1)
y3=y1 + m*(x3-x1)

if (x1==x2):
    print("Vertical Line")    
else:
    print(y3)
if (m>0):
    print("Positive slope")
elif (m<0):
    print("Negative slope")
else:
    print("Horizontal line")