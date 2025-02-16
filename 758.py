def max_subarray_sum(arr):
    max_sum = float('-inf') 
    current_sum = 0 
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    k, x = map(int, input().split())
    arr[k-1] = x
    print(max_subarray_sum(arr))