import sys

total_count, play_time = map(int, sys.stdin.readline().split())
card_list = list(sys.stdin.readline())[:-1]


def game_rule(left, right):
    if (left == 'R' and right == 'S') or (left == 'S' and right == 'P') or (left == 'P' and right == 'R'):
        return True
    return False


unsorted_until_index = total_count - 1
sorted = False
times = 0

while(not sorted and times < play_time):
    sorted = True
    for i in range(unsorted_until_index):
        if game_rule(card_list[i], card_list[i+1]):
            card_list[i], card_list[i+1] = card_list[i+1], card_list[i]
            sorted = False
    unsorted_until_index -= 1
    times += 1

print(''.join(card_list))
