def smallest_difference(arr1, arr2):
    min_num = float("inf")
    pair = (arr1[0], arr2[0])
    for arr1_num in range(len(arr1)):
        for arr2_num in range(len(arr2)):
            temp = abs(arr1[arr1_num] - arr2[arr2_num])
            if temp < min_num:
                min_num = temp
                pair = [arr1[arr1_num], arr2[arr2_num]]
    return pair
