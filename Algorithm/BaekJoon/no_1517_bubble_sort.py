import sys

total_count = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

sorted = False
unsorted_until_index = total_count - 1
count = 0

while not sorted:
    sorted = True
    for i in range(unsorted_until_index):
        if num_list[i] > num_list[i+1]:
            count += 1
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            sorted = False
    unsorted_until_index -= 1

print(count)


# https: // jokerldg.github.io/algorithm/2021/09/12/bubble-sort.html
