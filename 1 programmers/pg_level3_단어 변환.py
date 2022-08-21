def solution(begin, target, words):
    answer = 0
    queue_list = [begin]
    while True:
        temp_list = []
        for queue_word in queue_list:
            if queue_word == target:
                return answer
            for word_idx in range(len(words)-1,-1,-1):
                temp_word = words[word_idx]
                diff = sum([x != y for x, y in zip(queue_word, temp_word)])
                if diff == 1:
                    temp_list.append(words.pop(word_idx))
        if not temp_list:
            return 0
        queue_list = temp_list
        answer += 1