DAY,_,_=__file__.rpartition('.')

from collections import *

from alg.file import download_input
download_input(DAY)

n=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        n=l

#part 1
#josephus
print(int(bin(n)[3:]+'1',2))

#part 2
def solve_parttwo(): # from https://www.reddit.com/r/adventofcode/comments/5j4lp1/comment/dbdf9mn/?utm_source=share&utm_medium=web2x&context=3
    left = deque()
    right = deque()
    for i in range(1, n+1):
        if i < (n // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]

print(solve_parttwo())