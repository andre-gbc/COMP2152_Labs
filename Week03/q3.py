print("="*50)
print("Question 3: Coordinate System (Tuples)")
print("="*50)

point1=(3, 5)
print("Point 1:", point1)

point2=(7, 2)
print("Point 2:", point2)

x1, y1 = point1
print("Point 1 - x:", x1, "y:", y1)
x2, y2 = point2
print("Point 2 - x:", x2, "y:", y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance between Point 1 and Point 2:", distance)
