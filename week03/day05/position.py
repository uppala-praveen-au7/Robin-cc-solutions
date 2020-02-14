""" Coding Challenges:

1)Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order. 
[You may assume no duplicates in the array.]

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0 """

def locate_me(arr, number):

    if number in arr:
        return arr.index(number)
    else:
        for i in arr:
            if number < i:
                return arr.index(i)
        else:
            return len(arr)

List = [1,3,5,6]
pos = locate_me(List, 0)
print(pos)