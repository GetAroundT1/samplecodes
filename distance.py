import math

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    
    Args:
    point1 (tuple): The coordinates of the first point (x1, y1).
    point2 (tuple): The coordinates of the second point (x2, y2).
    
    Returns:
    float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage:
point_a = (1, 2)
point_b = (4, 6)
distance = calculate_distance(point_a, point_b)
print(f"The distance between {point_a} and {point_b} is {distance:.2f}")
