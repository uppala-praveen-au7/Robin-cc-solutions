def is_leap(year):
    leap = False

    #this condition checks for the leap year ex:- 2004, 2008
    if year%4 == 0:
        #these two condiiton checks for the century leap year ex:- 2000
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

#check more about leap year
#https://www.youtube.com/watch?v=56zlm9qhVGc