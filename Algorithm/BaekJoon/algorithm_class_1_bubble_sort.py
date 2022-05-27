# 알고리즘 수업 - 버블 정렬 1
import sys

total_count, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, (sys.stdin.readline().split())))

unsorted_until_index = total_count - 1
times_of_change = 0
sorted = False

while(not sorted):
    sorted = True
    for i in range(unsorted_until_index):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            sorted = False
            times_of_change += 1

            if times_of_change == k:
                print(num_list[i], num_list[i+1])
                break

    unsorted_until_index -= 1

if times_of_change < k:
    print(-1)
