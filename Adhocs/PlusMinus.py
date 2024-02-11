def plusMinus(arr, n):
    c_pos = c_neu = c_neg = 0
    for i in arr:
        if i > 0:
            c_pos += 1
        elif i < 0:
            c_neg = c_neg + 1
        else:
            c_neu = c_neu + 1
    
    print("{:.6f}".format((c_pos)/n))
    print("{:.6f}".format((c_neg)/n))
    print("{:.6f}".format((c_neu)/n))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr, n)
