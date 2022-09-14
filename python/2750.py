# sort 내장 함수

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
for e in arr:
    print(e)


# Bubble Sort

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for e in arr:
    print(e)


# Insertion Sort

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
    
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

for e in arr:
    print(e)