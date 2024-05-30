import ast
import itertools
import sys

path = 'points_small.txt'
input_array = []
min_float = sys.float_info.max
res_p1 = -1
res_p2 = -1
res_p3 = -1
res_p4 = -1

def read_input_from_file():
    with open(path, 'r') as file:
        for line in file:
            # Converting the line to tuple
            data = ast.literal_eval(line)
            input_array.append(list(data))

def volume_of_tetrahedron(p1, p2, p3, p4):
    # Vectors from p1 to p2, p3, and p4
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    # Direct calculation of the cross product components
    cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
    cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
    cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

    # Dot product of AD with the cross product of AB and AC
    scalar_triple_product = (
        AD[0] * cross_product_x +
        AD[1] * cross_product_y +
        AD[2] * cross_product_z
    )

    # The volume of the tetrahedron
    volume = abs(scalar_triple_product) / 6.0
    return volume

read_input_from_file()

# Generate all combinations of 4 points with their indexes
combinations_of_points = itertools.combinations(enumerate(input_array), 4)

# Calculate volume for each combination and print with indexes
for combination in combinations_of_points:
    indices, points = zip(*combination)
    p1, p2, p3, p4 = points
    volume = volume_of_tetrahedron(p1, p2, p3, p4)
    if (p1[3] + p2[3] + p3[3] + p4[3]) == 100:
        if volume != 0:
            if volume < min_float:
                res_p1 = indices[0]
                res_p2 = indices[1]
                res_p3 = indices[2]
                res_p4 = indices[3]
                min_float = volume

print(res_p1, res_p2, res_p3, res_p4)