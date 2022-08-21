from collections import defaultdict
from bisect import bisect_left, bisect_right

def query_count(wlist, query):
    return bisect_right(wlist, query.replace('?', 'z')) - bisect_left(wlist, query.replace('?', 'a'))

def solution(words, queries):
    answer = []
    wdict = defaultdict(list)
    wdict_reverse = defaultdict(list)
    
    for w in words:
        wdict[len(w)].append(w)
    for wr in words:
        wdict_reverse[len(wr)].append(wr[::-1])
    
    for wd in wdict.values():
        wd.sort()
    for wd in wdict_reverse.values():
        wd.sort()    
        
    for q in queries:
        if(q[0] == '?'):
            query = q[::-1]
            wlist = wdict_reverse[len(q)]
        else:
            query = q
            wlist = wdict[len(q)]
        answer.append(query_count(wlist, query))
    return answer