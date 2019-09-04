def python_cheater(num):
    num = [int(i) for i in str(num)]
    num.sort()
    num = [str(i) for i in num]
    num = num[::-1]
    return int(''.join(num))


print(python_cheater(1254859723))
