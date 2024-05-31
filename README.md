# Answers

points_small.txt answer: (0, 5, 11, 76)
points_large.txt answer: (70, 386, 493, 1429)

# How I did it?

I did brute force tried to do all combinations as expected it didn't work for points_large.txt as it had 1500 points, which leads to 1500^4 test cases. So large to compute. Next given a valid tetrahedron only formed by the values had 100 as sum. So I applied four sum but I didn't get the correct output, courtesy brute force solution helped me to test it. In four sum I was skipping duplicate cases. So I removed duplicate cases and tried it. In solution.py

    nr = right - 1
    while(left < nr and input_array[left][3] + input_array[nr][3] == target):
        possible_list.append(path + [input_array[left], input_array[nr]])
        nr -= 1
    left += 1

This line checks all right values for current left then proceed to the next left value. Still it didn't work because I was checking every left values by incrementing 1 and right values by decrementing 1. I gave up finding the solution at this point. So I looked for another way to do four sum using maps I thought it will work (solution_2.py). It didn't work too because there were so many combinations. So modifying the solution_2 a bit helped me. I calculated the values of all the pairs and sorted it. Then while incrementing pointers in failed sum == 100 cases with binary search. Thanks to brute force I was able to check for points_small.txt test case. I think there may be better solutions but I was able to optimize as much as possible to get a solution.

# Problem Solved 🎉

It feels so good to solve a problem 😊.