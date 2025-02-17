#!/bin/python3
"""
Check out the resources on the page's right side to learn more about heaps. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.
The median of a dataset of integers is the midpoint value of the dataset for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your dataset of integers in non-decreasing order, then:

If your dataset contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted dataset ,  is the median.
If your dataset contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted dataset ,  is the median.
Given an input stream of  integers, you must perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the list's updated median on a new line. The printed value must be a double-precision number scaled to decimal place (i.e.,  format).
Input Format

The first line contains a single integer, , denoting the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be added to your list.

Constraints

Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to  decimal place (i.e.,  format).

Sample Input

6
12
4
5
3
8
7
Sample Output

12.0
8.0
5.0
4.5
5.0
6.0
Explanation
There are  integers, so we must print the new median on a new line as each integer is added to the list:


"""

import sys
from bisect import insort


def median(a):
    if len(a) % 2 == 0:
        l = a[ len(a) // 2 ];
        r = a[ (len(a) // 2) - 1 ]
        med = (l + r) / 2.0

    elif len(a) % 2 != 0:
        med = a[ len(a) // 2 ]
    return med


if __name__ == '__main__':
    heap = [ ]
    for _ in range(int(input())):
        insort(heap, int(input()))
        print(float(median(heap)))

"""n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)a
x = []
for i in a:
    x.append(i)
    ans = float(median(x))
    print(ans)"""
