data = [12,4,65,5,1,12,24]

# сортировка пузырьком
# for i in range(len(data)):
#     for i in range(len(data)-1):
#         if data[i+1] < data[i]:
#             el = data.pop(i+1)
#             data.insert(i, el)
#     print(data)

# быстрая сортировка (n log n)

def quick_sort(data):
    if len(data) <= 1:
        return data

    op = data[len(data)//2]

    left = []
    right = []
    middle = []
    for number in data:
        if number < op:
            left.append(number)
        elif number > op:
            right.append(number)
        else:
            middle.append(number)
    print(left, middle, right)
    return quick_sort(left)+middle+quick_sort(right)


# 1. quick_sort([4, 1]) + [5] + quick_sort([12, 65, 12, 24])
# 2. quick_sort([]) + [1] + quick_sort([4]) + [5] + quick_sort([12, 65, 12, 24])
# 3. [] + [1] + [4] + [5] + quick_sort([12,65, 12, 24])
# 4. [] + [1] + [4] + [5] + quick_sort([]) + [12, 12] +  quick_sort([65, 24])

print(quick_sort(data))