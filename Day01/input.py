#Input function

# Function: 輸入數字進行計算
def input_word(): 
    # input() 輸入, int() 轉換成整數
    a = int(input('a = '))
    b = int(input('b = '))
    # %d 整數
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


# Main function
if __name__ == '__main__':
   input_word()