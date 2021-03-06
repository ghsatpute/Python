# @Author   : Ganesh Satpute
# @Email    : ghsatpute@gmail.com
# @Time     : 16 Feb 2016, 11:59 PM

"""
https://www.hackerrank.com/challenges/manasa-and-stones

Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either aa or bb. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 00, find all the possible values for the number on the last stone.

Note: The numbers on the stones are in increasing order.

Input Format 
The first line contains an integer TT, i.e. the number of test cases. TT test cases follow; each has 3 lines. The first line contains nn (the number of stones). The second line contains aa, and the third line contains bb.

Output Format 
Space-separated list of numbers which are the possible values of the last stone in increasing order.

Constraints 
1=T=101=T=10 
1=n,a,b=1031=n,a,b=103

Sample Input

2
3 
1
2
4
10
100
Sample Output

2 3 4 
30 120 210 300 
Explanation

All possible series for the first test case are given below:

0,1,2
0,1,3
0,2,3
0,2,4
Hence the answer 2 3 4.

Series with different number of final steps for second test case are the following:

0, 10, 20, 30
0, 10, 20, 120
0, 10, 110, 120
0, 10, 110, 210
0, 100, 110, 120
0, 100, 110, 210
0, 100, 200, 210
0, 100, 200, 300
Hence the answer 30 120 210 300.
"""

num_test_cases = int(raw_input())

# Looking at the examples it is clear that output should start from
# minimum of those numbers a and b multiplied by n
# And ends to maximum of a, b multiplied by n
# And step should be difference between a and b
# If they are equal step size should be a 

for i in range(num_test_cases):
    n = int(raw_input()) - 1
    a = int(raw_input())
    b = int(raw_input())
    #print n, a, b
    if a < b:
        minimum = a
        maximum = b
    else:
        minimum = b
        maximum = a
    diff = maximum - minimum
    i = minimum * n
	# When the diff is zero the while loop goes in infinite loop
    if diff == 0:
        diff = minimum
    #print minimum, maximum, diff
    while i <= maximum * n:
        print i, 
        i += diff
    print
	
	
	