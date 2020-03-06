#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# const arr = []
#   arr[0]=1
#   arr[1]=1

#   for(let i =2; i <= n; i++) {
#       arr[i] = arr[i-1] + arr[i-2]
#   }
#   return arr[n]


# def eating_cookies(n, cache=None):
#     arr = []
#     arr.append(1)
#     arr.append(2)

#     if n == 0:
#         return 1

#     for i in range(2, n):
#         arr[1] = arr[i - 1] + arr[i-2]
#         return arr[n] + 1

# def eating_cookies(n, cache={0: 1, 1: 1, 2: 2, 3: 4}):
#     if n in cache:
#         return cache[n]
#     else:
#         cache[n] = eating_cookies(
#             n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#         return cache[n]


# print(eating_cookies(3))

def eating_cookies(n):
    count = 0
    for i in range(n//2, n):
        j = 1
        while j < n:
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
