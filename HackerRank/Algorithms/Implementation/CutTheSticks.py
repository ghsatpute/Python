# @Author   : Ganesh Satpute
# @email 	: ghsatpute@gmail.com
# @time     : 22 Apr 2015, 11:55 PM

'''
Problem Statement

You are given N sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

Suppose we have six sticks of the following lengths:

5 4 4 2 2 8
Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following:

3 2 2 6
The above step is repeated until no sticks are left.

Given the length of N sticks, print the number of sticks that are cut in subsequent cut operations.

Input Format 
The first line contains a single integer N. 
The next line contains N integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.

Output Format 
For each operation, print the number of sticks that are cut in separate line.

Constraints 
1 = N = 1000 
1 = ai = 1000

Sample Input #00

6
5 4 4 2 2 8
Sample Output #00

6
4
2
1
Sample Input #01

8
1 2 3 4 3 3 2 1
Sample Output #01

8
6
4
1
Explanation

Sample Case #00 :

sticks-length        length-of-cut   sticks-cut
5 4 4 2 2 8             2               6
3 2 2 _ _ 6             2               4
1 _ _ _ _ 4             1               2
_ _ _ _ _ 3             3               1
_ _ _ _ _ _           DONE            DONE
Sample Case #01

sticks-length         length-of-cut   sticks-cut
1 2 3 4 3 3 2 1         1               8
_ 1 2 3 2 2 1 _         1               6
_ _ 1 2 1 1 _ _         1               4
_ _ _ 1 _ _ _ _         1               1
_ _ _ _ _ _ _ _       DONE            DONE
'''


numSticks = int(raw_input())

sticks = map(int, raw_input().split(' '))

while(len(sticks) != 0) :
    minimum = min(sticks)
    print len(sticks)
    for i in range(0, len(sticks)) :
        sticks[i] = sticks[i] - minimum
    sticks = filter(lambda a: a != 0, sticks)