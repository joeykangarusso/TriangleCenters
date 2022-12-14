import math


def centroid(x1, y1, x2, y2, x3, y3):
    Ce_x = (x1 + x2 + x3) / 3
    Ce_y = (y1 + y2 + y3) / 3
    return(Ce_x, Ce_y)


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return(dist)


def incenter(x1, y1, x2, y2, x3, y3):
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)
    if a > 0 and b > 0 and c > 0:
        I_x = ((a * x1 + b * x2 + c * x3) / (a + b + c))
        I_y = ((a * y1 + b * y2 + c * y3) / (a + b + c))
        return(I_x, I_y)
    else:
        return()


def circumcenter(x1, y1, x2, y2, x3, y3):
    a = ((x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2))
    if a != 0:
        Ci_x = (((x1**2 + y1**2) - (x2**2 + y2**2)) * (y1 - y3) -
                ((x1**2 + y1**2) - (x3**2 + y3**2)) * (y1 - y2)) / (2 * a)
        Ci_y = (((x1**2 + y1**2) - (x3**2 + y3**2)) * (x1 - x2) -
                ((x1**2 + y1**2) - (x2**2 + y2**2)) * (x1 - x3)) / (2 * a)
        return(Ci_x, Ci_y)
    else:
        return()


def orthocenter(x1, y1, x2, y2, x3, y3):
    a = (x3 - x2) * (y3 - y1) - (y3 - y2) * (x3 - x1)
    b = (y3 - y2) * (x3 - x1) - (x3 - x2) * (y3 - y1)
    if (a != 0) and (b != 0):
        O_x = ((x2 * (x1 - x3) + y2 * (y1 - y3)) * (y3 - y2) -
               (x1 * (x2 - x3) + y1 * (y2 - y3)) * (y3 - y1)) / a
        O_y = ((x2 * (x1 - x3) + y2 * (y1 - y3)) * (x3 - x2) -
               (x1 * (x2 - x3) + y1 * (y2 - y3)) * (x3 - x1)) / b
        return(O_x, O_y)
    else:
        return()


def findTriangle(xy_low, xy_high, Ce_x, Ce_y, I_x, I_y, Ci_x, Ci_y, O_x, O_y):
    A_x = A_y = B_x = B_y = C_x = C_y = range(xy_low, xy_high)
    for a in A_x:
        for b in A_y:
            for c in B_x:
                for d in B_y:
                    for e in C_x:
                        for f in C_y:
                            if ((centroid(a, b, c, d, e, f) == (Ce_x, Ce_y)) and (incenter(a, b, c, d, e, f) == (I_x, I_y)) and (circumcenter(a, b, c, d, e, f) == (Ci_x, Ci_y)) and orthocenter(a, b, c, d, e, f) == (O_x, O_y)):
                                if(a <= c and c <= e and b <= d):
                                    print("A(", a, ",", b, "),", "B(", c,
                                          ",", d, "),", "C(", e, ",", f, ")")


findTriangle(-11, 11, 14 / 3, 2, 5, 0, 5.5, 4, 3, -2)
