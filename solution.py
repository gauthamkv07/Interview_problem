import ast
import sys

paths = ['sample_points.txt', 'points_small.txt', 'points_large.txt']
path = paths[1]
input_array = []
possible_list = []
min_float = sys.float_info.max
res_p1 = -1
res_p2 = -1
res_p3 = -1
res_p4 = -1
ans = []

def read_input_from_file():
    index = 0
    with open(path, 'r') as file:
        for line in file:
            # Converting the line to tuple
            data = ast.literal_eval(line)
            data = list(data)
            data.append(index)
            input_array.append(list(data))
            index+=1

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



def k_sum(start, target, k, path):
        if k == 2: 
            left, right = start, len(input_array) - 1
            while left < right:
                sum_two = input_array[left][3] + input_array[right][3]
                if sum_two == target:
                    possible_list.append(path + [input_array[left], input_array[right]])
                    nr = right - 1
                    while(left < nr and input_array[left][3] + input_array[nr][3] == target):
                        possible_list.append(path + [input_array[left], input_array[nr]])
                        nr -= 1
                    left += 1
                elif sum_two < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, len(input_array)):
                k_sum(i + 1, target - input_array[i][3], k - 1, path + [input_array[i]])

if __name__ == "__main__":
    read_input_from_file()

    input_array = sorted(input_array, key=lambda x: x[3])

    k_sum(0,100, 4, [])

    for curr in possible_list:
        p1, p2, p3, p4 = curr
        volume = volume_of_tetrahedron(p1, p2, p3, p4)
        if volume != 0 and volume < min_float:
            res_p1 = p1[4]
            res_p2 = p2[4]
            res_p3 = p3[4]
            res_p4 = p4[4]
            min_float = volume

    ans = [res_p1,res_p2,res_p3,res_p4]
    ans.sort()
    print(ans, min_float)



