from collections import defaultdict
# 구현 문제
def solution(commands):
    answer = []    
    # 기본적으로 모든 셀은 자기 자신을 위치로 가짐
    # 자기 자신이 위치가 아니면 병합된 셀, 병합될 때 r1, r2의 값만 자기 자신의 위치를 가짐
    pos_chart = [[(i, j) for j in range(51)] for i in range(51)]
    
    # 문자열을 값으로 가지는 차트
    chart = [["" for _ in range(51)] for _ in range(51)]
    merge_table = defaultdict(set)
    
    def strToNum(*args):
        return tuple(map(int, args))
        
    # 차트의 값 접근은 항상 pos_chart를 통해서 한다.
    # 차트의 값 변경
    def select(r, c):
        r, c = strToNum(r, c)
        
        while pos_chart[r][c] != (r, c):
            chart[r][c] = ""
            r, c = pos_chart[r][c]
        return r, c
    
    # 값 변경
    def update(r, c, value):
        r, c = strToNum(r, c)
        r, c = select(r, c)        
        chart[r][c] = value
        return
    
    def update2(value1, value2):
        for r in range(51) :
            for c in range(51) :
                pr, pc = select(r, c)
                if chart[pr][pc] == value1:
                    chart[pr][pc] = value2
    
    # 차트의 값 합치기
    def merge(r1, c1, r2, c2):
        r1, c1, r2, c2 = strToNum(r1, c1, r2, c2)
        r1, c1 = select(r1,c1)
        r2, c2 = select(r2,c2)
        if (r1,c1) == (r2,c2):
            return
        temp_set = set(merge_table[(r1, c1)])
        
        if chart[r2][c2] != "" and chart[r1][c1] == "":
            pos_chart[r1][c1] = (r2, c2)
            merge_table[(r2,c2)].add((r1, c1))
            merge_table[(r2,c2)].update(merge_table[(r1, c1)])
            merge_table[(r1, c1)].clear()
        else:
            pos_chart[r2][c2] = (r1, c1)
            merge_table[(r1, c1)].add((r2,c2))
            merge_table[(r1, c1)].update(merge_table[(r2,c2)])
            merge_table[(r2,c2)].clear()
        return
    
    def unmerge(r, c):
        r, c = strToNum(r, c)
        ori_r, ori_c = r, c
        r, c = select(r, c)
        ori_value = chart[r][c]
        update(r, c, "")    
        for mr, mc in merge_table[(r, c)]:
            pos_chart[mr][mc] = (mr,mc)
            update(mr, mc, "")
        merge_table[(r, c)].clear()
        update(ori_r, ori_c, ori_value)
        
        return
    
    def printRC(r, c):
        r, c = strToNum(r, c)
        r, c = select(r,c)
        if chart[r][c] == "":
            answer.append("EMPTY")
        else:
            answer.append(chart[r][c])
        return
    
    ops = {"MERGE": merge, "UNMERGE": unmerge, "PRINT": printRC}
    
    
    
    for command in commands:
        op, *args = command.split()
        if op == "UPDATE":
            if len(args) == 3:
                update(*args)
            else:
                update2(*args)
        else:
            ops[op](*args)
    return answer