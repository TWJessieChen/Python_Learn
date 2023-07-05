#九九乘法表

#for in 迴圈
def print_nine_nine_table(): 
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
        print()

# Main function
if __name__ == '__main__':
   print_nine_nine_table()
