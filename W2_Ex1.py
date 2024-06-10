def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []
    
    if k == 1:
        return num_list

    result = []
    n = len(num_list)
    
    for i in range(n - k + 1):
        window = num_list[i:i + k]
        max_value = window[0]
        
        for num in window:
            if num > max_value:
                max_value = num
        
        result.append(max_value)
    
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))  
