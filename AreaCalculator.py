#wrt a prg to create area calculator
print("******AREA CALCULATOR******")
print("press 1 to get the area of square")
print("press 2 to get the area of cube")
print("press 3 to get the area of rectangle")
print("press 4 to get the area of triangle")

choice=int(input("choose your choice 1-4:"))

if choice==1:
    s=int(input("enter the side"))
    area=s**2
    print("the area of square is",area)

