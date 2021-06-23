def solution(s, n): 
    return  ''.join(map(lambda x: 
                    chr(97+(ord(x)+n)%97%26) if ord(x)>90 and x!=' '
                    else chr(65+(ord(x)+n)%65%26) if x!=' ' 
                    else x,s))