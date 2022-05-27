import sys

total_count = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

unsorted_until_index = total_count - 1
changed = False

for i in range(total_count):
    changed = False
    for j in range(unsorted_until_index):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            changed = True
    if not changed:
        print(i)
        break

    unsorted_until_index -= 1
