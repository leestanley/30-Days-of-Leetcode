def addBinary(a: str, b: str) -> str:
    def find_value(str1):
        str1 = str1[::-1]
        count = 0
        for i in range(len(str1)):
            if int(str1[i]) == 1:
                count += 2 ** i
        return count

    def build_string(x):
        return int(bin(x)[2:])

    num = find_value(a) + find_value(b)
    return build_string(num)
