#Print triangle pattern

#for_in 迴圈 列印三角形
def print_triangle_pattern(): 
    row = int(input('請輸入想列印的行數: '))
    
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()

# Main function
if __name__ == '__main__':
   print_triangle_pattern()
