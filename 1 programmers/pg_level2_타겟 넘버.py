import itertools
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = [0 for a in map(sum, itertools.product(*l)) if a==target]
    return len(s)


#문제에 더 어울리는 풀이
def solution2(numbers, target):
    tree = [0]
    for num in numbers:
        sub_tree = []
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
    return tree.count(target)
