import math
from friendsbalt.acs import Stack, Vector, Plotter
import random
import sys

def get_distance(one, two):
        x1, y1 = one
        x2, y2 = two
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_closest(points):

    closest_points = []
    closest = 10000000
    if len(points) < 3:
        for p in points:
            closest_points.insert(p)
        return closest_points

    if all(p == points [0] for p in points):
        closest_points.insert(points[0])
        return closest_points

    for i in range (len(points)):
        P_0 = points[i]
        for g in range(len(points)):
            P_k = points[g]
            if i == g:
               pass
            else:
                print("closest",closest)
                if get_distance(P_0,P_k) < closest:
                    closest = get_distance(P_0,P_k)
                    closest_points = [P_0,P_k]

    return closest_points
        

def ccw(p1, p2, p3):
    """
    Determines if three points make a counter-clockwise turn.

    Args:
        p1 (tuple): The first point as a tuple (x, y).
        p2 (tuple): The second point as a tuple (x, y).
        p3 (tuple): The third point as a tuple (x, y).

    Returns:
        int: A positive value if the points make a counter-clockwise turn,
             a negative value if they make a clockwise turn,
             and zero if the points are collinear.
    """
    #return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    v_1 = Vector.from_points(p1, p2)
    v_2 = Vector.from_points(p1, p3)
    return v_1.cross(v_2).z()

def is_left_turn(p1, p2, p3):
    print(ccw(p1,p2,p3)>0)
    return ccw(p1, p2, p3) > 0

def get_lowest_point(points):
    return min(points, key=lambda p: (p[1], p[0]))


def read_points_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def main():
    # Read points from file if available or generate random points
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        points = read_points_from_file(file_path)
    else:
        points = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
    
    # Compute the Hull
    hull = get_closest(points)
    print("hull", hull)

    # Plot the points and the hull
    plotter = Plotter()
    plotter.set_color('blue')
    for i in range(len(hull) - 1):
        plotter.plot_line(hull[i], hull[i + 1])
    plotter.plot_line(hull[len(hull) - 1], hull[0])
    
    print(len(points))
    for p in points:
        plotter.set_color('red')
        if p in hull:
            plotter.set_color('green')
        plotter.plot_point(p)

    #Output the plot
    plotter.save("closest_points.png")

if __name__ == "__main__":
    main()
