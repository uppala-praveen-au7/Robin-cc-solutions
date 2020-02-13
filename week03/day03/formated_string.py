def print_formatted(number):

    l = len(bin(number)[2:])
    for i in range(1, number+1):

        Deci = str(i)
        Oct = oct(i)[2:]
        Hex = hex(i)[2:].upper()
        Bin = bin(i)[2:]
        print(Deci.rjust(l), Oct.rjust(l), Hex.rjust(l), Bin.rjust(l))
        
if __name__ == '__main__':
    n = int(input('Enter number: '))
    print_formatted(n)