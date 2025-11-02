side1=int(input("Enter a first side\n"))
side2=int(input("Enter a second side\n"))
side3=int(input("Enter a third side\n"))

AC=side1*side1
AB=side2*side2
BC=side3*side3
if AC == AB + BC or AB == AC + BC or BC == AB + AC:
    {
        print("Yes")
    }
else:
    print("No")