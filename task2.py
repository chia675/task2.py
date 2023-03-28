#read the shape of the building
building = input("Enter the shape of the building ("square", "rectangular" or "round"): ") 
#intialize the area and pi
building_area = 0;
pi = 3.142

#control statement to execute user entered building 
print()
if building == "square":
    length = int(input("Enter length of the square: "))
    #calculates if the user enters square
    building_area = length ** 2
elif building == "rectangle":
    #else calculates rectangle
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    building_area = length * width 
elif building == "circle":
    #else calculates a circle
    radius = int(input("Enter circle radius length: "))
    building_area = pi * (radius ** 2)
else: 
    #prints if the user enters an invalid building
    print("Invalid enter")

print()    
print("Area of  the foundation of building for shape", building, ":", building_area)
