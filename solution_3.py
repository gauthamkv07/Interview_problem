import ast
import sys
import bisect

paths = ['sample_points.txt', 'points_small.txt', 'points_large.txt']
path = paths[2]
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

def binary_search_after(arr, target, left, right):
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid][0] == target:
            return mid
        elif arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def binary_search(arr, target, left, right):
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid][0] == target:
            return mid
        elif arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  


def four_sum():
    ans = []
    n = len(input_array)

    size = ((n * (n - 1)) // 2)
    arr = [None for _ in range(size)]

    k = 0
    for i in range(n-1):
        for j in range(i+1, n):
            arr[k] = [0,0,0]
            arr[k][0] = input_array[i][3] + input_array[j][3]
            arr[k][1] = i
            arr[k][2] = j
            k += 1
    
    arr.sort(key = lambda x: x[0])
    l = 0
    r = size - 1
    min_float = sys.float_info.max
    while(l < r):
        i = arr[l][1]
        j = arr[l][2]
        k = arr[r][1]
        m = arr[r][2]
        if arr[l][0] + arr[r][0] == 100 and i != k and i != m and j != k and j != m:
            nr = r
            while l < nr and arr[l][0] + arr[nr][0] == 100:
                k = arr[nr][1]
                m = arr[nr][2]
                if i != k and i != m and j != k and j != m:
                    volume =  volume_of_tetrahedron(input_array[i], input_array[j], input_array[k], input_array[m])
                    if volume != 0 and volume < min_float:
                        res_p1 = i
                        res_p2 = j
                        res_p3 = k
                        res_p4 = m
                        min_float = volume
                        ans = [res_p1,res_p2,res_p3,res_p4]
                nr -= 1
            l+=1
        elif arr[l][0] + arr[r][0] < 100:
            l = binary_search_after(arr, (100 - arr[r][0]), l+1, r-1)
        else:
            r = binary_search(arr, (100 - arr[l][0]), l+1, r-1)
    return ans, min_float
        
if __name__ == "__main__":
    read_input_from_file()
    ans, vol = four_sum()
    ans.sort()
    print(ans, vol)





