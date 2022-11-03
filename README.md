# TriangleCenters

Use the function findTriangle to find the vertices of a triangle given its triangle centers.

As input, findTriangle accepts 8 parameters in the following order: (xy_low, xy_high, Ce_x, Ce_y, I_x, I_y, Ci_x, Ci_y, O_x, O_y). They are defined thusly:
  xy_low  =   low range of x- and y-values for your search;  xy_high =   high range of x- and y-values for your search;  Ce_x    =   x-value of centroid;  Ce_y    =   y-value of centroid;  I_x     =   x-value of incenter;  I_y     =   y-value of incenter;  Ci_x    =   x-value of circumcenter;  Ci_y    =   y-value of circumcenter;  O_x     =   x-value of orthocenter;  O_y     =   y-value of orthocenter
  
As of 11/1/2022, the script no longer produces the permutations of solutions, however the runtime is still higher than it needs to be.

As of 10/31/2022, the script is slow and inefficient, but it works. Future improvements will include eliminating redundant solutions. Right now, all permutations of a solution triangle's three vertices are given, so one solution comprised of 3 points appears as six solutions (since 3! = 6).
