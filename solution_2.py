import ast
import sys

paths = ['sample_points.txt', 'points_small.txt', 'points_large.txt']
path = paths[1]
input_array = []
possible_list = []
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

def fourSum():
    mp = {}
    ans = []
    min_float = sys.float_info.max
    for i in range(len(input_array)):
        for j in range(i+1, len(input_array)):
            sum = input_array[i][3] + input_array[j][3]
            if sum not in mp:
                mp[sum] = []
            mp[sum].append([i,j])
    
    for curr in mp:
        target = 100 - curr
        if target in mp:
            pairs1 = mp[curr]
            pairs2 = mp[target]
            for pair1 in pairs1:
                for pair2 in pairs2:
                    i, j = pair1
                    k, l = pair2
                    if i != k and i != l and j != k and j != l:
                       volume =  volume_of_tetrahedron(input_array[i], input_array[j], input_array[k], input_array[l])
                       if volume != 0 and volume < min_float:
                            res_p1 = i
                            res_p2 = j
                            res_p3 = k
                            res_p4 = l
                            min_float = volume
                            ans = [res_p1,res_p2,res_p3,res_p4]
    mp[curr] = []
    mp[target] = []
    return ans
        
if __name__ == "__main__":
    read_input_from_file()
    ans = fourSum()
    ans.sort()
    print(ans)






