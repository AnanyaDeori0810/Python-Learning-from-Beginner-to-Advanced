x=float(input("Enter the coordinate for x axis"))
y=float(input("Enter the coordinate for y axis"))
if (x<0 and y<0):
    print("Third Quadrant")
elif (x>0 and y>0):
    print("First Quadrant")
elif (x<0 and y>0):
    print("Second Quandrant")
elif (x>0 and y<0):
    print("Fourth Quadrant")
elif (x==0 and y==0):
    print("Origin")
elif (x>0 and y==0):
    print("X axis")
elif (x<0 and y==0):
    print("X axis")
elif (x==0 and y<0):
    print("Y axis")
elif (x==0 and y>0):
    print("Y axis")
else:
    print("Not acceptable")