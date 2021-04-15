def solution(array, commands):
    """
    array [start, end, k]
    """
    return [sorted(array[start-1:end])[k-1] for start, end, k in commands]
