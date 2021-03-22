#!/bin/python3

import sys


def jimOrders(orders):
    # Complete this function
    ans = list()
    d = dict()
    for i in range(len(orders)):
        ans.append( [orders[i][0]+orders[i][1],i+1] )
    ans.sort()
    ans2 = list()
    for i in ans:
        ans2.append(i[1] )
    return ans2


if __name__ == "__main__":
    n = int(input().strip())
    orders = [ ]
    for orders_i in range(n):
        orders_t = [ int(orders_temp) for orders_temp in input().strip().split(' ') ]
        orders.append(orders_t)
    result = jimOrders(orders)
    print(" ".join(map(str, result)))


