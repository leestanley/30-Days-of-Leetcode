def progress_days(runs):
    count = 0
    for i in range(len(runs) + 1):
        if (runs[i + 1] > runs[i]):
            count += 1
    return count


print(progress_days([10, 11, 12, 9, 10]))
