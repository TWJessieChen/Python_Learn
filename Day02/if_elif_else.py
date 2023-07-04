#if elif else 判斷式

#if elif else 判斷式
def print_if_elif_else(): 
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))
    print('輸入一個數字，如果大於1，則輸出3x-5，如果介於-1與1之間，則輸出x+2，如果小於-1，則輸出5x+3')

# if else if else 判斷式
def print_if_else_if_else(): 
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    else:
        if x >= -1:
            y = x + 2
        else:
            y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))
    print('多巢狀if else，這範例是兩層巢狀if else')
        
# Main function
if __name__ == '__main__':
   print_if_elif_else()
   print_if_else_if_else()

