def counting_sort(arr):

    # getting largest element and creating other array
    maximum = max(arr) + 1
    count_arr = [0] * maximum
    sort_arr = [0] * len(arr)

    # storing the count of element
    for i in arr:
        count_arr[i] += 1 
    
    # storing commutative sum
    for i in range(1, maximum):
        count_arr[i] += count_arr[i-1]

    # sorting the array
    for i in arr:
        index = count_arr[i]-1
        sort_arr[index] = i
        count_arr[i] = count_arr[i]-1
    return sort_arr
    #print('sort :',sort_arr)

arr = [4,2,2,8,3,3,1]
sorted_array = counting_sort(arr)
print(sorted_array)
