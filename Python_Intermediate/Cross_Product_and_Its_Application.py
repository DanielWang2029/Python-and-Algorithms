

# this represent a point in 2D
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


# this computes the cross product of two vector starting from the origin in 2D
#  i   j   k
# p1x p1y  0  =  p1x * p2y - p1y * p2x
# p2x p2y  0
# remember that cross product is positive only if points are given in counter-clockwise, otherwise its negative
def cross_product(p1: Point, p2: Point):
    return p1.x * p2.y - p1.y * p2.x


# remember that the area of the triangular OAB is the same as the length of the cross product of a and b / 2
def area_origin(p1: Point, p2: Point):
    return abs(cross_product(p1, p2)) / 2.0


# this is simply dividing the triangle into three smaller triangle and add their area together
def area_origin_within(p1: Point, p2: Point, p3: Point):
    return area_origin(p1, p2) + area_origin(p1, p3) + area_origin(p2, p3)


# this works for all cases because if the origin is outside
# then one or two of the cross product is going to be negative because the points are cross product in clockwise order
# which will cancel the area between the origin and those points that is not within the triangle
def area_triangle(p1: Point, p2: Point, p3: Point):
    return abs(cross_product(p1, p2) + cross_product(p2, p3) + cross_product(p3, p1)) / 2.0


# args must be given in either clockwise or counter-clockwise order
# this also works for all cases regardless of where this polygon stands
def area_polygon(*args: Point):
    productSum = 0.0
    for index in range(len(args)):
        productSum += cross_product(args[index], args[index - 1])
    return abs(productSum) / 2.0


print(area_origin_within(Point(-1, -1), Point(1, -1), Point(0, 1)))
print(area_triangle(Point(1, 1), Point(3, 1), Point(2, 4)))
print(area_polygon(Point(1, 1), Point(3, 1), Point(5, 1), Point(4, 4), Point(3, 7), Point(2, 4)))
print()


# another application of cross product:
# return 0 is pt is on the line formed by p1 and p2
# return 1 if pt is on the left of the vector p1 -> p2
# return -1 if pt is on the right of the vector p2 -> p1
def direction_of_point_from_line(pt: Point, p1: Point, p2: Point):
    product = cross_product(Point(p2.x - p1.x, p2.y - p1.y), Point(pt.x - p1.x, pt.y - p1.y))
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0


print(direction_of_point_from_line(Point(0, 2), Point(-3, 0), Point(5, 0)))
