import sys
ellips = sys.argv[1]
points = sys.argv[2]
 
with open(ellips, 'r') as f:
    cx, cy = map(float, f.readline().strip().split()) 
    a, b = map(float, f.readline().strip().split())
 
with open(points, 'r') as f:
    for line in f:
        x, y = map(float, line.strip().split()) 
        distance_value = ((x - cx)**2 / a**2) + ((y - cy)**2 / b**2)
        if abs(distance_value - 1) < 1e-10:
            print(0)  
        elif distance_value < 1:
            print(1)  
        else:
            print(2)
