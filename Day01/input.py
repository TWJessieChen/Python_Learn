#Input function

# Function: 輸入數字進行計算
def input_int(): 
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


def input_float(): 
    # input() 輸入, float() 轉換成浮點數
    a = float(input('a = '))  
    b = float(input('b = '))
    # %f 整數
    print('%f + %f = %f' % (a, b, a + b))
    print('%f - %f = %f' % (a, b, a - b))
    print('%f * %f = %f' % (a, b, a * b))
    print('%f / %f = %f' % (a, b, a / b))
    print('%f // %f = %f' % (a, b, a // b))
    print('%f %% %f = %f' % (a, b, a % b))
    print('%f ** %f = %f' % (a, b, a ** b))


# Main function
if __name__ == '__main__':
   input_int()
   input_float()