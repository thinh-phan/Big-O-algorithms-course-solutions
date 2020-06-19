INF = 1e9
 
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
 
def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return (x * x + y * y) ** 0.5
 
# A Brute Force method to return the smallest distance between two points   
def brute_force(point_set, left, right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(point_set[i], point_set[j]))
    return min_dist
 

# A utility function to find the distance beween the closest points of strip of given size
def strip_closest(point_set, left, right, mid, dist_min):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda p: p.y)
 
    smallest = INF
    l = len(splitted_points)
    for i in range(0, l):
        for j in range(i + 1, l):
            if not (splitted_points[j].y - splitted_points[i].y) < dist_min:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)
    return smallest
 
# A recursive function to find the smallest distance.
def closest_util(point_set, left, right):
    # If there are 2 or 3 points, then use brute force
    if right - left <= 3:
        return brute_force(point_set, left, right)
    # Find the middle point
    mid = (right + left) // 2
    # Consider the vertical line passing through the middle point
    dist_left = closest_util(point_set, left, mid)
    dist_right = closest_util(point_set, mid + 1, right)
    # Find the smaller of two distances
    dist_min = min(dist_left, dist_right)
    # Find the closest points in strip
    return min(dist_min, strip_closest(point_set, left, right, mid, dist_min))
 
 
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        point_set = []
        for i in range(n):
            x, y = map(float, input().split())
            point_set.append(Point(x, y))
 
        point_set.sort(key=lambda p: p.x)
        ans = closest_util(point_set, 0, n)
        # Condition
        if ans < 10000:
            print('%.4f' % ans)
        else:
            print('INFINITY')