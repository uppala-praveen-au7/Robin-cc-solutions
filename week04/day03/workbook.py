def workbook(n, k, book):
    special = 0
    page = 0
    # getting the chapter from book
    for chapter in book:
        page += 1
        # getting into the chaper
        for problem in range(1, chapter+1):
            # comparing the page no. with question no.
            if problem == page:
                print('problem: ',problem, 'on page No.',page)
                special += 1
            # turning the page
            if problem % k == 0 and problem != chapter:
                page += 1
    return special

# getting input
n, k = map(int, input().split())
book = list(map(int, input().split()))

# spitting the output
x = workbook(n,k,book)
print(x)