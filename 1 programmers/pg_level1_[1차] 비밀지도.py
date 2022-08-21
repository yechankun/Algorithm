def solution(n, arr1, arr2):
    return list(
        map(
            lambda x: "{0:>{1}}".format(
                    bin(x[0]|x[1])[2:].replace("1",'#').replace("0"," "), 
                    n
                ),
            zip(arr1, arr2)
        )
    )
