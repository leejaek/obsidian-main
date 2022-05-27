import sys

total_count, play_time = map(int, sys.stdin.readline().split())
card_list = list(sys.stdin.readline())[:-1]


def game_rule(left, right):
    if (left == 'R' and right == 'S') or (left == 'S' and right == 'P') or (left == 'P' and right == 'R'):
        return True
    return False


start_point = 0
for a in range(play_time):
    print(a)
    if start_point == total_count - 1:
        break
    for i in range(start_point, total_count-1):
        if game_rule(card_list[i], card_list[i+1]):
            card_list[i], card_list[i+1] = card_list[i+1], card_list[i]

    start_point += 1

print(''.join(card_list))
