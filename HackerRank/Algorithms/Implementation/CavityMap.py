# @Author   : Ganesh Satpute
# @Email    : ghsatpute@gmail.com
# @Time     : 23 Apr 2015, 04:15 PM

'''
CAVITY MAP

Problem Statement

You are given a square map of size n×n. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side.

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format

The first line contains an integer, n, denoting the size of the map. Each of the following n lines contains n positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.

Constraints

1≤n≤100
Output Format

Output n lines, denoting the resulting map. Each cavity should be replaced with character X.

Sample Input

4
1112
1912
1892
1234
Sample Output

1112
1X12
18X2
1234

'''



import sys
n = int(raw_input())

matrix = []
for i in range(0, n) :
    matrix.append(list(raw_input()))

for i in range(1, n - 1) :
    for j in range(1 , n - 1) :
        if( matrix[i][j] > matrix[i-1][j] and
            matrix[i][j] > matrix[i+1][j] and
            matrix[i][j] > matrix[i][j-1] and
            matrix[i][j] > matrix[i][j+1]
          ) :
            #print "X"
            matrix[i][j] = "X"
            
for i in range(0, n) :
    for j in range(0, n) :
        sys.stdout.write(matrix[i][j]) # Using sysout to avoid printing newline or space 
    print ""
    