from itertools import combinations
def get_ordered_pairs (arr):
    return combinations(sorted(arr), 2)

print(get_ordered_pairs([1,2,3]))
