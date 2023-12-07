import re
from collections import defaultdict
from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_order_j = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
hand_order = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
ordered_hands = [[] for i in range(len(hand_order))]


def is_smaller_than(a, b, joker=False):
    if joker:
        check_with = card_order_j
    else:
        check_with = card_order

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif check_with.index(a[i]) < check_with.index(b[i]):
            return True
        else:
            return False


# Part 1
hands_bids = defaultdict(int)
for line in lines:
    hands_bids[line.split()[0]] = int(line.split()[1])

for hand in hands_bids.keys():
    occurence = [*Counter("".join(sorted(hand))).values()]
    occurence.sort(reverse=True)
    # print(hand, occurence, hand_order.index(occurence), len(set(hand)) == len(hand))

    for i, ordered in enumerate(ordered_hands[hand_order.index(occurence)]):
        if is_smaller_than(hand, ordered):
            ordered_hands[hand_order.index(occurence)].insert(i, hand)
            break
    else:
        ordered_hands[hand_order.index(occurence)].append(hand)

ordered_hands = [j for sub in ordered_hands for j in sub]
ans = sum([hands_bids[x] * (i + 1) for i, x in enumerate(ordered_hands)])
print("Part 1:", ans)

# Part 2
ordered_hands = [[] for i in range(len(hand_order))]
for hand in hands_bids.keys():
    temp_rank = Counter("".join(sorted(hand)))
    if "J" in temp_rank.keys() and temp_rank["J"] < 5:
        num_of_jokers = temp_rank["J"]
        del temp_rank["J"]
        occurence = [*temp_rank.values()]
        occurence.sort(reverse=True)
        occurence[0] += num_of_jokers
    else:
        occurence = [*temp_rank.values()]
        occurence.sort(reverse=True)
    # print(hand, occurence, hand_order.index(occurence), len(set(hand)) == len(hand))

    for i, ordered in enumerate(ordered_hands[hand_order.index(occurence)]):
        if is_smaller_than(hand, ordered, True):
            ordered_hands[hand_order.index(occurence)].insert(i, hand)
            break
    else:
        ordered_hands[hand_order.index(occurence)].append(hand)

ordered_hands = [j for sub in ordered_hands for j in sub]
ans = sum([hands_bids[x] * (i + 1) for i, x in enumerate(ordered_hands)])
print("Part 2:", ans)
